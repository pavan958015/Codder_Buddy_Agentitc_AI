let eventSource = null;
let lastProjectDir = null;

// Submit prompt to backend via SSE stream
function submitPrompt(event) {
    event.preventDefault();
    
    const promptInput = document.getElementById('prompt');
    const recursionLimit = document.getElementById('recursion-limit').value;
    const submitBtn = document.getElementById('btn-submit');
    const prompt = promptInput.value.trim();

    if (!prompt) return;

    // Clean UI state
    clearConsole();
    resetTimeline();
    document.getElementById('success-panel').classList.add('hidden');
    
    // Disable inputs to prevent concurrent submissions
    promptInput.disabled = true;
    submitBtn.disabled = true;
    submitBtn.querySelector('.btn-text').textContent = 'Running Agent...';
    
    logToConsole('Orchestrating multi-agent system...', 'info-msg');
    logToConsole(`User Prompt: "${prompt}"`, 'system-msg');
    
    // Connect to Server-Sent Events stream
    const url = `/api/stream?prompt=${encodeURIComponent(prompt)}&recursion_limit=${recursionLimit}`;
    eventSource = new EventSource(url);

    eventSource.onmessage = function(e) {
        try {
            const eventData = JSON.parse(e.data);
            handleEvent(eventData);
        } catch (err) {
            console.error("Failed to parse event data:", err, e.data);
        }
    };

    eventSource.onerror = function(err) {
        console.error("SSE Connection Error:", err);
        logToConsole("SSE Connection disconnected or closed.", "info-msg");
        cleanup();
    };
}

// Clean up input states
function cleanup() {
    if (eventSource) {
        eventSource.close();
        eventSource = null;
    }
    document.getElementById('prompt').disabled = false;
    const submitBtn = document.getElementById('btn-submit');
    submitBtn.disabled = false;
    submitBtn.querySelector('.btn-text').textContent = 'Generate Project';
}

// Process streamed events from backend
function handleEvent(event) {
    const type = event.type;
    const data = event.data;

    switch (type) {
        case 'node_start':
            const node = data.node;
            logToConsole(`>>> Entering Node: ${node.toUpperCase()}`, 'info-msg');
            setTimelineStep(node, 'active');
            break;
            
        case 'node_end':
            const completedNode = data.node;
            logToConsole(`<<< Completed Node: ${completedNode.toUpperCase()}`, 'success-msg');
            setTimelineStep(completedNode, 'completed');
            break;
            
        case 'log':
            logToConsole(data.message, data.level || 'system-msg');
            break;
            
        case 'success':
            logToConsole("🎉 Generation process completed successfully!", "success-msg");
            renderSuccess(data.plan, data.project_dir);
            cleanup();
            break;
            
        case 'error':
            logToConsole(`❌ Error encountered: ${data.message}`, 'error-msg');
            cleanup();
            break;

        case 'done':
            logToConsole("Orchestrator run finished.", 'success-msg');
            cleanup();
            break;
    }
}

// Update UI Timeline Steps
function setTimelineStep(step, status) {
    const stepEl = document.getElementById(`step-${step}`);
    if (!stepEl) return;

    // Remove old classes
    stepEl.classList.remove('active', 'completed');
    
    const badgeEl = stepEl.querySelector('.step-badge');

    if (status === 'active') {
        stepEl.classList.add('active');
        badgeEl.textContent = 'Active';
    } else if (status === 'completed') {
        stepEl.classList.add('completed');
        badgeEl.textContent = 'Done';
    } else {
        badgeEl.textContent = 'Idle';
    }
}

// Reset Timeline states
function resetTimeline() {
    ['planner', 'architect', 'coder', 'reviewer'].forEach(step => {
        setTimelineStep(step, 'idle');
    });
}

// Print line to terminal console
function logToConsole(message, className = '') {
    const consoleOutput = document.getElementById('console-output');
    if (!consoleOutput) return;

    const line = document.createElement('div');
    line.className = `console-line ${className}`;
    line.textContent = message;
    
    consoleOutput.appendChild(line);
    
    // Auto-scroll to bottom
    consoleOutput.scrollTop = consoleOutput.scrollHeight;
}

// Clear terminal logs
function clearConsole() {
    const consoleOutput = document.getElementById('console-output');
    if (consoleOutput) {
        consoleOutput.innerHTML = '';
        logToConsole("Console cleared.", "system-msg");
    }
}

// Render Success card info
function renderSuccess(plan, projectDir) {
    const successPanel = document.getElementById('success-panel');
    if (!successPanel) return;

    lastProjectDir = projectDir;

    document.getElementById('res-project-name').textContent = plan.name || 'N/A';
    document.getElementById('res-project-path').textContent = projectDir || 'N/A';
    document.getElementById('res-project-tech').textContent = plan.techstack || 'N/A';

    const fileListEl = document.getElementById('res-file-list');
    fileListEl.innerHTML = '';

    if (plan.files && plan.files.length > 0) {
        plan.files.forEach(f => {
            const li = document.createElement('li');
            li.textContent = `${f.path} (${f.purpose})`;
            fileListEl.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.textContent = 'No files returned in plan metadata.';
        fileListEl.appendChild(li);
    }

    successPanel.classList.remove('hidden');
}

// Download project ZIP using lastProjectDir path
function downloadZip() {
    if (!lastProjectDir) {
        alert("No project path is active. Generate a project first.");
        return;
    }
    const url = `/api/download?project_dir=${encodeURIComponent(lastProjectDir)}`;
    window.location.href = url;
}

