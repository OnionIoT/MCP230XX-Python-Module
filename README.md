# MCP230XX-Python-Module
Python module to use the MCP23017 or MCP23008 GPIO expander chip and the Onion Omega2. This module
supports using the interrupt capabilities on the MCP230XX chips (no module to support this though)

## Dependencies
 
This requires the Onion I2C module for the i2c connection. 

```
opkg update
opkg install python3-light python3-onion-i2c
```

Requires a GPIO module to use the interrupt capabilities **Not tested with the Omega2**.

Included at the end of the module are some example uses of the module

## Connection to the MCP230XX from the Omega2 are as follows:

- SCL to MCP SCL
- SDA to MCP SDA
- 3.3V to MCP VDD
- Gnd to MCP Vss

With the above A0-A2 connections the i2c address is 0x20

For the MCP23008 the MCP GPIOA 0-7 are IO 0-7 in this module
For the MCP23017 the MCP GPIOA 0-7 are IO 0-7 and the MCP GPIOB 0-7 are IO 8-15 in this module

## Current functions include:

- `interrupt_options(outputType = 'activehigh', bankControl = 'separate')``
- `set_register_addressing(regScheme='8bit')`
- `set_mode(pin, mode, pullUp='disable')`
- `invert_input(pin, invert = False)`
- `output(pin, value)`
- `input(pin)`
- `add_interrupt(pin, callbackFunctLow='empty', callbackFunctHigh='empty')`
- `remove_interrupt(pin)`
- `register_reset()`

## Example uses

To initialize the chip

```
MCP = MCP230XX('MCP23017', i2cAddress, '16bit')
```

To set up an input and output

```
MCP.set_mode(0, 'output')  # set IO 0 to an output
MCP.set_mode(1, 'input')   # set IO 1 to an input
MCP.set_mode(10, 'input', 'enable')  # set IO 10 to an input with the pullup enabled
```

To set an output:

```
MCP.output(0,1)  # set IO 0 high
MCP.output(0,0)  # set IO 0 low
```

To read an input:

```
MCP.input(1)  # reads current value on IO 1, return 0 for low and 1 for high
```

To set interrupt options

```
MCP.interrupt_options(outputType = 'activehigh', bankControl = 'separate')
```

- the interrupt pins can be set as either activehigh, activelow or opendrain
- for the MCP23017 the interrupts for IO 0-7 and IO 8-15 can be trigger INTA and INTB respectively
with bankControl = 'seperate' or and an intterupt on any of the IO (0-15) can be sent to both INTA and INTB
with bankControl = 'both'

To add and remove an interrupt to an input

```
MCP.add_interrupt(10, callbackFunctLow=functA, callbackFunctHigh=functB)  # add interrupt to IO 10 with
call back functions functA and functB
```

- separate callback functs can be set for when the pin goes high and low, the same function can be used for
callbackFunctLow and callbackFunctHigh

On the Raspberry Pi side using the RPi.GPIO module as IO, the following needs to be included in your program
IO.add_event_detect(intPin,IO.RISING,callback=MCP.callbackB)

callback = either MCP.callbackA or MCP.callbackB if using the bankControl = 'seperate'
or callback = MCP.callbackBoth if using the bankControl = 'both'

MCP.remove_interrupt(10)  # remove interrupt from IO 10
