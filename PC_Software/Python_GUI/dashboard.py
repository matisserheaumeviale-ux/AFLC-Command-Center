from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QTextEdit, QGroupBox
)

from serial_manager import SerialManager
import protocol


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.serial = SerialManager()

        self.setWindowTitle("AFLC Command Center")
        self.resize(850, 550)

        self.port_box = QComboBox()
        self.refresh_button = QPushButton("Refresh")
        self.connect_button = QPushButton("Connect")

        self.status_label = QLabel("Master: Offline")
        self.firmware_label = QLabel("Firmware: Unknown")

        self.ping_button = QPushButton("Ping")
        self.status_button = QPushButton("Status")
        self.id_button = QPushButton("ID")
        self.safe_button = QPushButton("PIC Safe")

        self.logs = QTextEdit()
        self.logs.setReadOnly(True)

        self.build_ui()
        self.bind_events()
        self.refresh_ports()

    def build_ui(self):
        root = QWidget()
        layout = QVBoxLayout(root)

        connection_box = QGroupBox("Connection")
        connection_layout = QHBoxLayout(connection_box)
        connection_layout.addWidget(QLabel("Port:"))
        connection_layout.addWidget(self.port_box)
        connection_layout.addWidget(self.refresh_button)
        connection_layout.addWidget(self.connect_button)

        master_box = QGroupBox("STM32 Master")
        master_layout = QVBoxLayout(master_box)
        master_layout.addWidget(self.status_label)
        master_layout.addWidget(self.firmware_label)

        command_box = QGroupBox("Commands")
        command_layout = QHBoxLayout(command_box)
        command_layout.addWidget(self.ping_button)
        command_layout.addWidget(self.status_button)
        command_layout.addWidget(self.id_button)
        command_layout.addWidget(self.safe_button)

        log_box = QGroupBox("Logs")
        log_layout = QVBoxLayout(log_box)
        log_layout.addWidget(self.logs)

        layout.addWidget(connection_box)
        layout.addWidget(master_box)
        layout.addWidget(command_box)
        layout.addWidget(log_box)

        self.setCentralWidget(root)

    def bind_events(self):
        self.refresh_button.clicked.connect(self.refresh_ports)
        self.connect_button.clicked.connect(self.connect_serial)

        self.ping_button.clicked.connect(lambda: self.send(protocol.build_ping()))
        self.status_button.clicked.connect(lambda: self.send(protocol.build_status()))
        self.id_button.clicked.connect(lambda: self.send(protocol.build_id()))
        self.safe_button.clicked.connect(lambda: self.send(protocol.build_pic_safe()))

    def refresh_ports(self):
        self.port_box.clear()
        self.port_box.addItems(self.serial.list_ports())

    def connect_serial(self):
        port = self.port_box.currentText()

        if not port:
            self.log("No port selected")
            return

        try:
            self.serial.connect(port)
            self.status_label.setText("Master: Connected")
            self.log(f"Connected to {port}")
        except Exception as e:
            self.log(f"ERROR: {e}")

    def send(self, message):
        try:
            self.log(f"TX: {message}")
            response = self.serial.send_command(message)
            self.log(f"RX: {response}")

            if response == "#PONG;":
                self.status_label.setText("Master: Online")

            if response.startswith("#ID:"):
                self.firmware_label.setText(f"Firmware: {response}")

        except Exception as e:
            self.log(f"ERROR: {e}")

    def log(self, text):
        self.logs.append(text)