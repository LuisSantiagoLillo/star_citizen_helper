#!/.venv/bin/python3

from flask import Flask, render_template_string, request, jsonify
import keyboard  # Biblioteca para simular eventos de teclado

# Crear la instancia del servidor Flask
app = Flask(__name__)

# Página HTML que contiene el botón
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Futuristic Interface</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* Global Styles */
        body {
            margin: 0;
            padding: 0;
            font-family: 'Orbitron', sans-serif;
            background: #0a0f14;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: flex-start; /* Cambiado de center a flex-start */
            min-height: 100vh;
            overflow-y: auto; /* Cambiado de hidden a auto */
        }

        .interface {
            width: 90%;
            max-width: 1200px;
            background: #0d141a;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 255, 255, 0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            min-height: 100vh; /* Asegura que el contenido ocupe al menos la altura de la pantalla */
        }

        /* Tabs */
        .tabs {
            display: flex;
            justify-content: space-between;
            background: #121b23;
            border-bottom: 1px solid #1e2932;
            padding: 10px 0;
        }

        .tab {
            flex: 1;
            text-align: center;
            padding: 15px 20px;
            cursor: pointer;
            color: #ffffff;
            text-transform: uppercase;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .tab:hover,
        .tab.active {
            background: #1a2a38;
            color: #00eaff;
            box-shadow: inset 0 -4px 0 0 #00eaff;
        }

        /* Tab Content */
        .tab-content {
            display: none;
            flex: 1;
            padding: 20px;
            background: #0d141a;
        }

        .tab-content.active {
            display: block;
        }

        /* Panel Styles */
        .panel {
            display: grid;
            gap: 20px;
        }

        /* Core Interface */
        .panel-core {
            display: grid;
            grid-template-columns: repeat(2, 1fr); /* 2 columns */
            gap: 20px;
        }

        .section {
            background: #121f27;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #00eaff;
            box-shadow: 0 0 10px rgba(0, 255, 255, 0.1);
        }

        .section h2 {
            margin: 0 0 10px 0;
            font-size: 1.2rem;
            color: #00eaff;
        }

        /* Shields / Power */
        .panel-shields {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .ship-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
            align-items: center;
        }

        .ship-image {
            width: 100%;
            max-width: 300px;
            aspect-ratio: 16 / 9;
            background: #1e2b38;
            border: 1px solid #00eaff;
            border-radius: 10px;
            position: relative;
        }

        .ship-controls {
            display: flex;
            justify-content: space-between;
            gap: 10px;
        }

        .energy-controls {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        /* Communications */
        .panel-communications {
            display: grid;
            grid-template-columns: 1.5fr 1fr;
            gap: 20px;
        }

        .radar {
            position: relative;
            width: 100%;
            max-width: 300px;
            aspect-ratio: 1 / 1;
            background: radial-gradient(circle, rgba(0, 234, 255, 0.1), transparent);
            border: 2px solid #00eaff;
            border-radius: 50%;
            overflow: hidden;
        }

        .radar::before {
            content: "";
            position: absolute;
            top: 50%;
            left: 50%;
            width: 4px;
            height: 4px;
            background: #00eaff;
            border-radius: 50%;
            transform: translate(-50%, -50%);
        }

        .radar .target {
            position: absolute;
            width: 10px;
            height: 10px;
            background: #ff0055;
            border: 1px solid #ffffff;
            border-radius: 50%;
            animation: blink 1.5s infinite;
        }

        @keyframes blink {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.5;
            }
        }

        /* Buttons */
        .button {
            background: #121f27;
            color: #00eaff;
            padding: 15px;
            text-align: center;
            border-radius: 15px;
            border: 1px solid #00eaff;
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: bold;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            text-transform: uppercase;
            margin: 2px;
        }

        .button:hover {
            transform: scale(1.1);
            box-shadow: 0 0 10px #00eaff;
        }

        /* Media Queries */
        @media (max-width: 768px) {
            .panel-core, .panel-shields, .panel-communications {
                grid-template-columns: 1fr; /* Single column */
            }

            .tabs {
                flex-direction: column;
                align-items: stretch;
            }

            .tab {
                padding: 12px;
                font-size: 0.9rem;
            }

            .ship-controls {
                flex-direction: column;
            }

            .energy-controls {
                flex-direction: row;
                justify-content: space-between;
            }
        }

        @media (max-width: 480px) {
            .panel-core, .panel-shields, .panel-communications {
                padding: 10px; /* Reduce padding */
            }

            .section h2 {
                font-size: 1rem; /* Smaller font size */
            }

            .button {
                font-size: 0.8rem; /* Smaller buttons */
                padding: 10px; /* Smaller padding */
            }

            .radar {
                max-width: 200px; /* Smaller radar */
            }
        }
    </style>
</head>
<body>
        <div class="interface">
        <!-- Tabs -->
        <div class="tabs">
            <div class="tab active" onclick="switchTab('core')">Core Interface</div>
            <div class="tab" onclick="switchTab('shields')">Shield / Power</div>
            <div class="tab" onclick="switchTab('communications')">battle Mode</div>
        </div>

        <!-- Core Interface -->
        <div id="core" class="tab-content active">
            <div class="panel-core">
                <div class="section">
                    <h2>Doors</h2>
                    <button class="button">Open Doors</button>
                    <button class="button">Close Doors</button>
                </div>
                <div class="section">
                    <h2>Mobiglass</h2>
                    <button class="button">F1</button>
                    <button class="button">F2</button>
                    <button class="button">F3</button>
                    <button class="button">F4</button>
                    <button class="button">F5</button>
                    <button class="button">F6</button>
                    <button class="button">F7</button>
                    <button class="button">F8</button>
                    <button class="button">F9</button>
                    <button class="button">F10</button>
                    <button class="button">F11</button>
                    <button class="button">F12</button>
                </div>
                <div class="section">
                    <h2>Lights</h2>
                    <button class="button">On</button>
                    <button class="button">Off</button>
                </div>
                <div class="section">
                    <h2>Docking / Landing</h2>
                    <button class="button">Landing Gear - N</button>
                    <button class="button">Docking Camera - D</button>
                    <button class="button">Vtol - K</button>
                </div>
            </div>
        </div>

        <!-- Shields -->
        <div id="shields" class="tab-content">
            <div class="panel-shields">
                <div class="ship-container">
                    <div class="ship-image"></div>
                    <div class="ship-controls">
                        <button class="button">Top</button>
                        <button class="button">Left</button>
                        <button class="button">Right</button>
                        <button class="button">Bottom</button>
                    </div>
                </div>
                <div class="energy-controls">
                    <button class="button">Energy A</button>
                    <button class="button">Energy B</button>
                    <button class="button">Energy C</button>
                </div>
            </div>
        </div>

        <!-- Battle Mode -->
        <div id="communications" class="tab-content">
            <div class="panel-core">
                <div class="section">
                    <h2>Shields</h2>
                    <button class="button">Button</button>
                </div>
                <div class="section">
                    <h2>Countermeasures</h2>
                    <button class="button">Decoy Burst - H</button>
                    <button class="button">Noise - J</button>
                </div>
                <div class="section">
                    <h2>Power</h2>
                    <button class="button">Increase weapons - F5</button>
                    <button class="button">Increase engines - F6</button>
                    <button class="button">Increase shields - F7</button>
                    <button class="button">Increase ship power - F9</button>
                    <button class="button">Decrease ship power - F10</button>
                    <button class="button">Reset - F8</button>
                </div>
                <div class="section">
                    <h2>Targeting</h2>
                    <button class="button">Cycle assisted/standard and locked gimbal - G</button>
                    <button class="button">Cycle in view targets - T</button>
                    <button class="button">Auto targeting - T</button>
                    <button class="button">Cycle attackers - 4</button>
                    <button class="button">Cycle hostiles - 5</button>
                    <button class="button">Cycle fiendlies - 6</button>
                    <button class="button">Cycle all - 7</button>
                    <button class="button">Cycle sub target - 8</button>
                    <button class="button">Pinned selected target 1 - 1</button>
                    <button class="button">Pinned selected target 2 - 2</button>
                    <button class="button">Pinned selected target 3 - 3</button>
                    <button class="button">Remove all pins - 0</button>
                    
                </div>

            </div>
        </div>
    </div>
    
     <script>
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
            });
            document.getElementById(tabId).classList.add('active');
            document.querySelector(`.tab[onclick="switchTab('${tabId}')"]`).classList.add('active');
        }

        // Función de simulación de teclas
        function sendKeyPress(key) {
            fetch('/simulate_key', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ key: key })
            })
            .then(response => response.json())
            .then(data => alert(data.message))
            .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/simulate_key', methods=['POST'])
def simulate_key():
    data = request.get_json()
    key = data.get('key', '')

    if key:
        try:
            keyboard.press_and_release(key)
            # return jsonify({"message": f"Tecla '{key}' simulada con éxito."})
        except Exception as e:
            return jsonify({"message": f"Error al simular la tecla: {e}"}), 500
    else:
        return jsonify({"message": "No se proporcionó ninguna tecla."}), 400

if __name__ == '__main__':
    # Hacer que el servidor sea accesible desde la red local
    app.run(host='0.0.0.0', port=5000)