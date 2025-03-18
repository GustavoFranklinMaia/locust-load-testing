# Load Testing with Locust and Python

## 📌 Overview
This project is designed to perform **load and stress testing** on a web application using **Locust** and **Python**. The script simulates multiple login attempts by retrieving user credentials from a CSV file and records the success and failure of each attempt in separate log files.

By using this tool, you can analyze how your system behaves under different load conditions and identify potential bottlenecks before they impact real users.

## 🚀 Features
- Simulates multiple user logins using data from a CSV file.
- Logs successful and failed login attempts into separate CSV files.
- Provides insights into system performance under high-traffic conditions.
- Uses **Locust**, a powerful load-testing tool for Python.
- Helps in detecting authentication issues and system limitations.

## 📂 Project Structure
```
📁 project-folder
│── users.csv  # Input file containing user login credentials
│── successful_logins.csv  # Logs of successful login attempts
│── failed_logins.csv  # Logs of failed login attempts
│── locustfile.py  # Main script for load testing
│── README.md  # Documentation
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.x installed
- `pip` installed

### Install Required Dependencies
```bash
pip install locust
```

## 🏃‍♂️ Running the Load Test
1. **Prepare the CSV File**
   - Create a `users.csv` file with user credentials in the following format:
   ```csv
   email,password
   user1@example.com,password123
   user2@example.com,securePass456
   ```

2. **Run the Locust Test**
   ```bash
   locust -f locustfile.py --host=https://your-api-endpoint.com
   ```

3. **Access the Locust Web Interface**
   - Open your browser and go to: **http://localhost:8089**
   - Enter the number of users to simulate and the spawn rate, then start the test.

## 📝 Customization
### Change the API Endpoint
Update the following line in `locustfile.py` to match your login endpoint:
```python
response = self.client.post(
    "", # Add your login endpoint here
    json={
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
)
```

### Adjust Wait Time Between Requests
Modify the `wait_time` attribute to control how often users make requests:
```python
wait_time = between(1, 5)  # Users will wait between 1 to 5 seconds before making the next request
```

## 📊 Understanding Test Results
- **Successful login attempts** will be recorded in `successful_logins.csv`.
- **Failed login attempts**, along with error messages, will be stored in `failed_logins.csv`.
- The **Locust web interface** provides real-time metrics, including response times, request failures, and request per second.

## 🛠️ Troubleshooting
- **No users are executing tests?** Ensure that `users.csv` is correctly formatted.
- **Locust Web UI not loading?** Make sure Locust is running and check if another process is using port 8089.
- **API requests failing?** Double-check the login endpoint and API key (if required).

## 📌 Why Load Testing is Important?
Many **e-commerce platforms lose millions** due to unexpected website crashes during high-traffic events like Black Friday. Running **load and stress tests** ensures your application can handle peak loads and prevents revenue loss caused by downtime.

## 🔗 Additional Resources
- [Locust Documentation](https://docs.locust.io/en/stable/)
- [Python Official Site](https://www.python.org/)


