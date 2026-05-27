import time
import serial
import serial.tools.list_ports


class SerialLink:
    def __init__(self):
        self.ser = None

    def list_ports(self):
        return [port.device for port in serial.tools.list_ports.comports()]

    def connect(self, port, baudrate=19200, timeout=1):
        self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        time.sleep(0.2)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        return self.ser.is_open

    def disconnect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()

    def is_connected(self):
        return self.ser is not None and self.ser.is_open

    def send_line(self, message):
        if not self.is_connected():
            raise RuntimeError("Serial port not connected")

        if not message.endswith(";"):
            message += ";"

        self.ser.reset_input_buffer()
        self.ser.write(message.encode("utf-8"))
        self.ser.flush()

    def read_line(self):
        if not self.is_connected():
            raise RuntimeError("Serial port not connected")

        data = self.ser.readline()
        return data.decode("utf-8", errors="replace").strip()