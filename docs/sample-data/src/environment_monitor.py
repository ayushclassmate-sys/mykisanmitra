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
    for reading in read_environment_data():
        print(reading)
