function classifyWhitespaces(text) {
    const container = document.createElement('span');
    let normalText = [];

    for (let i = 0; i < text.length; i++) {
        const char = text[i];

        if ([' ', '\t', '\n'].includes(char)) {
            // Flush normal text
            if (normalText.length > 0) {
                container.appendChild(document.createTextNode(normalText.join('')));
                normalText = [];
            }

            // Create span for whitespace
            const span = document.createElement('span');

            switch (char) {
                case ' ':
                    span.className = 'ws_space';
                    span.textContent = ' ';
                    break;
                case '\t':
                    span.className = 'ws_tab';
                    span.textContent = '\t';
                    break;
                case '\n':
                    span.className = 'ws_newline';
                    span.textContent = '\n';
                    break;
            }

            container.appendChild(span);
        } else {
            normalText.push(char);
        }
    }

    // Flush remaining text
    if (normalText.length > 0) {
        container.appendChild(document.createTextNode(normalText.join('')));
    }

    return container;
}

function toggleWhitespaces() {
    const showWhitespace = document.getElementById('showWhitespace').checked;
    const wsElements = document.querySelectorAll('.ws_space, .ws_tab, .ws_newline');

    if (showWhitespace) {
        wsElements.forEach(el => el.classList.add('ws_vis'));
    } else {
        wsElements.forEach(el => el.classList.remove('ws_vis'));
    }
}

function render() {
    fetch('/render', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            template: document.getElementById('template').value,
            data: document.getElementById('data').value
        })
    })
    .then(r => r.json())
    .then(d => {
        const out = document.getElementById('output');
        out.innerHTML = '';

        if (d.error) {
            out.textContent = 'ERROR: ' + d.error;
            out.className = 'output error';
        } else {
            const renderedHtml = classifyWhitespaces(d.output);
            out.appendChild(renderedHtml);
            out.className = 'output';
            toggleWhitespaces();
        }
    });
}
