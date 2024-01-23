class UM6507:
    # Status Flags
    C = 1 << 0  # Carry
    Z = 1 << 1  # Zero
    I = 1 << 2  # IRQ Disable
    D = 1 << 3  # Decimal Mode
    B = 1 << 4  # BRK Command
    N = 1 << 6  # Overflow
    V = 1 << 7  # Negative

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
        
    """Signals"""
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

"""
    OPCODES
ADC Add Memory to Accumulator with Carry 
AND "AND" Memory with Accumulator
ASL Shift left One Bit (Memory or Accumulator)

BCC Branch on Carry Clear
BCS Branch on Carry Set
BEQ Branch on Result Zero
BIT Test Bits in Memory with Accumulator 
BMI Branch on Result Minus
BNE Branch on Result not Zero
BPL Branch on Result Plus
BNK Force Break
BVC Branch on Overflow Clear
BVS Branch on Overflow Set

CLC Clear Carry Flag
CLD Clear Decimal Mode
CLI Clear Interrupt Disable Bit
CLV Clear Overflow Flag
CMP Compare Memory and Accumulator
CPX Compare Memory and Index X 
CPY Compare Memory and Index Y

DEC Decrement Memory by One
DEX Decrement Index X by One
DEY Decrement Index Y by One

EOR "Exclusive-or" Memory with Accumulator

INC Increment Memory by One 
INX Increment Index X by One 
INY Increment Index Y by One

JMP Jump to New Location
JSR Jump to New Location Saving Return Address

LDA Load Accumulator with Memory
LDX Load Index X with Memory
LDY Load Index Y with Memory
LSR Shift One Bit Right (Memory or Accumulator)

NOP No Operation

ORA "OR" Memory with Accumulator

PHA Push Accumulator on Stack
PHP Push Processor Status on Stack
PLA Pull Accumulator from Stack
PLP Pull Processor Status from Stack

ROL Rotate One Bit Left (Memory or Accumlator)
ROR Rotate One Bit Right (Memory or Accumulator)
RTI Return from Interrupt
RTS Return from Subroutine

SBC Subtract Memory from Accumulator with Borrow
SEC Set Carry Flag
SED Set Decimal Mode
SEI Set Interrupt Disable Status
STA Store Accumulator in Memory 
STX Store Index X in Memory
STY Store Index Y in Memory

TAX Transfer Accumulator to Index X
TAY Transfer Accumulator to Index Y
TSX Transfer Stack Pointer to Index X
TXA Transfer Index X to Accumulator
TXS Transfer Index X to Stack Pointer
TYA Transfer Index Y to Accumulator

    ADDRESSING MODES
ACC Accumulator Addressing
IMM Immediate Addressing
ABS Absolute Addressing
ABX Absolute with X Offset
ABY Absolute with Y Offset
IMP Implied Addressing
REL Relative Addressing
ZP0 Zero Page Addressing
ZPX Zero Page with X Offset
ZPY Zero Page with Y Offset
XIN Indexed Indirect Addressing
INX Indirect Indexed Addressing
ABI Absolute Indirect Addressing
"""
