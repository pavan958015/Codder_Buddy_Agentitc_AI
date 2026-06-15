// DOM Elements
const searchForm = document.getElementById('search-form');
const usernameInput = document.getElementById('username-input');
const dashboard = document.getElementById('dashboard');
const errorContainer = document.getElementById('error-container');
const errorTitle = document.getElementById('error-title');
const errorMessage = document.getElementById('error-message');
const errorRetryBtn = document.getElementById('error-retry-btn');

// Card contents vs skeleton wrappers
const cards = ['profile-card', 'rank-card', 'reputation-card', 'solved-card'];

// LeetCode total questions approximate counts (Updated mid-2026)
const TOTAL_EASY = 830;
const TOTAL_MEDIUM = 1720;
const TOTAL_HARD = 750;
const TOTAL_ALL = TOTAL_EASY + TOTAL_MEDIUM + TOTAL_HARD; // ~3300

// Initialize Circle Progress
const circleProgress = document.getElementById('circle-progress');
const circlePercent = document.getElementById('circle-percent');
const RADIUS = 70;
const CIRCUMFERENCE = 2 * Math.PI * RADIUS;

if (circleProgress) {
    circleProgress.style.strokeDasharray = `${CIRCUMFERENCE} ${CIRCUMFERENCE}`;
    circleProgress.style.strokeDashoffset = CIRCUMFERENCE;
}

// Set circular progress bar value
function setCircleProgress(percent) {
    if (!circleProgress) return;
    const offset = CIRCUMFERENCE - (percent / 100) * CIRCUMFERENCE;
    circleProgress.style.strokeDashoffset = offset;
    
    // Animate percentage text count up
    let start = 0;
    const end = Math.round(percent);
    if (end === 0) {
        circlePercent.textContent = '0%';
        return;
    }
    const duration = 1000; // 1s
    const stepTime = Math.abs(Math.floor(duration / end));
    
    const timer = setInterval(() => {
        start++;
        circlePercent.textContent = `${start}%`;
        if (start >= end) {
            clearInterval(timer);
            circlePercent.textContent = `${end}%`;
        }
    }, Math.max(stepTime, 15));
}

// Show skeleton load state
function showLoading() {
    errorContainer.classList.add('hidden');
    dashboard.classList.remove('hidden');
    
    cards.forEach(cardId => {
        const card = document.getElementById(cardId);
        if (card) {
            const skeleton = card.querySelector('.skeleton-wrapper');
            const content = card.querySelector(`.${cardId.split('-')[0]}-content`);
            if (skeleton) skeleton.classList.remove('hidden');
            if (content) content.classList.add('hidden');
        }
    });
}

// Hide loading state
function hideLoading() {
    cards.forEach(cardId => {
        const card = document.getElementById(cardId);
        if (card) {
            const skeleton = card.querySelector('.skeleton-wrapper');
            const content = card.querySelector(`.${cardId.split('-')[0]}-content`);
            if (skeleton) skeleton.classList.add('hidden');
            if (content) content.classList.remove('hidden');
        }
    });
}

// Show error state
function showError(title, message) {
    dashboard.classList.add('hidden');
    errorContainer.classList.remove('hidden');
    errorTitle.textContent = title;
    errorMessage.textContent = message;
}

// Fetch user data from alfa-leetcode-api
async function fetchLeetCodeData(username) {
    showLoading();
    
    const cleanUsername = username.trim();
    if (!cleanUsername) {
        showError('Invalid Username', 'Please enter a valid LeetCode username.');
        return;
    }
    
    try {
        // Fetch both profile and solved problems stats concurrently
        const [profileRes, solvedRes] = await Promise.all([
            fetch(`https://alfa-leetcode-api.onrender.com/${cleanUsername}`),
            fetch(`https://alfa-leetcode-api.onrender.com/${cleanUsername}/solved`)
        ]);
        
        if (!profileRes.ok || !solvedRes.ok) {
            throw new Error('User not found or API error.');
        }
        
        const profileData = await profileRes.json();
        const solvedData = await solvedRes.json();
        
        // Check if the API returned an error message inside a successful response code
        if (profileData.errors || profileData.error || profileData.message === "user does not exist") {
            throw new Error('User does not exist');
        }
        
        updateUI(profileData, solvedData);
        hideLoading();
        
    } catch (error) {
        console.error('Error fetching LeetCode data:', error);
        showError(
            'User Not Found',
            `Could not retrieve stats for "${cleanUsername}". Please verify the spelling and ensure the profile is public.`
        );
    }
}

// Update UI elements with data
function updateUI(profile, solved) {
    // 1. Profile Panel Update
    const avatar = document.getElementById('user-avatar');
    const name = document.getElementById('user-name');
    const usernameText = document.getElementById('user-username-text');
    const school = document.getElementById('user-school');
    const country = document.getElementById('user-country');
    const bio = document.getElementById('user-bio');
    
    avatar.src = profile.avatar || 'https://assets.leetcode.com/users/default_avatar.png';
    name.textContent = profile.name || profile.username || 'No Name';
    usernameText.textContent = profile.username;
    
    // Bio
    bio.textContent = profile.about || 'Slow but determined.';
    
    // Meta (School & Country)
    const schoolContainer = document.getElementById('meta-school-container');
    if (profile.school) {
        school.textContent = profile.school;
        schoolContainer.classList.remove('hidden');
    } else {
        schoolContainer.classList.add('hidden');
    }
    
    const countryContainer = document.getElementById('meta-country-container');
    if (profile.country) {
        country.textContent = profile.country;
        countryContainer.classList.remove('hidden');
    } else {
        countryContainer.classList.add('hidden');
    }
    
    // Social Links
    const githubLink = document.getElementById('link-github');
    const linkedinLink = document.getElementById('link-linkedin');
    const websiteLink = document.getElementById('link-website');
    
    if (profile.gitHub) {
        githubLink.href = profile.gitHub;
        githubLink.classList.remove('hidden');
    } else {
        githubLink.classList.add('hidden');
    }
    
    if (profile.linkedIN) {
        linkedinLink.href = profile.linkedIN;
        linkedinLink.classList.remove('hidden');
    } else {
        linkedinLink.classList.add('hidden');
    }
    
    if (profile.website && profile.website.length > 0) {
        websiteLink.href = profile.website[0];
        websiteLink.classList.remove('hidden');
    } else {
        websiteLink.classList.add('hidden');
    }
    
    // Skills Tags
    const tagsContainer = document.getElementById('skills-tags');
    tagsContainer.innerHTML = '';
    const skills = profile.skillTags || [];
    if (skills.length > 0) {
        skills.forEach(skill => {
            const span = document.createElement('span');
            span.className = 'tag';
            span.textContent = skill;
            tagsContainer.appendChild(span);
        });
        document.querySelector('.tags-section').classList.remove('hidden');
    } else {
        document.querySelector('.tags-section').classList.add('hidden');
    }
    
    // 2. Global Rank & Reputation
    const globalRank = document.getElementById('global-rank');
    const rankPercent = document.getElementById('rank-percent');
    const userReputation = document.getElementById('user-reputation');
    
    const rank = profile.ranking || 0;
    globalRank.textContent = rank > 0 ? `#${rank.toLocaleString()}` : 'Unranked';
    
    // Estimate percentile rank based on rank (approx 4M active LeetCode users)
    const totalUsersEstimate = 5000000;
    const percentile = rank > 0 ? ((rank / totalUsersEstimate) * 100).toFixed(2) : '0';
    rankPercent.textContent = percentile;
    
    userReputation.textContent = (profile.reputation || 0).toLocaleString();
    
    // 3. Solved Problems statistics
    const totalSolved = solved.solvedProblem || 0;
    const easySolved = solved.easySolved || 0;
    const mediumSolved = solved.mediumSolved || 0;
    const hardSolved = solved.hardSolved || 0;
    
    document.getElementById('total-solved').textContent = totalSolved;
    document.getElementById('total-questions').textContent = TOTAL_ALL;
    
    document.getElementById('easy-solved').textContent = easySolved;
    document.getElementById('medium-solved').textContent = mediumSolved;
    document.getElementById('hard-solved').textContent = hardSolved;
    
    // Update labels for maximum questions
    document.querySelector('.easy .max-total').textContent = `/${TOTAL_EASY}`;
    document.querySelector('.medium .max-total').textContent = `/${TOTAL_MEDIUM}`;
    document.querySelector('.hard .max-total').textContent = `/${TOTAL_HARD}`;
    
    // Set percentages for progress bars
    const easyPct = (easySolved / TOTAL_EASY) * 100;
    const mediumPct = (mediumSolved / TOTAL_MEDIUM) * 100;
    const hardPct = (hardSolved / TOTAL_HARD) * 100;
    
    // Apply width with delay for transition effect
    setTimeout(() => {
        document.getElementById('easy-bar').style.width = `${Math.min(easyPct, 100)}%`;
        document.getElementById('medium-bar').style.width = `${Math.min(mediumPct, 100)}%`;
        document.getElementById('hard-bar').style.width = `${Math.min(hardPct, 100)}%`;
    }, 100);
    
    // Set circular progress
    const totalPct = (totalSolved / TOTAL_ALL) * 100;
    setCircleProgress(Math.min(totalPct, 100));
}

// Event Listeners
searchForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = usernameInput.value.trim();
    if (username) {
        fetchLeetCodeData(username);
    }
});

errorRetryBtn.addEventListener('click', () => {
    usernameInput.value = 'pavan9580';
    fetchLeetCodeData('pavan9580');
});

// Initial Load
document.addEventListener('DOMContentLoaded', () => {
    fetchLeetCodeData('pavan9580');
});
