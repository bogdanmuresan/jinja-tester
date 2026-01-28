# Jinja2 Template Tester

A web-based tool for testing Jinja2 templates with YAML data input. Includes support for Ansible filters, whitespace visualization, and a clean yellow-themed interface with a friendly silkie chicken mascot.

🐔 **Live Demo:** https://jinja-tester.fly.dev/

## Features

- Live Jinja2 template rendering
- YAML data input with complex data structures (dictionaries, lists)
- Full Ansible filters support
- Whitespace visualization toggle
- Clean, accessible split-pane interface
- Yellow-themed design with silkie chicken branding
- SEO optimized with comprehensive meta tags
- Responsive layout

## Requirements

- Python 3.13+
- Flask
- PyYAML
- Ansible (for filter support)

## Running Locally

### 1. Install Dependencies

```bash
pip install flask pyyaml ansible
```

### 2. Run the Application

```bash
python jinja_tester.py
```

### 3. Open in Browser

Navigate to: http://localhost:5002

## Running with Docker

### Build the Image

```bash
docker build -t jinja-tester .
```

### Run the Container

```bash
docker run -p 5002:5002 jinja-tester
```

Then open http://localhost:5002 in your browser.

## Deploying to Fly.io

This project is configured for deployment to Fly.io:

```bash
fly deploy
```

The app is configured to:
- Run in the `fra` region
- Use 256MB memory
- Auto-stop when idle
- Auto-start on request

## Usage

1. Enter your Jinja2 template in the left panel
2. Enter your data in YAML format in the right panel
3. Click "Render" to see the output
4. Toggle "Show Whitespace" to visualize spaces, tabs, and newlines

## Project Structure

```
jinja_tester/
├── jinja_tester.py          # Main Flask application
├── templates/
│   └── index.html           # Main HTML template
├── static/
│   ├── style.css            # Styling with yellow theme
│   ├── app.js              # Whitespace visualization
│   └── favicon.svg         # Chicken favicon
├── Dockerfile              # Container configuration
├── fly.toml               # Fly.io deployment config
└── README.md
```

## Version

Current version: 1.0.0
