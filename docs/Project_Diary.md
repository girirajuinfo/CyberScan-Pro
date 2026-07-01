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

--------------------------------------------------------------------------------------------------------------------------------

# 📅 Day 3 – HTTP Security Headers Scanner

**Date:** 29 June 2026

## Objective

The objective of Day 3 was to transform CyberScan Pro from a website availability checker into a real web security assessment tool by implementing an HTTP Security Headers Scanner.

---

## Work Completed

### 1. Created a Modular Scanner Structure

Created a dedicated Python package named `scanner` to organize the scanning modules.

Created files:

* scanner/**init**.py
* scanner/headers.py

This separates the scanning logic from the Flask application and follows a professional project structure.

---

### 2. Implemented Security Header Scanner

Implemented a new function `check_security_headers()` inside `headers.py`.

The scanner checks for the following important HTTP security headers:

* Content-Security-Policy
* Strict-Transport-Security
* X-Frame-Options
* X-Content-Type-Options
* Referrer-Policy
* Permissions-Policy

Each header is marked as either **Present** or **Missing**.

---

### 3. Integrated Scanner with Flask

Imported the scanner module into `app.py`.

After the website responds successfully, CyberScan Pro automatically performs a security header analysis and stores the results inside the result dictionary.

---

### 4. Updated Frontend

Modified `templates/index.html` to display a new section named **Security Header Analysis**.

Implemented a dynamic HTML table using Jinja2 that displays:

* Security Header Name
* Status (Present / Missing)

---

### 5. Tested the Scanner

Successfully scanned:

https://google.com

Verified:

* Website connectivity
* HTTP Status Code
* Security Header Analysis
* Dynamic result rendering

The scanner successfully displayed the detected security headers on the web interface.

---

## Concepts Learned

* Python Packages
* Modular Project Structure
* Python Modules
* Importing Custom Functions
* HTTP Response Headers
* Security Header Analysis
* Flask Integration
* Jinja2 Loops
* Dynamic HTML Tables
* Dictionary Iteration

---

## Challenges Faced

* Organizing scanner modules correctly.
* Importing functions from another Python file.
* Displaying dictionary data inside HTML.
* Understanding HTTP security headers.

All issues were successfully resolved.

---

## Outcome

CyberScan Pro can now:

* Accept a website URL
* Connect to the target website
* Analyze important HTTP security headers
* Display a professional security analysis table

This marks the first real cybersecurity scanning capability of the project.

---

## Git Commit

Day 3: Implement HTTP security headers scanner

---

## Project Status

Completed Successfully ✅

--------------------------------------------------------------------------------------------------------------------------------------

# Day 4 – SSL Certificate Scanner

## Objective

Implemented SSL certificate analysis to verify HTTPS configuration and certificate validity.

## Tasks Completed

- Created ssl_checker.py module
- Used Python ssl library
- Used socket module for secure connections
- Retrieved SSL certificate from target website
- Extracted certificate issuer
- Extracted certificate expiry date
- Calculated remaining validity period
- Displayed SSL analysis in Flask interface
- Integrated SSL scanner into app.py
- Updated HTML template to show SSL details

## Files Modified

- app.py
- scanner/ssl_checker.py
- templates/index.html

## Concepts Learned

- SSL/TLS
- HTTPS
- X.509 Certificates
- socket module
- ssl module
- datetime calculations
- Modular programming

## Result

CyberScan Pro can now verify SSL certificates, display the certificate issuer, expiry date, remaining validity period, and certificate status.

--------------------------------------------------------------------------------------------------------------------------------------------------

# 📅 Day 5 – robots.txt & sitemap.xml Scanner

**Date:** 01 July 2026

## Objective

The objective of Day 5 was to implement website discovery file scanning by checking the availability of robots.txt and sitemap.xml files.

---

## Work Completed

### 1. Created robots.py Module

Created a dedicated scanner module named `robots.py` inside the `scanner` package.

---

### 2. Implemented robots.txt Scanner

Developed functionality to automatically check whether the target website contains a robots.txt file.

Example:

https://example.com/robots.txt

The scanner reports whether the file exists.

---

### 3. Implemented sitemap.xml Scanner

Developed functionality to automatically check whether the target website contains a sitemap.xml file.

Example:

https://example.com/sitemap.xml

The scanner reports whether the file exists.

---

### 4. Integrated Scanner with Flask

Imported the robots scanner into `app.py`.

Executed the scanner automatically after successful website connectivity and SSL analysis.

Stored the results inside the result dictionary.

---

### 5. Updated Frontend

Added a new section named **Website Discovery Files**.

Displayed:

- robots.txt Status
- sitemap.xml Status

using a dynamic HTML table.

---

## Files Modified

- app.py
- scanner/robots.py
- templates/index.html

---

## Concepts Learned

- Website Reconnaissance
- robots.txt
- sitemap.xml
- URL Parsing
- Dynamic URL Generation
- HTTP Requests
- Flask Module Integration
- Dynamic HTML Rendering

---

## Challenges Faced

- Constructing robots.txt and sitemap.xml URLs.
- Integrating multiple scanner modules.
- Displaying dynamic scan results.

Successfully resolved all issues.

---

## Result

CyberScan Pro can now:

- Detect robots.txt
- Detect sitemap.xml
- Display website discovery information
- Perform multiple security checks from a single scan

---

## Git Commit

Day 5: Implement robots.txt and sitemap.xml scanner

---

## Project Status

Completed Successfully ✅