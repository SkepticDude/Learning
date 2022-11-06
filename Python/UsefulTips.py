# String / list Rotation
def rightShiftRotate(myStr, n):
    return myStr[-n:] + myStr[:-n]

def leftShiftRotate(myStr, n):
    return myStr[n:] + myStr[:n]

# Binary <==> Integer conversion
int("10001",2)              # 17
int("0b10001",2)            # 17
bin(17)                     # 0b10001
bin(17)[2:]                 # 10001

# Octal <==> Integer conversion
int("21", 8)                # 17
int("0o21", 8)              # 17
oct(17)                     # 0o21
oct(17)[2:]                 # 21

# Hex <==> Integer conversion
int("11", 16)               # 17
int("0x11", 16)             # 17
hex(17)                     # 0x11
hex(17)[2:]                 # 11




