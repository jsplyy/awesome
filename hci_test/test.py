ogf = 0x03
ocf = 0x03
# print (ogf<<10|ocf).to_bytes(length=2, byteorder='big')
import struct
print type(struct.pack('<H', ogf<<10|ocf))
# byte_a = bytearray()
# byte_a.append([100,102])
# byte_a.append(101)
# print byte_a
a = bytearray([100])
print [a.append(i) for i in (struct.pack('<H', ogf<<10|ocf))]
print a