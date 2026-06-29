# CyberScan Pro - Project Diary

## Day 0 – Planning & Environment Setup

**Date:** 28 June 2026

### Objective

Prepare the complete development environment for the CyberScan Pro project, initialize version control, and organize the project structure following professional software development practices.

---

## Tasks Completed

### Development Environment

* Installed and configured Visual Studio Code.
* Verified Python 3 installation.
* Created and activated a Python virtual environment (`venv`).
* Installed required Python packages:

  * Flask
  * Requests
  * BeautifulSoup4
  * python-nmap
  * ReportLab

### Project Setup

* Created the project folder:

  * `CyberScan-Pro`
* Generated `requirements.txt`.
* Created the initial project structure.
* Added project folders for documentation, templates, static files, reports, screenshots, scanner modules, and database.

### Version Control

* Initialized a local Git repository.
* Renamed the default branch to `main`.
* Configured Git username and email.
* Created a public GitHub repository named **CyberScan-Pro**.
* Connected the local repository to GitHub.
* Performed the first commit.
* Successfully pushed the project to GitHub.

---

## Project Structure

* app.py
* config.py
* README.md
* requirements.txt
* docs/
* scanner/
* templates/
* static/

  * css/
  * js/
  * images/
* database/
* reports/
* screenshots/
* venv/

---

## Tools Used

* Kali Linux
* Visual Studio Code
* Python 3
* Git
* GitHub
* Flask
* pip

---

## Challenges Faced

1. Git displayed **Author identity unknown** during the first commit.
2. Configured Git with the correct username and GitHub email.
3. Successfully committed and pushed the project after configuration.

---

## Skills Learned

* Creating a professional Python project structure.
* Creating and activating virtual environments.
* Installing project dependencies.
* Initializing Git repositories.
* Creating GitHub repositories.
* Connecting local projects to GitHub.
* Performing Git commits and pushes.
* Organizing a cybersecurity software project.

---

## Git Commands Practiced

* git init
* git branch -M main
* git status
* git add .
* git commit
* git remote add origin
* git push

---

## Deliverables

* Development environment ready.
* Professional project structure created.
* Git repository initialized.
* GitHub repository connected.
* First project commit completed.

---

## Outcome

The CyberScan Pro development environment is fully prepared. The project is version-controlled with Git and synchronized with GitHub. The repository is now ready for feature development.

---

## Next Day Plan (Day 1)

* Learn the basics of Flask.
* Create the first Flask application.
* Build the project homepage.
* Run the application on the local development server.
* Understand routing and templates.
* Push the first working version to GitHub.

-------------------------------------------------------------------------------------------------

# Day 1 – Flask Web Application Development

**Date:** 29 June 2026

## Objective
Build the first working version of CyberScan Pro using Flask and understand the basics of web application development.

---

## Tasks Completed

- Learned the basics of Flask.
- Created the first Flask application (`app.py`).
- Created the first route (`/`).
- Connected Flask with HTML templates.
- Created `base.html` using template inheritance.
- Created `index.html` for the homepage.
- Linked CSS using Flask static files.
- Designed a basic CyberScan Pro homepage.
- Added navigation bar and footer.
- Styled the webpage using CSS.
- Successfully ran the Flask development server.
- Tested the application in the browser.

---

## Files Created / Updated

- app.py
- templates/base.html
- templates/index.html
- static/css/style.css

---

## Concepts Learned

- Flask Framework
- Web Server
- Routing
- HTML Templates
- Template Inheritance
- Static Files
- CSS Styling
- Request and Response Cycle

---

## Result

Successfully created the first working CyberScan Pro web application. The homepage loads correctly in the browser with a navigation bar, content section, button, and footer.

---

## Challenges Faced

- Understanding Flask routing.
- Learning template inheritance.
- Linking CSS correctly.
- Designing the first webpage.

---

## Skills Gained

- Flask Basics
- HTML
- CSS
- Web Application Structure
- Frontend and Backend Connection

---

## Git Commands Used

git add .

git commit -m "Day 1: Build Flask homepage with template inheritance"

git push

---

## Next Day Plan

- Add URL input field.
- Validate website URLs.
- Build the first website scanning feature.
- Display scan results on the webpage.

-----------------------------------------------------------------------------------------------------------------

# Day 2 – Website Connectivity Scanner

**Date:** 30 June 2026

## Objective
Develop the first functional scanning feature by allowing users to enter a website URL, validating the input, checking website availability, and displaying results on the webpage.

---

## Tasks Completed

- Added HTML form for website URL input.
- Implemented POST request handling in Flask.
- Captured user input using Flask request object.
- Connected Python with HTML templates using Jinja2.
- Used the Requests library to connect to websites.
- Retrieved HTTP status codes.
- Displayed scan results on the webpage.
- Implemented exception handling for:
  - Invalid URLs
  - Connection errors
  - Request timeouts
- Improved the user experience with friendly error messages.

---

## Files Updated

- app.py
- templates/index.html

---

## Concepts Learned

- HTML Forms
- GET vs POST Requests
- Flask Request Object
- Requests Library
- HTTP Status Codes
- Jinja2 Template Variables
- Conditional Rendering
- Exception Handling (try/except)

---

## Result

CyberScan Pro can now:

- Accept website URLs.
- Validate user input.
- Connect to live websites.
- Detect whether a website is reachable.
- Display HTTP status codes.
- Show success and error messages without crashing.

---

## Challenges Faced

- Understanding POST requests.
- Reading form data in Flask.
- Handling invalid URLs.
- Managing connection errors gracefully.

---

## Skills Gained

- Flask Backend Development
- Dynamic HTML Rendering
- HTTP Communication
- Python Requests Library
- Error Handling
- Basic Web Security Scanner Development

---

## Git Commands Used

git add .

git commit -m "Day 2: Implement URL validation and website availability scanner"

git push

---

## Next Day Plan

- Learn HTTP Headers.
- Build the Security Headers Scanner.
- Detect missing security headers.
- Display security analysis results.