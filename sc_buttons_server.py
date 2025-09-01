#!/.venv/bin/python3

from flask import Flask, render_template, request, jsonify
import keyboard  # Biblioteca para simular eventos de teclado

# Crear la instancia del servidor Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza el archivo HTML en templates/

# Ruta para simular la tecla
@app.route('/simulate_key', methods=['POST'])
def simulate_key():
    data = request.get_json()
    key = data.get('key', '')

    if key:
        try:
            keyboard.press_and_release(key)
            return jsonify({"message": f"Tecla '{key}' simulada con éxito."})
        except Exception as e:
            return jsonify({"message": f"Error al simular la tecla: {e}"}), 500
    else:
        return jsonify({"message": "No se proporcionó ninguna tecla."}), 400

if __name__ == '__main__':
    # Hacer que el servidor sea accesible desde la red local
    app.run(host='0.0.0.0', port=5000)
