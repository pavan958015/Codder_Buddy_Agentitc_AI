# 🤖 LeetCode Rank & Stats Showcase

A premium, responsive, single-page dashboard application that displays real-time LeetCode statistics and global ranking for any valid user. It defaults to the username `pavan9580` but allows searching for any active LeetCode user.

---

## ✨ Features

- **Dynamic Profile Lookup**: Fetches user profile picture, name, school/university, country, and bio directly from the API.
- **Problem Solving Breakdown**:
  - Displays the total number of solved questions out of the LeetCode catalog.
  - Interactive SVG circular progress ring animating the overall completion percentage.
  - Emerald Green, Amber Orange, and Rose Red progress bars for **Easy**, **Medium**, and **Hard** problems.
- **Premium Dark Mode Glassmorphism**: Built with modern CSS design aesthetics featuring glowing gradient blobs, blur effects, outline card borders, and smooth micro-animations.
- **Social Connect**: Link-outs to the user's GitHub, LinkedIn, and personal portfolio website (when available on LeetCode).
- **Responsive Layout**: Designed using CSS grids and flexbox, optimized for desktop, tablet, and mobile displays.
- **Skeleton Loaders**: Displays premium pulsing skeleton shapes during active API fetches.

---

## 🛠️ Technology Stack

- **Markup:** HTML5 (Semantic Structure)
- **Styling:** CSS3 (Vanilla layout with CSS variables, keyframe animations, custom gradients)
- **Icons:** FontAwesome v6.4.0
- **Typography:** Google Fonts (Outfit & Inter)
- **Scripting:** Modern Vanilla JavaScript (ES6 Fetch API, Promise concurrency)
- **Backend API:** Alfa LeetCode API (`alfa-leetcode-api.onrender.com`)

---

## 🚀 How to Run

Since the application is purely client-side, you can choose either of the following methods to view it:

### Method 1: Direct File Access
Simply double-click the `index.html` file in your system's file manager to open it in any modern web browser.

### Method 2: Local Web Server (Recommended)
To run a light development server, use Python or Node.js. 

Using Python:
```bash
# Navigate to the LeetCode-Rank-Showcase directory and run:
python -m http.server 8000
```
Then visit `http://localhost:8000` in your web browser.

---

## 📁 Project Structure

```text
LeetCode-Rank-Showcase/
├── index.html      # Main HTML structure and UI widgets layout
├── style.css       # Core theme variables, typography, animations, and layouts
└── app.js          # API integration, DOM updates, and circular progress logic
```
