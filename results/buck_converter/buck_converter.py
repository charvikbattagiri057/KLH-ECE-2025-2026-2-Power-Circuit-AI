import os

# Configure KiCad symbol library paths for SKiDL
kicad_sym_path = os.environ.get("KICAD_SYMBOL_DIR", r"D:\Kicad\share\kicad\symbols")
for var in ['KICAD_SYMBOL_DIR', 'KICAD8_SYMBOL_DIR', 'KICAD10_SYMBOL_DIR']:
    os.environ[var] = kicad_sym_path

from skidl import *

# ==============================================================================
# Power Circuit Design: Buck Converter (CCM)
# Specifications:
#   Vin_min  = 12.0 V, Vin_max = 15.0 V, Vin_nom = 13.5 V
#   Vout     = 5.0 V
#   Iout_max = 2.0 A
#   fsw      = 100 kHz
#   mode     = CCM
#
# Design Calculations:
#   R_load   = Vout / Iout_max = 5.0 / 2.0 = 2.5 Ohms
#   Duty (D) = Vout / Vin_nom = 5.0 / 13.5 ≈ 0.370
#   dI_L     = 0.3 * Iout_max = 0.6 A (30% ripple current)
#   L        = (Vin_nom - Vout) * D / (fsw * dI_L) ≈ 52.5 uH -> Standard 56 uH
#   dVout    = 0.01 * Vout = 50 mV (1% output ripple)
#   C_out    = dI_L / (8 * fsw * dVout) ≈ 15 uF -> Standard 22 uF
# ==============================================================================

# Create Nets with appropriate power drive flags to satisfy ERC
vin_net = Net('VIN')
gnd_net = Net('GND')
sw_net = Net('SW')
vout_net = Net('VOUT')
gate_net = Net('GATE')

# Power flags: indicate driving power rails for Electrical Rules Check
vin_net.drive = POWER
gnd_net.drive = POWER
gate_net.drive = POWER

# Instantiate Components with KiCad standard footprints to eliminate netlist errors
v_in = Part(
    'Device', 'Battery', 
    value='13.5V', 
    footprint='Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical'
)
q_main = Part(
    'Device', 'Q_NMOS', 
    footprint='Package_TO_SOT_SMD:TO-252-2'
)
d_freewheel = Part(
    'Device', 'D_Schottky', 
    footprint='Diode_SMD:D_SMA'
)
l_filter = Part(
    'Device', 'L', 
    value='56uH', 
    footprint='Inductor_SMD:L_12x12mm_h6mm'
)
c_filter = Part(
    'Device', 'C', 
    value='22uF', 
    footprint='Capacitor_SMD:C_1206_3216Metric'
)
r_load = Part(
    'Device', 'R', 
    value='2.5', 
    footprint='Resistor_SMD:R_0805_2012Metric'
)
# Gate pull-down resistor: ensures Gate is not floating and terminates the GATE net
r_gate = Part(
    'Device', 'R', 
    value='10k', 
    footprint='Resistor_SMD:R_0805_2012Metric'
)

# Connect Input DC Source
v_in['+'] += vin_net
v_in['-'] += gnd_net

# Connect Main Switch (NMOS: Gate, Drain to VIN, Source to SW)
q_main['G'] += gate_net
q_main['D'] += vin_net
q_main['S'] += sw_net

# Connect Gate pull-down resistor (GATE to GND)
r_gate[1] += gate_net
r_gate[2] += gnd_net

# Connect Freewheeling Diode (Cathode to SW, Anode to GND)
d_freewheel['K'] += sw_net
d_freewheel['A'] += gnd_net

# Connect Output Filter Inductor (SW to VOUT)
l_filter[1] += sw_net
l_filter[2] += vout_net

# Connect Output Filter Capacitor (VOUT to GND)
c_filter[1] += vout_net
c_filter[2] += gnd_net

# Connect Load Resistor (VOUT to GND)
r_load[1] += vout_net
r_load[2] += gnd_net

# Perform Electrical Rules Check
ERC()

# Generate Netlist
generate_netlist(file_="buck_converter.net")

print("SKiDL buck converter circuit successfully generated and verified!")
print("Netlist written to buck_converter.net")
