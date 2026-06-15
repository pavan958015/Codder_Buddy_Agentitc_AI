// frontend/app.js

document.addEventListener("DOMContentLoaded", () => {
    const mysqlIndicator = document.querySelector(".mysql-status .status-indicator");
    const mongoIndicator = document.querySelector(".mongo-status .status-indicator");

    const mysqlForm = document.getElementById("mysql-connection-form");
    const mongoForm = document.getElementById("mongo-connection-form");

    const mysqlTableBody = document.querySelector("#mysql-instances-table tbody");
    const mongoTableBody = document.querySelector("#mongo-instances-table tbody");

    const API_BASE_URL = "http://127.0.0.1:8000";

    // Function to fetch database health from FastAPI backend
    async function checkDatabaseHealth() {
        try {
            const response = await fetch(`${API_BASE_URL}/health`);
            if (!response.ok) throw new Error("Backend offline");

            const data = await response.json();

            // Update MySQL indicator
            if (data.mysql_check && data.mysql_check.includes("established")) {
                mysqlIndicator.textContent = "Online";
                mysqlIndicator.className = "status-indicator online";
                addInstanceToTable(mysqlTableBody, "mysql-1", "localhost", "3306", "Active");
            } else {
                mysqlIndicator.textContent = "Offline";
                mysqlIndicator.className = "status-indicator offline";
            }

            // Update MongoDB indicator
            if (data.mongo_check && data.mongo_check.includes("connected")) {
                mongoIndicator.textContent = "Online";
                mongoIndicator.className = "status-indicator online";
                addInstanceToTable(mongoTableBody, "mongo-1", "mongodb://localhost:27017", null, "Active");
            } else {
                mongoIndicator.textContent = "Offline";
                mongoIndicator.className = "status-indicator offline";
            }
        } catch (error) {
            console.error("Health check failed:", error);
            
            mysqlIndicator.textContent = "Offline";
            mysqlIndicator.className = "status-indicator offline";
            
            mongoIndicator.textContent = "Offline";
            mongoIndicator.className = "status-indicator offline";
        }
    }

    // Helper to add instance to UI table
    function addInstanceToTable(tableBody, id, hostOrUri, port, status) {
        // Clear existing rows
        tableBody.innerHTML = "";

        const row = document.createElement("tr");
        if (port) {
            row.innerHTML = `
                <td>${id}</td>
                <td>${hostOrUri}</td>
                <td>${port}</td>
                <td><span class="status-indicator online">${status}</span></td>
                <td><button class="btn delete-btn" onclick="this.closest('tr').remove()">Remove</button></td>
            `;
        } else {
            row.innerHTML = `
                <td>${id}</td>
                <td>${hostOrUri}</td>
                <td><span class="status-indicator online">${status}</span></td>
                <td><button class="btn delete-btn" onclick="this.closest('tr').remove()">Remove</button></td>
            `;
        }
        tableBody.appendChild(row);
    }

    // Handle MySQL Test Connection Form
    mysqlForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const host = document.getElementById("mysql-host").value;
        const port = document.getElementById("mysql-port").value;

        alert(`Testing MySQL connection to ${host}:${port} via FastAPI backend...`);
        // Trigger health check again
        await checkDatabaseHealth();
    });

    // Handle MongoDB Test Connection Form
    mongoForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const uri = document.getElementById("mongo-uri").value;

        alert(`Testing MongoDB connection to ${uri} via FastAPI backend...`);
        // Trigger health check again
        await checkDatabaseHealth();
    });

    // Initial check
    checkDatabaseHealth();
});
