# IoT Dashboard

Welcome to the IoT Dashboard project! This web application provides a professional and clean dashboard to display IoT sensor data, specifically monitoring fuel and distance metrics. Initially designed with built-in testing capabilities, this project is ready to integrate with actual IoT sensors.

## Features

- **Real-time Data Visualization**: Displays sensor data in real-time using interactive charts.
- **Fuel and Distance Monitoring**: Separate charts for fuel and distance metrics.
- **Data Persistence**: Stores data locally in a JSON file.
- **Responsive Design**: Works seamlessly on both desktop and mobile devices.

## Preview

![image](https://github.com/Sowoul/IoT_Server/assets/93905595/73fd0500-e986-4d92-b3d4-868b611655cf)


## Getting Started

Follow these steps to get the IoT Dashboard up and running on your local machine.

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/iot-dashboard.git
    cd iot-dashboard
    ```

2. **Install required packages**:
    ```bash
    pip install flask
    ```

3. **Run the application**:
    ```bash
    python main.py
    ```

4. **Access the Dashboard**:
    Open your web browser and navigate to `http://127.0.0.1:8080`.

### Sample Data

Sample data is provided to get you started right away. You can find it in `store.json`

### Sending Data

You can use `curl` or a simple Python script to send data to the dashboard.

- **Using `curl`**:
    ```bash
    curl -X POST -d "data=50,120" http://127.0.0.1:8080/post
    ```

- **Using a Python Script**:
    ```python
    import requests

    url = 'http://127.0.0.1:8080/post'
    data = {
        'data': '50,120'  # Replace with your desired fuel and distance values
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Data sent successfully:', response.json())
    else:
        print('Failed to send data:', response.status_code)
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

