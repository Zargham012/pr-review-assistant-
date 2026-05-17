from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze a folder for missing docstrings and tests."""
    try:
        data = request.get_json()
        
        if not data or 'folder_path' not in data:
            return jsonify({
                'error': 'Missing folder_path in request body'
            }), 400
        
        folder_path = data['folder_path']
        
        # Validate folder path
        if not os.path.exists(folder_path):
            return jsonify({
                'error': f'Folder path does not exist: {folder_path}'
            }), 400
        
        # Run analyzer.py as a subprocess
        result = subprocess.run(
            ['python', 'analyzer.py', folder_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            return jsonify({
                'error': 'Analysis failed',
                'details': result.stderr
            }), 500
        
        # Parse the JSON output from analyzer.py
        try:
            analysis_result = json.loads(result.stdout)
            return jsonify(analysis_result), 200
        except json.JSONDecodeError:
            return jsonify({
                'error': 'Failed to parse analysis results',
                'output': result.stdout
            }), 500
            
    except subprocess.TimeoutExpired:
        return jsonify({
            'error': 'Analysis timed out after 30 seconds'
        }), 500
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'details': str(e)
        }), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'Smart PR Review Assistant'
    }), 200


if __name__ == '__main__':
    print("Starting Smart PR Review Assistant Server...")
    print("Server running on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)

# Made with Bob
