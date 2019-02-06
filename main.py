import minimalmodbus

instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instr.serial.baudrate = 9600
instr.serial.timeout  = 1
instr.debug = True
instr.read_register(61, 4)