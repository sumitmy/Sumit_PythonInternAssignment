from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('apps.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS apps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app_name TEXT NOT NULL,
        version TEXT NOT NULL,
        description TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

# Initialize database
init_db()

# API Endpoints
@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    app_name = data.get('app_name')
    version = data.get('version')
    description = data.get('description')

    if not app_name or not version or not description:
        return jsonify({'error': 'All fields are required!'}), 400

    conn = sqlite3.connect('apps.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO apps (app_name, version, description) VALUES (?, ?, ?)',
                   (app_name, version, description))
    conn.commit()
    conn.close()

    return jsonify({'message': 'App added successfully!'}), 201

@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    conn = sqlite3.connect('apps.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM apps WHERE id = ?', (id,))
    app = cursor.fetchone()
    conn.close()

    if app:
        return jsonify({'id': app[0], 'app_name': app[1], 'version': app[2], 'description': app[3]}), 200
    else:
        return jsonify({'error': 'App not found!'}), 404

@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    conn = sqlite3.connect('apps.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM apps WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    if cursor.rowcount:
        return jsonify({'message': 'App deleted successfully!'}), 200
    else:
        return jsonify({'error': 'App not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True)