import MCP230XX

mcp = MCP230XX.MCP230XX('MCP23017', 0x20, '16bit')

def setPinMode(pin, mode):
    print('> Set pin %d to %s mode'%(pin, mode))
    mcp.set_mode(pin, mode, pullUp='disable')
    
def setPinOutput(pin, value):
    print('> Setting pin %d output to %d'%(pin, value))
    mcp.output(pin, value)

def readPin(pin):
    print('> Reading pin %d'%pin)
    val = mcp.input(pin)
    print('    read %d'%val)

def setAllInput():
    print('> Setting all pins to input mode')
    for i in range(0, 16):
        mcp.set_mode(i, 'input', pullUp='disable')

def readAllInput():
    print('> Setting all pins to input mode')
    for i in range(0, 16):
        readPin(i)


def test():
    setPinMode(0, 'output')
    setPinMode(1, 'output')
    setPinMode(2, 'input')

    setPinOutput(0, 1)
    setPinOutput(1, 0)
    readPin(2)
    
    setPinMode(15, 'output')
    setPinMode(14, 'output')
    setPinMode(13, 'input')

    setPinOutput(15, 1)
    setPinOutput(14, 0)
    readPin(13)
    


if __name__ == "__main__":
    print('Starting!')
    #test()
    setAllInput()
    readAllInput()
    
    print('Done!')
