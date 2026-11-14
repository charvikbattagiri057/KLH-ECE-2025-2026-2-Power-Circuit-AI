import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(file='test_schematic.png', show=False) as d:
    d += elm.Resistor().label('1K')
    d += elm.Capacitor().down().label('10uF')
    d += elm.Line().left()
    d += elm.SourceV().up().label('10V')

print("Schemdraw smoke test passed! test_schematic.png generated.")