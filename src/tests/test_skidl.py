import os

# Force SKiDL to look for libraries on your D drive BEFORE importing skidl
kicad_sym_path = r"D:\Kicad\share\kicad\symbols"
os.environ['KICAD8_SYMBOL_DIR'] = kicad_sym_path
os.environ['KICAD_SYMBOL_DIR'] = kicad_sym_path
os.environ['KICAD10_SYMBOL_DIR'] = kicad_sym_path

from skidl import *

# Create a basic RC circuit
r1 = Part("Device", "R", value="1K")
c1 = Part("Device", "C", value="10uF")

# Define nets
vin = Net('VIN')
gnd = Net('GND')
vout = Net('VOUT')

# Connect parts
vin += r1[1]
vout += r1[2], c1[1]
gnd += c1[2]

# Run Electrical Rules Check (ERC)
ERC()

# Generate netlist
generate_netlist(file_="test_netlist.net")
print("SKiDL smoke test passed! test_netlist.net generated.")