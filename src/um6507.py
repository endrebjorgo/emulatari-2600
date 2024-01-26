from enum import IntEnum

class StatusFlag(IntEnum):
    C = 1 << 0  # Carry
    Z = 1 << 1  # Zero
    I = 1 << 2  # IRQ Disable
    D = 1 << 3  # Decimal Mode
    B = 1 << 4  # BRK Command
    N = 1 << 6  # Overflow
    V = 1 << 7  # Negative


class UM6507:
    def __init__(self):
        """Registers"""
        self.a = 0b00000000         # Accumulator
        self.y = 0b00000000         # y-register
        self.x = 0b00000000         # x-register
        self.pch = 0b00000000       # Program counter high register
        self.pcl = 0b00000000       # Program counter low register
        self.sp = 0b00000000        # Stack pointer
        self.status = 0b00000000    # Status register

        """Buses"""
        self.addr = 0b0000000000000000  # Address bus
        self.data = 0b00000000          # Data bus

        self.ram = [0] * 1024 * 64 # 64KiB RAM

        self.cycles = 0

    """Helper functions"""
    def get_status_flag(self, flag):
        return bool(flag & self.status)

    def set_status_flag(self, flag, value):
        if not isinstance(flag, StatusFlag):
            raise ValueError("Value argument must be of type StatusFlag")

        if not isinstance(value, bool):
            raise ValueError("Value argument must be of type bool")

        if flag ^ self.status:
            self.status += flag * value
        
    """External signals"""
    def clock(self):
        """Clock Signal"""
        pass

    def reset(self):
        """Reset Signal"""
        pass

    def irq(self):
        """Interrupt request"""
        pass

    def nmi(self): 
        """Non-maskable interrupt"""
        pass

    def ADC(self):
        pass

    def AND(self):
        pass

    def ASL(self):
        pass

    def BCC(self):
        pass

    def ACD(self):
        pass

