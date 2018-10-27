from serial import Serial
from enums import HCIResetCommand

hci_port = Serial('COM3', 115200)
hci_port.write(HCIResetCommand().pack())
print ' '.join(hex(ord(i)) for i in hci_port.read(7))