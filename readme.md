# LogEval

This is the front end of A Comprehensive Benchmark Suite for LLMs in Log Analysis (https://nkcs.iops.ai/LogEval/). The warehouse results are as follows. 

## Project Structure Overview
```
old_proj/
static/
templates/
translations/
└── en/
    └── LC_MESSAGES/
         ├── messages.mo
         └── messages.po
app.py								# Application entry point
babel.cfg							# Multilingual configure
datasrc.py							# Acquisition of variable resources
index.html							# Website entry point
leaderboard.csv						        # Leaderboard data
messages.pot						        # Multilingual related
news.json							# News data
requirements.txt					        # Requirements for running
submitted.csv						        # Submitted data from users
```

## Detailed File and Directory Descriptions
### 1. Core Application Files
**app.py**

- **Purpose:** Main application entry point and Flask server controller

- **Contents:**
  - Flask application initialization and configuration
  - Route definitions for all website endpoints
  - View functions that handle HTTP requests
  - Template rendering with Jinja2
  - Integration with other modules (datasrc.py, multilingual support)
  - Server startup logic

- **Key Features:**
  - Handles user requests and routes to appropriate views
  - Integrates with Babel for internationalization
  - Processes form submissions

**index.html**

- **Purpose:** Primary website entry point and landing page

- **Contents:**

  - HTML structure with Jinja2 templating

  - Navigation to different sections of the benchmark suite

  - Overview of LogEval's purpose and capabilities

  - Links to leaderboard, documentation, and submission areas

- **Key Features:**

  - Serves as the root page of the application

  - Provides quick access to all major sections

### 2. Data Management Files
**datasrc.py**

- **Purpose:** Data acquisition and resource management module

- **Contents:**

  - Functions to read and process CSV/JSON data files

  - Data transformation logic for presentation

  - Integration with leaderboard.csv and submitted.csv

- **Key Features:**

  - Abstracts data access from presentation logic

  - Provides clean API for data retrieval

**leaderboard.csv**

- **Purpose:** Storage for benchmark results and rankings

- **Structure:**

  - Columns for model names, evaluation methods, evaluation metrics

  - Categorization by task types

- **Usage:**

  - Primary data source for the leaderboard display

  - Updated with new evaluation results

  - Read by datasrc.py and presented in templates

**submitted.csv**

- **Purpose:** Repository for user-submitted demands

- **Structure:**

  - Columns for submitter information, model details

- **Usage:**

  - Stores all user demand

  - Potential source for updating leaderboard.csv

**news.json**

- **Purpose:** Storage for announcements and news

- **Structure:**

  - JSON array of news items

  - Each item contains title, scription, time, and link

- **Usage:**

  - Powers the "News" section

### 3. Internationalization Files
**babel.cfg**

- **Purpose:** Configuration file for Babel localization

- **Contents:**

  - File path patterns for string extraction

  - Template parsing configurations

  - Encoding settings

  - Mapping between source files and translation domains

- **Usage:**

  - Guides the Babel tool in extracting translatable strings

  - Configures how Jinja2 templates are processed for i18n

**messages.pot**

- **Purpose:** Translation template file (Portable Object Template)

- **Contents:**

  - All extracted strings from source code and templates

  - Source references for each translatable string

  - Metadata about the translation project

- **Usage:**

  - Base file for creating language-specific .po files

  - Updated when new strings are added to the application

**translations/** Directory
-  **Purpose:** Houses all multilingual resources

- **Structure:**

```
translations/
└── en/                            # English language directory
     └── LC_MESSAGES/              # Standard locale message directory
          ├── messages.mo          # Compiled translation file
          └── messages.po          # Source translation file
```

- **Files:**

  - `messages.po`: Human-editable translation file containing source strings and their translations

  - `messages.mo`: Binary-compiled version used by the application at runtime

### 4. Resource Directories
**static/**

- **Purpose:** Storage for all static assets

- **Contents:**

  - CSS files for styling (e.g., main.css, forms.css)

  - Images (logos, diagrams, screenshots)

  - Dataset files available for download

- **Key Features:**

  - Served directly by Flask's static file handler

  - Organized into subdirectories (css/, js/, images/, datasets/)

**templates/**

- **Purpose:** Contains all Jinja2 HTML templates

- **Structure:**

  - Base template (base.html) for common layout

  - Page-specific templates (leaderboard.html, submit.html, results.html)

  - Partial templates for reusable components

- **Key Features:**

  - Implements Jinja2 template inheritance

  - Contains dynamic content placeholders

  - Integrates with Flask-Babel for translated content

**old_proj/**

- **Purpose:** the basic and brief introduction of this benchmark suite. 

- **Contents:**

  - the basic and brief introduction of this benchmark suite. 

### 5. Configuration and Dependency Files
**requirements.txt**

- **Purpose:** Lists all Python dependencies

- **Contents:**

  - Flask and related extensions (Flask-Babel, Flask-WTF)

  - Data processing libraries (pandas, numpy)

  - CSV/JSON handling libraries

  - Deployment dependencies

- **Usage:**

  - Used with `pip install -r requirements.txt` to set up environment

  - Ensures consistent dependencies across deployments
