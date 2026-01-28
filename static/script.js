function classifyWhitespaces(text) {
    const container = document.createElement('span');
    let normalText = [];

    for (let i = 0; i < text.length; i++) {
        const char = text[i];

        if ([' ', '\t', '\n'].includes(char)) {
            // Flush accumulated normal text
            if (normalText.length > 0) {
                container.appendChild(document.createTextNode(normalText.join('')));
                normalText = [];
            }

            // Create span for whitespace character
            const ws = document.createElement('span');

            switch (char) {
                case ' ':
                    ws.classList.add('ws_space');
                    ws.textContent = ' ';
                    container.appendChild(ws);
                    break;
                case '\t':
                    ws.classList.add('ws_tab');
                    ws.textContent = '\t';
                    container.appendChild(ws);
                    break;
                case '\n':
                    ws.classList.add('ws_newline');
                    ws.textContent = ' ';
                    container.appendChild(ws);
                    // Also add actual newline for proper line breaks
                    normalText.push('\n');
                    break;
            }
        } else {
            normalText.push(char);
        }
    }

    // Flush remaining normal text
    if (normalText.length > 0) {
        container.appendChild(document.createTextNode(normalText.join('')));
    }

    return container;
}

function toggleWhitespace() {
    const showWs = document.getElementById('showWhitespace').checked;
    const wsElements = document.querySelectorAll('.ws_space, .ws_tab, .ws_newline');

    if (showWs) {
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

        if (d.error) {
            out.textContent = 'ERROR: ' + d.error;
            out.className = 'output error';
        } else {
            const processedOutput = classifyWhitespaces(d.output);
            out.className = 'output';
            out.innerHTML = '';
            out.appendChild(processedOutput);

            // Apply whitespace visibility if checkbox is checked
            toggleWhitespace();
        }
    });
}
