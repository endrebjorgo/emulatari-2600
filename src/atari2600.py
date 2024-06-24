from um6507 import UM6507

class Atari2600:
    def __init__(self):
        self.cpu = None
        self.ram = [0x00] * 128

    def read(addr):
        return self.ram[addr]

    def write(addr, data):
        self.ram[addr] = data
