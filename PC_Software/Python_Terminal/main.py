from serial_link import SerialLink
from commands import build_command


def print_help():
    print("")
    print("AFLC Command Center Terminal")
    print("")
    print("Commands:")
    print("  ports")
    print("  connect COM3")
    print("  ping")
    print("  status")
    print("  safe")
    print("  rpm")
    print("  fan1 pwm 65")
    print("  mode auto")
    print("  mode manual")
    print("  exit")
    print("")


def main():
    link = SerialLink()

    print_help()

    while True:
        try:
            user_input = input("AFLC> ").strip()

            if not user_input:
                continue

            if user_input.lower() == "exit":
                link.disconnect()
                break

            if user_input.lower() == "help":
                print_help()
                continue

            if user_input.lower() == "ports":
                ports = link.list_ports()

                if not ports:
                    print("No serial ports found")
                else:
                    for port in ports:
                        print(port)

                continue

            if user_input.lower().startswith("connect "):
                port = user_input.split()[1]
                ok = link.connect(port)

                if ok:
                    print(f"Connected to {port}")
                else:
                    print("Connection failed")

                continue

            protocol_message = build_command(user_input)

            print(f"TX: {protocol_message}")
            link.send_line(protocol_message)

            response = link.read_line()
            print(f"RX: {response}")

        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()