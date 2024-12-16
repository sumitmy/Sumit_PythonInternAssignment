# Python Intern Assignment

## Submission Guidelines

Submit all required files in a single ZIP folder named:

```
Sumit_PythonInternAssignment.zip
```

## Folder Contents

The folder should include:

1. **Code Files**
   - `api.py`
   - `networking.py`
   - `virtual_android.py`

2. **README.md**: A consolidated instruction file for running each script.

---

## Instructions for Running Each Task

### Task 1: API Development (`api.py`)

#### Description
This script creates a Flask-based REST API that interacts with an SQLite database. It provides endpoints to add, retrieve, and delete app details.

#### Prerequisites
- Python 3.x installed.
- Flask installed in your environment (`pip install flask`).

#### How to Run
1. Navigate to the folder containing `api.py`:
   ```bash
   cd Sumit_PythonInternAssignment
   ```

2. Run the API server:
   ```bash
   python api.py
   ```

3. The server will start at `http://127.0.0.1:5000`.

#### API Endpoints

| Endpoint          | Method | Description                    | Example Payload                                                                 |
|-------------------|--------|--------------------------------|--------------------------------------------------------------------------------|
| `/add-app`        | POST   | Add a new app to the database. | `{ "app_name": "Calculator", "version": "1.0", "description": "A basic calculator app" }` |
| `/get-app/<id>`   | GET    | Retrieve app details by ID.    | None                                                                           |
| `/delete-app/<id>`| DELETE | Delete app details by ID.      | None                                                                           |

#### Example
- To test these endpoints, you can use `curl` or a tool like Postman.
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"app_name": "Calculator", "version": "1.0", "description": "A basic calculator app"}' http://127.0.0.1:5000/add-app
  ```

---

### Task 2: Networking Script (`networking.py`)

#### Description
This script sends mock data (device information) from a virtual Android system to the backend API created in Task 1. It uses HTTP POST requests to interact with the `add-app` endpoint.

#### Prerequisites
- Ensure the API server (`api.py`) is running at `http://127.0.0.1:5000`.
- Install the `requests` library if not already installed:
  ```bash
  pip install requests
  ```

#### How to Run
1. Navigate to the folder containing `networking.py`:
   ```bash
   cd Sumit_PythonInternAssignment
   ```

2. Run the script:
   ```bash
   python networking.py
   ```

3. Check the terminal for the response from the API server.

#### Output
- On success, the script logs:
  ```
  Data sent successfully: {"message": "App added successfully!"}
  ```
- On failure (e.g., if required fields are missing):
  ```
  Error sending data: {"error": "All fields are required!"}
  ```

---

### Task 3: Virtual Android System (`virtual_android.py`)

#### Description
This script simulates a virtual Android system and sends mock device data (like `device_id` and `system_info`) to the backend API server. It also demonstrates data transmission to a server endpoint.

#### Prerequisites
- Ensure the API server (`api.py`) is running at `http://127.0.0.1:5000`.

#### How to Run
1. Navigate to the folder containing `virtual_android.py`:
   ```bash
   cd Sumit_PythonInternAssignment
   ```

2. Run the script:
   ```bash
   python virtual_android.py
   ```

3. Check the terminal for the response from the API server.

#### Output
- On success:
  ```
  Virtual Android device successfully connected. Server Response: {"message": "App added successfully!"}
  ```
- On failure (e.g., if the server is not running):
  ```
  Error connecting to server: [Error Details]
  ```

---

## Code Documentation and Best Practices

### Code Structure
- Each script is modular and performs its designated task independently.
- Functions and modules are logically organized.

### Error Handling
- Proper error messages are logged for invalid API requests or connection issues.

### API Usage
- The scripts use `requests` for making HTTP calls.
- Example payloads are provided in the API section.

### Testing
- Scripts are tested for compatibility with Python 3.x.
- Ensure the backend server (`api.py`) is running before testing dependent scripts (`networking.py` and `virtual_android.py`).
