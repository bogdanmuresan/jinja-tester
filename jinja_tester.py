from flask import Flask, request, jsonify, render_template
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

@app.route('/')
def index():
    mode = "(with Ansible Filters)" if ANSIBLE_AVAILABLE else ""
    return render_template('index.html', mode=mode)

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


