from enum import Enum, unique
import struct 


@unique
class HCIPackageType(Enum):
    """docstring for HCIPackageType"""
    Command = 0x01
    ACL = 0x02
    Sync = 0x03
    Event = 0x04


class HCIGenericCommand(object):
    """docstring for HCICommand"""
    def __init__(self):
        super(HCIGenericCommand, self).__init__()
        self.indicator = HCIPackageType.Command.value
        self.OGF = 0x00
        self.OCF = 0x0000
        self.param_total_len = 0x00
        self.params = bytearray([100])

    def pack(self):
        arr = bytearray([self.indicator])

        [arr.append(i) for i in struct.pack('<H', self.OGF << 10|self.OCF)]
        arr.append(self.param_total_len)
        if self.param_total_len is not 0:
            [arr.append(i) for i in self.params]
        print 'HCI Command:', arr
        return arr


class HCIResetCommand(HCIGenericCommand):
    """docstring for HCIResetCommand"""
    def __init__(self):
        super(HCIResetCommand, self).__init__()
        self.OGF = 0x03
        self.OCF = 0x0003
        self.param_total_len = 0x00

# print HCIResetCommand().pack()
