/**
 * UniversityData object holding static content for the university website.
 */
const UniversityData = {
    name: "Global Tech University",
    missionStatement: "To foster innovation and academic excellence through cutting-edge research and a commitment to community service.",
    contactInfo: {
        email: "info@gtu.edu",
        phone: "+1 (555) 123-4567",
        address: "101 University Drive, City, State"
    }
};

/**
 * Minimal JavaScript for interactivity.
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log("University Data loaded:", UniversityData);

    // 1. Simple Smooth Scrolling Implementation (Optional but good practice)
    if ('scrollBehavior' in document.documentElement.style) {
        document.body.style.scrollBehavior = 'smooth';
    } else {
        // Fallback for older browsers if needed, though modern browsers support it well.
        console.log("Smooth scrolling not fully supported or style not applied.");
    }

    // 2. Simple Navigation Menu Toggle Example (Placeholder)
    const navToggle = document.getElementById('nav-toggle');
    if (navToggle) {
        navToggle.addEventListener('click', () => {
            const menu = document.getElementById('main-navigation');
            if (menu) {
                // Simple toggle logic: add/remove a class to show/hide the menu
                menu.classList.toggle('active');
            }
        });
    }

    // Example of using data in the DOM (assuming an element with id 'university-name' exists)
    const nameElement = document.getElementById('university-name');
    if (nameElement) {
        nameElement.textContent = UniversityData.name;
    }
});