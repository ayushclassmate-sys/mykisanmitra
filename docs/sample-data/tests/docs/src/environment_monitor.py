import csv
from pathlib import Path

DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "sample-data"
    / "environment_readings.csv"
)


def validate_reading(temperature, humidity):
    """Check whether temperature and humidity values are valid."""
    if not -50 <= temperature <= 70:
        return False

    if not 0 <= humidity <= 100:
        return False

    return True


def read_environment_data(file_path=DATA_FILE):
    """Read and validate environmental readings from a CSV file."""
    readings = []

    with open(file_path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                temperature = float(row["temperature_c"])
                humidity = float(row["humidity_percent"])
            except (ValueError, KeyError):
                continue

            if validate_reading(temperature, humidity):
                readings.append({
                    "timestamp": row["timestamp"],
                    "temperature_c": temperature,
                    "humidity_percent": humidity,
                })

    return readings


if __name__ == "__main__":
    data = read_environment_data()

    if not data:
        print("No valid environmental readings found.")
    else:
        for reading in data:
            print(
                f'{reading["timestamp"]}: '
                f'{reading["temperature_c"]}°C, '
                f'{reading["humidity_percent"]}% humidity'
            )

**5.** Click **Commit changes** and confirm.

**Note:** This program processes sample CSV data; it does not connect directly to physical sensors.

When you're finished, reply **done**. I'll guide you through adding automated tests next.
