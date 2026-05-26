def build_command(user_input):
    parts = user_input.strip().split()

    if not parts:
        return None

    cmd = parts[0].lower()

    if cmd == "ping":
        return "@PING?;"

    if cmd == "status":
        return "@STATUS?;"

    if cmd == "safe":
        return "@PIC:SAFE?;"

    if cmd == "rpm":
        return "@FAN1:RPM?;"

    if cmd == "fan1" and len(parts) == 3 and parts[1].lower() == "pwm":
        value = int(parts[2])

        if value < 0 or value > 100:
            raise ValueError("PWM must be between 0 and 100")

        return f"@FAN1:PWM:{value};"

    if cmd == "mode" and len(parts) == 2:
        mode = parts[1].upper()

        if mode not in ["AUTO", "MANUAL", "SAFE"]:
            raise ValueError("Mode must be AUTO, MANUAL, or SAFE")

        return f"@MODE:{mode};"

    raise ValueError("Unknown command")