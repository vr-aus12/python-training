from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/status', methods=['GET'])
def get_status():
    data = {
        "service": "Python Course API",
        "status": "online",
        "version": "1.0"
    }
    return jsonify(data)

if __name__ == '__main__':
    # To run this, you would typically use:
    # app.run(debug=True)
    print("Flask app defined. Run with 'flask run' or 'python flask_api.py'")

# Expected Output (Client Request GET /api/v1/status):
# {
#     "service": "Python Course API",
#     "status": "online",
#     "version": "1.0"
# }
