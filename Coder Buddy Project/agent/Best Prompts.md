# Best Prompts for Project Creation with Coder Buddy

This file contains **25 high-quality, structured prompts** designed to get the best out of your Coder Buddy Agent. These prompts are divided into categories and tailored specifically to utilize the technology stack listed in the `Tech Used` file (Python backend, HTML/JS frontend, LocalStorage, MySQL, MongoDB, and local file storage).

---

## Table of Contents
1. [Full-Stack Web Applications with Database Integration](#1-full-stack-web-applications-with-database-integration)
2. [Productivity & Developer Tools](#2-productivity--developer-tools)
3. [Business & Management Portals](#3-business--management-portals)
4. [AI-Assisted & Data Visualization Tools](#4-ai-assisted--data-visualization-tools)
5. [Utilities & Interactive Applications](#5-utilities--interactive-applications)

---

## 1. Full-Stack Web Applications with Database Integration

### Prompt 1: Personal Finance Tracker & Budgeting Dashboard
> **Target Stack:** HTML/JS Frontend, Python Backend, MySQL Database, LocalStorage (for offline fallback)
```text
Build a Full-Stack Personal Finance Tracker application. 
- Backend: Python script handling API endpoints for transactions (income/expenses) with a MySQL database to persist data.
- Frontend: Single-page HTML interface styled with a modern dark glassmorphism theme and responsive design. 
- Features: 
  1. Add, edit, delete, and list transactions (fields: description, amount, category, date, type [income/expense]).
  2. A visual dashboard showing: Total Income, Total Expenses, and Net Balance.
  3. Interactive category-wise budget progress bars (e.g. Food: 80% used).
  4. Use LocalStorage to cache transactions so the page loads instantly, then sync with the MySQL database.
- Design: Clean Outfit/Inter typography, vibrant color accents (emerald green for income, rose red for expenses), and hover transitions on dashboard cards.
```

### Prompt 2: Kanban Task Board with Collaborative Workspace
> **Target Stack:** HTML/JS Frontend, Python Backend, MongoDB Database
```text
Create a collaborative Kanban Task Board web application.
- Backend: Python API connecting to a MongoDB database.
- Frontend: Responsive HTML layout with columns for "To Do", "In Progress", "In Review", and "Completed".
- Features:
  1. Add tasks with Title, Description, Priority (High, Medium, Low), Due Date, and Assignee.
  2. Implement drag-and-drop capability (or button-triggered status changes) to move cards between columns.
  3. Detail modal when clicking a task, allowing users to add comments and check off subtask items.
  4. Filter tasks by priority or search by title.
- Design: Modern slate UI with subtle color indicators for task priorities, smooth card animations on drag/drop, and clean custom scrollbars.
```

### Prompt 3: E-Commerce Product Catalog & Shopping Cart
> **Target Stack:** HTML/JS Frontend, Python Backend, MySQL Database
```text
Build a responsive E-Commerce Product Catalog application.
- Backend: Python API serving product data from a MySQL database.
- Frontend: Modern, elegant shopping interface.
- Features:
  1. Product grid displaying items with title, price, category, rating, and image placeholder.
  2. Live search bar and filter controls (by category, price range, and sorting by price/rating).
  3. Fully functional Shopping Cart sliding drawer where users can add items, increase/decrease quantities, and view a detailed subtotal breakdown (with simulated tax and shipping).
  4. A mock Checkout panel verifying address and payment info, resulting in an order confirmation screen.
- Design: Minimalist design using cream and charcoal colors, smooth image zoom transitions, and interactive slide-in animations.
```

### Prompt 4: Real-Time Chat Platform Simulation
> **Target Stack:** HTML/JS Frontend, Python Backend, MongoDB Database
```text
Develop a simulated Real-Time Chat application.
- Backend: Python backend saving messages and channels/rooms to MongoDB.
- Frontend: A twin-panel interface (Left: active chat channels & user list, Right: main chat feed and message input area).
- Features:
  1. Join/Create different chat channels (e.g., #general, #random, #dev).
  2. Input area supporting text, emojis, and simulated file uploads (saving file names and paths in MongoDB).
  3. Auto-polling mechanism in the frontend to refresh messages every 2 seconds to simulate real-time communication.
  4. User status indicators (Active, Away, Offline).
- Design: Modern Discord/Slack-style interface with a dark sidebar and soft-blue message bubbles, responsive toggle sidebar for mobile views.
```

### Prompt 5: Recipe Finder & Meal Planner
> **Target Stack:** HTML/JS Frontend, Python Backend, SQLite / MySQL Database
```text
Build a Recipe Finder and weekly Meal Planner.
- Backend: Python API managing recipe databases and saved meal plans.
- Frontend: Dynamic grid UI with cards.
- Features:
  1. Browse and search recipes by title, preparation time, or ingredients list.
  2. Interactive "Fridge Filter": Enter ingredients you currently have (e.g. tomato, chicken) and list matching recipes.
  3. Weekly Meal Calendar: Drag recipes into specific days (Monday - Sunday) and meals (Breakfast, Lunch, Dinner).
  4. Generate a combined shopping list based on the ingredients needed for the weekly plan.
- Design: Clean light mode layout using warm organic tones (terracotta and green accents), clear recipe card imagery, and expandable cooking steps.
```

---

## 2. Productivity & Developer Tools

### Prompt 6: Interactive Markdown Editor & Documentation Hub
> **Target Stack:** HTML/JS Frontend, Python Backend, File System Storage
```text
Create a Markdown Editor and Documentation Hub.
- Backend: Python script that reads/writes markdown files directly from/to a local folder structure (under agent's workspace).
- Frontend: Side-by-side split view. Left side: markdown code editor (with syntax guide); Right side: live rendered HTML preview using a library like Marked.js.
- Features:
  1. File tree navigation in a left panel showing files in the markdown directory.
  2. Save, Create New, and Rename markdown files.
  3. Search through file names and text contents.
  4. Export options: Download current document as Raw Markdown, HTML, or Print-to-PDF.
- Design: Sleek developer-focused dark mode interface using monospaced typography for the editor and standard clean sans-serif typography for the preview.
```

### Prompt 7: Custom REST API Testing Client (Postman Clone)
> **Target Stack:** HTML/JS Frontend, Python Backend (for request forwarding)
```text
Build a web-based REST API client mockup.
- Backend: Python proxy script using the `requests` library to execute HTTP calls requested by the frontend to bypass CORS limits.
- Frontend: Tabbed API builder interface.
- Features:
  1. Dynamic URL input box with a dropdown to select HTTP Methods (GET, POST, PUT, DELETE, PATCH).
  2. Interactive tabs for Request Headers, Query Parameters, and Request Body (supporting JSON, raw text, and URL-encoded).
  3. Response view panel with formatting for JSON payloads, status code highlights (green for 200, red for errors), response times, and header inspector.
  4. History log sidebar saving past requests in LocalStorage, allowing one-click reloading of old queries.
- Design: High-contrast interface resembling VS Code, featuring collapsable folders for requests and colored badge pills for status indicators.
```

### Prompt 8: Local System Performance Dashboard
> **Target Stack:** Python (psutil), HTML/JS Frontend
```text
Develop a Local System Performance Monitor Dashboard.
- Backend: Python script using `psutil` to extract CPU load (per core), memory utilization, disk usage, and network upload/download speeds. Save data to a history log.
- Frontend: Single-page real-time monitoring center.
- Features:
  1. Real-time graphs (line charts) showing CPU and RAM trends over the last 60 seconds (using Chart.js).
  2. Interactive alert configuration: set a threshold (e.g. CPU > 90%) that triggers a visual blinking warning on the screen.
  3. Table showing top 5 running processes consuming the most resources, with a mock/real "Kill Process" trigger.
- Design: Dark sci-fi dashboard theme with neon green/cyan glow graphs and modern grid layout.
```

### Prompt 9: Code Snippet Manager & Explainer
> **Target Stack:** HTML/JS Frontend, Python Backend, MongoDB Database
```text
Build a Developer Code Snippet Manager.
- Backend: Python backend storing code snippets, titles, tags, and explanations in a MongoDB database.
- Frontend: Searchable grid layout.
- Features:
  1. Save snippets with language tags (Python, JS, HTML, CSS, SQL).
  2. Integrated syntax highlighter (like Prism.js or Highlight.js) to display saved snippets.
  3. Search and filter code snippets by language, tag, or description.
  4. Quick Copy button for one-click clipboard copying.
- Design: Elegant developer dashboard using custom code themes, rounded cards, and smooth hover translations.
```

### Prompt 10: Port Scanner & Network Mapper Dashboard
> **Target Stack:** Python (socket), HTML/JS Frontend
```text
Build a Port Scanner and local network mapping application.
- Backend: Python script using standard socket libraries to scan a target IP address or hostname for open ports (common ranges).
- Frontend: Interactive scan hub.
- Features:
  1. IP address or host input area with range selector (e.g., Ports 1 to 1024 or custom).
  2. Live progress bar and logging panel showing currently scanned ports in real-time.
  3. Dynamic summary table showing open ports, detected services, and estimated security level (Low, Medium, High risk).
  4. Save scan reports to text files in the project workspace via the backend.
- Design: Terminal-inspired terminal theme combined with clean CSS layouts and alert states.
```

---

## 3. Business & Management Portals

### Prompt 11: Inventory & Stock Control Management System
> **Target Stack:** HTML/JS Frontend, Python Backend, MySQL Database
```text
Create an Inventory and Stock Control Management System.
- Backend: Python API connected to a MySQL database tracking inventory records and log audits.
- Frontend: Professional tabular interface with detailed data visualization.
- Features:
  1. Grid of inventory items (columns: SKU, Name, Description, Quantity, Price, Min Stock Alert Threshold, Category).
  2. Highlight rows where stock is below the threshold, and show a central "Items to Reorder" banner list.
  3. Quick update adjustments (Increment/Decrement stock controls) directly in the table.
  4. File upload capability: Accept CSV files of stock updates, parse them in Python, and update the MySQL database.
- Design: Enterprise-grade layout with clean tabular grids, responsive modals, and alert badges.
```

### Prompt 12: Employee Directory and Org Chart Visualizer
> **Target Stack:** HTML/JS Frontend, Python Backend, MongoDB Database
```text
Develop an Employee Directory and Interactive Org Chart.
- Backend: Python backend maintaining employee records (Name, Role, Department, Email, Manager, Profile Image Path).
- Frontend: Twin view (Tab 1: Directory, Tab 2: Interactive Tree Diagram of Org Structure).
- Features:
  1. Full search bar, department filters, and role filters.
  2. Add, update, and remove employees.
  3. Org Chart view: Build a visual, interactive hierarchy tree showing manager-employee relationships (using D3.js or simple CSS trees).
  4. Profile card generator: Click an employee to open a details modal showing contact details and direct reports.
- Design: Clean corporate presentation using soft grey backgrounds, pastel accents, and professional layout.
```

### Prompt 13: Booking and Appointment Scheduler
> **Target Stack:** HTML/JS Frontend, Python Backend, MySQL Database
```text
Create a Booking and Appointment Scheduler.
- Backend: Python API tracking services, slots, bookings, and customer details.
- Frontend: Calender-based booking page.
- Features:
  1. Interactive Calendar view (Daily/Weekly/Monthly) letting users select dates.
  2. Time slot selector that filters out already booked slots dynamically from the MySQL database.
  3. Booking form collecting Name, Email, Service type, and Notes.
  4. Admin dashboard listing upcoming bookings with options to Accept, Reschedule, or Cancel bookings, triggering simulated notification emails.
- Design: Elegant booking experience featuring a clean grid scheduler, pleasant animations, and warm color layouts.
```

### Prompt 14: Customer Relationship Manager (CRM) Dashboard
> **Target Stack:** HTML/JS Frontend, Python Backend, MongoDB Database
```text
Build a CRM (Customer Relationship Management) Web Portal.
- Backend: Python script saving lead information, interaction logs, and deals data in MongoDB.
- Frontend: Multi-pane layout showing metrics, pipelines, and activities.
- Features:
  1. Sales pipeline (Kanban board layout) showing deals moving through stages (Lead, Contacted, Proposal, Closed Won, Closed Lost).
  2. Interactive list of clients showing name, contact details, and their last contact date.
  3. Interaction logger: Click on a client to log a meeting, call, or email, creating an audit history timeline.
  4. Summary charts showing Deal Value distribution and Conversion Rates.
- Design: Sleek blue and white UI styling, custom charts, and smooth animations.
```

### Prompt 15: Student Attendance & Grade portal
> **Target Stack:** HTML/JS Frontend, Python Backend, MySQL Database
```text
Build a Student Grade and Attendance Portal.
- Backend: Python backend querying MySQL database containing student data, courses, grades, and attendance dates.
- Frontend: Split view (Teacher Portal for entries, Student Portal for report cards).
- Features:
  1. Teacher portal: select a subject class, view student checklist to mark attendance for current date, and input test grades.
  2. Student portal: login (simple drop-down switch) to see personal GPA trends, attendance percentage, and graded assignments.
  3. Interactive chart plotting test-by-test performance of students.
- Design: Dynamic layout with modern alert colors, neat grade report sheets, and intuitive navigation.
```

---

## 4. AI-Assisted & Data Visualization Tools

### Prompt 16: Dynamic CSV Data Analyzer & Plotter
> **Target Stack:** HTML/JS Frontend, Python Backend (Pandas/Matplotlib)
```text
Create a Dynamic CSV Data Analyzer.
- Backend: Python script using `pandas` to process uploads, parse CSV columns, calculate summary metrics (mean, median, count, null values), and output charts.
- Frontend: Drag-and-drop file upload screen leading to a data workspace.
- Features:
  1. Upload CSV file from system.
  2. Show a paginated, scrollable preview table of the raw data (first 50 rows).
  3. Dropdowns to select target columns for graphing (e.g. X-axis: Date, Y-axis: Sales).
  4. Chart generator: dynamic plot output (Line, Bar, Scatter) rendered using Chart.js or embedded matplotlib PNG exports.
- Design: Premium dark layout with dashboard panel grids, glassmorphism elements, and data loaders.
```

### Prompt 17: AI Writing Assistant & SEO Optimizer
> **Target Stack:** HTML/JS Frontend, Python Backend, Groq LLM API
```text
Build an AI Writing Assistant & SEO Optimizer web application.
- Backend: Python API connected to the Groq API (or Ollama local LLM) using LangChain.
- Frontend: Rich writing panel.
- Features:
  1. Live text area editor where user types articles or blog posts.
  2. Sidebar showing real-time word count, character count, and SEO score calculator (based on keyword density input).
  3. "AI Boost" features: select text to "Expand", "Shorten", or "Improve Tone" via LLM API calls.
  4. AI SEO Keyword Suggestion: Input a topic, and call the LLM to get 10 recommended tags and keywords to include.
- Design: distraction-free writing layout with soft lighting accents, responsive side panels, and typography options.
```

### Prompt 18: File Converter & Metadata Inspector
> **Target Stack:** HTML/JS Frontend, Python Backend (Pillow, PyPDF2)
```text
Develop a multi-format File Converter & Metadata Inspector tool.
- Backend: Python backend using libraries like Pillow (images) and PyPDF2 (PDFs) to convert files and extract metadata details.
- Frontend: Upload hub with dropzone.
- Features:
  1. Dropzone to upload files (PNG, JPG, PDF, TXT).
  2. Metadata viewer: Displays file dimensions, size, creation date, EXIF camera details, or page count.
  3. Image converter options (convert JPG to PNG, resize dimensions, compress file size).
  4. PDF converter options (extract pages, convert PDF pages to images).
- Design: Modern clean interface with progress bars, file preview icons, and drag-and-drop animations.
```

### Prompt 19: Survey Analytics & Sentiment Dashboard
> **Target Stack:** HTML/JS Frontend, Python Backend (Sentiment Analysis), MongoDB Database
```text
Create a Survey Analytics and Feedback Sentiment Dashboard.
- Backend: Python script containing a simple rule-based or LLM-based sentiment engine to analyze feedback as positive, neutral, or negative, saving entries in MongoDB.
- Frontend: Analytical metrics center.
- Features:
  1. Public survey form where users can submit reviews/comments and ratings (1-5 stars).
  2. Admin panel showing total reviews, average star rating, and a circular sentiment distribution chart (Positive vs Negative vs Neutral).
  3. Feed showing feedback items color-coded by sentiment (Green for positive, Red for negative).
  4. Filter submissions by sentiment or date.
- Design: Pastel accent dashboards, interactive charts, and polished visual alerts.
```

### Prompt 20: Visual Sitemap & Website Scraper
> **Target Stack:** Python (BeautifulSoup), HTML/JS Frontend
```text
Build a Visual Sitemap & Website Scraper.
- Backend: Python script utilizing `BeautifulSoup` and `requests` to parse a URL, extract internal/external links, image assets, meta tags, and page headings.
- Frontend: Single-page scanner dashboard.
- Features:
  1. URL text input to initiate website analysis.
  2. Interactive sitemap visual list showing the tree structure of internal page links found.
  3. Detailed tabs: Headers (H1, H2, H3 lists), Images (lists all image URLs and flags missing alt tags), SEO validation check.
  4. Download report button (JSON or HTML).
- Design: Clean minimalist layout, loaders for scanning processes, and searchable tabular reports.
```

---

## 5. Utilities & Interactive Applications

### Prompt 21: Flashcard Learning Engine with Spaced Repetition
> **Target Stack:** HTML/JS Frontend, Python Backend, LocalStorage / SQLite
```text
Build a Flashcard Learning Web Application.
- Backend: Python database manager tracking deck names, cards, difficulty status, and scheduled review times.
- Frontend: Interactive cards engine.
- Features:
  1. Deck manager: Create, edit, and delete card decks (e.g. Spanish Vocabulary, Python syntax).
  2. Studying mode: Flashcard flip animation showing Question/Front and Answer/Back.
  3. Review controls: rate difficulty of recall (Easy, Medium, Hard). Based on the response, calculate when the card should appear next using a Leitner-system spaced repetition algorithm.
  4. Dashboard showing daily progress charts and streaks.
- Design: Clean aesthetic focused on readability, glass card flip animations, and quick keyboard shortcut bindings.
```

### Prompt 22: Virtual Whiteboard & Mind Mapper
> **Target Stack:** HTML/JS Frontend, LocalStorage (for drawings)
```text
Create a Virtual Whiteboard and Mind Map tool.
- Frontend: Full screen HTML5 Canvas app with responsive controls.
- Features:
  1. Pen controls: select colors, brush size, eraser tool, and clear canvas.
  2. Shape tool: draw rectangles, circles, lines, and add text nodes.
  3. Mind-mapping mode: double-click to place node bubbles, drag to position them, and draw connect lines between nodes.
  4. Export canvas option (download as PNG image).
  5. Automatically save active board status to LocalStorage so progress is not lost on refresh.
- Design: Floating toolbar UI panel with clean glassmorphism styling and dark-mode slate grid background.
```

### Prompt 23: Password Manager & Security Vault
> **Target Stack:** HTML/JS Frontend, Python Backend, SQLite / File Storage
```text
Build a local Password Manager & Security Vault.
- Backend: Python backend handling encrypted file writes (using `cryptography` library) with a master password authorization setup.
- Frontend: Secure portal dashboard.
- Features:
  1. Master password input to decrypt the vault.
  2. Add, view, edit, and delete password items (fields: website, username, password, category, notes).
  3. Interactive password strength generator with criteria sliders (length, numbers, special characters, uppercase).
  4. Quick Copy button for usernames and passwords (with auto-clear clipboard warning).
- Design: Cyber-security theme with subtle gold or purple accents, blurred password value displays, and secure toggle buttons.
```

### Prompt 24: Expense Approval Workflow System
> **Target Stack:** HTML/JS Frontend, Python Backend, MySQL Database
```text
Create an Enterprise Expense Approval Portal.
- Backend: Python backend with database workflows for tracking expense status (Pending, Approved, Rejected, Paid).
- Frontend: Dual interface (Employee Submission view and Manager Approval queue).
- Features:
  1. Employee view: submit expense reports with description, amount, category, and local file attachment (for receipt upload).
  2. Manager view: list pending requests, download/view receipts, and buttons to approve or reject with comments.
  3. Real-time updates: show expense status logs and monthly company budget usage indicators.
- Design: Modern administrative UI dashboard, structured tables, visual receipt galleries, and neat filter bars.
```

### Prompt 25: Social Media Post Scheduler
> **Target Stack:** HTML/JS Frontend, Python Backend, SQLite / MongoDB
```text
Build a Social Media Post Scheduler dashboard.
- Backend: Python script tracking scheduled posts, statuses, platforms, and date schedules.
- Frontend: Calendar planner dashboard.
- Features:
  1. Composer view: Write post updates, attach media files, select platforms (Twitter, LinkedIn, Facebook).
  2. Interactive Calendar Scheduler showing scheduled posts on different calendar days.
  3. Simulation Queue: Background check (represented by a Python daemon/polling routine) that moves posts from "Scheduled" to "Published" once schedule time is met.
  4. Analysis graph: Mock engagement overview (likes, retweets) charts.
- Design: Clean modern social tool feel, intuitive visual calendar blocks, and responsive side sheets.
```
