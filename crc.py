def crc8(data):
  poly = 0x7
  crc = 0x00
  data += '0' * 8

  for b in data:
    crc <<= 1
    crc |= int(b)
    if crc & 0x100:
      crc ^= poly

  return crc & 0xFF

def generate_crc8_table():
    poly=0x7
    table = []
    for byte in range(256):
        crc = byte
        for _ in range(8):
          crc <<= 1
          if crc & 0x100:
            crc ^= poly
        table.append(crc & 0xFF)
    return table

def crc8_with_table(data, table):
    crc = 0x00
    data += '0' * (8 - len(data) % 8 if len(data) % 8 else 0)
    
    for i in range(0, len(data), 8):
        byte = int(data[i:i + 8], 2)
        crc = table[crc ^ byte]
    return crc

def mirror_bits(value, num_bits):
    mirrored = 0
    for i in range(num_bits):
        mirrored |= ((value >> i) & 1) << (num_bits - 1 - i)
    return mirrored
  
def generate_mirrored_crc8_table():
    poly = mirror_bits(0x7, 8)
    table = []
    for byte in range(256):
        crc = mirror_bits(byte, 8)
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
        table.append(mirror_bits(crc, 8))
    return table

def crc8_table_mirrored(data, table):
    crc = 0x00
    data += '0' * (8 - len(data) % 8 if len(data) % 8 else 0)
    
    for i in range(0, len(data), 8):
        byte = int(data[i:i + 8], 2)
        crc = table[(crc ^ byte) & 0xFF]
    return crc