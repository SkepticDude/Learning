# String / list Rotation
def rightShiftRotate(myStr, n):
    return myStr[-n:] + myStr[:-n]

def leftShiftRotate(myStr, n):
    return myStr[n:] + myStr[:n]

# binary input
int("10001",2)              # integer output => 17
oct(int("10001",2))         # octal output => 0o21
hex(int("10001",2))         # Hex output => 0x11

# binary input binary output 
bin(int("10001",2))         # 0b10001
bin(int("10001",2))[2:]     # 10001

# hex input
int("11",16)                # integer output => 17
bin(int("11",16))           # binary output => 0b10001
oct(int("11",16))           # octal output => 0o21





