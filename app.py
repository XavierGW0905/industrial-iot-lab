
devices = [
    {"device_id": "DEV001", "location": "Plant A", "temperature": 35, "status": "Online"},
    {"device_id": "DEV002", "location": "Plant A", "temperature": 85, "status": "Online"},
    {"device_id": "DEV003", "location": "Plant B", "temperature": 42, "status": "Offline"}
]


def display_devices():
    print("\n===== INDUSTRIAL IOT MONITOR =====")

    for device in devices:
        print(
            f"{device['device_id']} | "
            f"{device['location']} | "
            f"{device['temperature']}°C | "
            f"{device['status']}"
        )


def check_alerts():
    print("\n===== DEVICE ALERTS =====")

    for device in devices:
        if device["temperature"] > 70:
            print(f"HIGH TEMPERATURE: {device['device_id']}")

        if device["status"] == "Offline":
            print(f"DEVICE OFFLINE: {device['device_id']}")


def count_devices():
    print(f"\nTotal devices monitored: {len(devices)}")


if __name__ == "__main__":
    display_devices()
    check_alerts()
    count_devices()
