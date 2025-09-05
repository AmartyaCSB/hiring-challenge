security_code = None
max_duration = -1

with open("space_missions.log", "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 8:
            continue

        date, mission_id, destination, status, crew, duration, success_rate, code = parts

        if destination == "Mars" and status == "Completed":
            try:
                duration_days = int(duration)
            except ValueError:
                continue

            if duration_days > max_duration:
                max_duration = duration_days
                security_code = code

print(security_code)
