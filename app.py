from flask import Flask, request, jsonify
from main import model
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in your Flask app

@app.route('/api/post_example', methods=['POST'])
def post_example():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Access the 'message' key from the JSON data
        message = data.get('message', 'Default Message')
        result = model(message)

        # Create a response
        response = {'status': 'success', 'message': f'Received message: {result}'}

        return jsonify(response)

    except Exception as e:
        # Handle exceptions
        return jsonify({'status': 'error', 'error_message': str(e)})

if __name__ == '__main__':
    # Run the Flask app on http://127.0.0.1:5000/
    app.run(debug=True)
