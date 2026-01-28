# Jinja2 Template Tester

A simple web-based tool for testing Jinja2 templates with YAML data input. Includes support for Ansible filters and whitespace visualization.

## Features

- Live Jinja2 template rendering
- YAML data input
- Ansible filters support (optional)
- Whitespace visualization toggle
- Clean, split-pane interface

## Requirements

- Python 3.8+
- Flask
- PyYAML
- Ansible (optional, for additional filters)

## Running Locally

### 1. Install Dependencies

```bash
pip install flask pyyaml ansible
```

Note: `ansible` is optional. The app will work without it but with fewer available filters.

### 2. Run the Application

```bash
python jinja_tester_simple.py
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

### Example

**Template:**
```jinja2
Hello {{ name }}!
{% for item in items %}
  - {{ item }}
{% endfor %}
```

**Data (YAML):**
```yaml
name: World
items:
  - a
  - b
  - c
```

**Output:**
```
Hello World!
  - a
  - b
  - c
```

## Version

Current version: 0.0.2
