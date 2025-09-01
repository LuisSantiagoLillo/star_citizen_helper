#!/.venv/bin/python3

from flask import Flask, render_template, request, jsonify
import keyboard  # Library to simulate keyboard events

# Create the Flask app instance
app = Flask(__name__)

# Root route
@app.route('/')
def index():
    return render_template('index.html')  # Renders the HTML file in templates/

# Route to simulate a key press
@app.route('/simulate_key', methods=['POST'])
def simulate_key():
    data = request.get_json()
    key = data.get('key', '')

    if key:
        try:
            keyboard.press_and_release(key)
            return jsonify({"message": f"Key '{key}' simulated successfully."})
        except Exception as e:
            return jsonify({"message": f"Error simulating key: {e}"}), 500
    else:
        return jsonify({"message": "No key was provided."}), 400

if __name__ == '__main__':
    # Make the server accessible from the local network
    app.run(host='0.0.0.0', port=5000)
