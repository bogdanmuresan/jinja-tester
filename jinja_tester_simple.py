from flask import Flask, request, jsonify
import jinja2
import json
import yaml

# Try to import Ansible filters
ANSIBLE_AVAILABLE = False
try:
    from ansible.plugins.filter.core import FilterModule as AnsibleCoreFilters
    ANSIBLE_AVAILABLE = True
    print("✅ Ansible filters loaded successfully!")
except ImportError:
    print("⚠️  Standard Jinja2 only (install ansible for more filters)")

def get_ansible_filters():
    if not ANSIBLE_AVAILABLE:
        return {}
    filters = {}
    core_filters = AnsibleCoreFilters()
    filters.update(core_filters.filters())
    return filters

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html>
<head>
    <title>Jinja2 Tester</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        <h1>Jinja2 Template Tester {MODE}</h1>
        <div class="grid">
            <div>
                <h3>Template:</h3>
                <textarea id="template">Hello {{ name }}!
{% for item in items %}
  - {{ item }}
{% endfor %}</textarea>
            </div>
            <div>
                <h3>Data (YAML):</h3>
                <textarea id="data">name: World
items:
  - a
  - b
  - c</textarea>
            </div>
        </div>
        <p>
            <button onclick="render()">Render</button>
            <label><input type="checkbox" id="showWhitespace" onchange="toggleWhitespace()"> Show Whitespace</label>
        </p>
        <h3>Output:</h3>
        <div id="output" class="output">Click render...</div>
        <div class="version">v0.0.3</div>
    </div>
    <script src="/static/script.js"></script>
</body>
</html>
"""

@app.route('/')
def index():
    mode = "(with Ansible)" if ANSIBLE_AVAILABLE else ""
    return HTML.replace("{MODE}", mode)

@app.route('/render', methods=['POST'])
def render():
    try:
        data = request.get_json()
        template_str = data.get('template', '')
        context_str = data.get('data', '{}')

        try:
            context = yaml.safe_load(context_str) or {}
        except yaml.YAMLError as e:
            return jsonify({'error': f'Invalid YAML: {str(e)}'})

        env = jinja2.Environment()
        if ANSIBLE_AVAILABLE:
            env.filters.update(get_ansible_filters())

        try:
            template = env.from_string(template_str)
            output = template.render(context)
            return jsonify({'output': output})
        except Exception as e:
            return jsonify({'error': str(e)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    print("📍 Open: http://localhost:5002")
    app.run(debug=False, host='0.0.0.0', port=5002)


