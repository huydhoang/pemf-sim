# pemf-sim
A series of calculations to simulate a PEMF device

## Resistance, Current, MF Strength

To calculate the magnetic field (MF) strength of the coil, we need to determine the magnetic field at the center of a solenoid. The formula for the magnetic field at the center of a solenoid is:

\[
B = \mu_0 \cdot \frac{N \cdot I}{L}
\]

Where:
- \( B \) is the magnetic field strength (in Tesla, T),
- \( \mu_0 \) is the permeability of free space (\( 4\pi \times 10^{-7} \, \text{T}\cdot\text{m/A} \)),
- \( N \) is the number of turns in the coil,
- \( I \) is the current flowing through the coil (in Amperes, A),
- \( L \) is the length of the coil (in meters, m).

First, let's calculate the current \( I \) using Ohm's Law:

\[
I = \frac{V}{R}
\]

Where:
- \( V \) is the voltage (19.5 V),
- \( R \) is the resistance of the wire.

The resistance \( R \) of the wire can be calculated as:

\[
R = \rho \cdot \frac{l}{A}
\]

Where:
- \( \rho \) is the resistivity of the wire material (typically copper, with \( \rho = 1.68 \times 10^{-8} \, \Omega \cdot \text{m} \)),
- \( l \) is the length of the wire (which we need to estimate based on the coil dimensions),
- \( A \) is the cross-sectional area of the wire.

We know the diameter of the coil, thickness of the wire, number of turns, and length of the coil, so we can calculate \( l \) and \( A \).

"""python
import math

# Given values
V = 19.5  # voltage in volts
N = 1000  # number of turns
coil_length = 50 / 1000  # coil length in meters (converted from mm)
wire_thickness = 0.5 / 1000  # wire thickness in meters (converted from mm)
coil_diameter = 75 / 1000  # coil diameter in meters (converted from mm)
rho_copper = 1.68e-8  # resistivity of copper in ohm meter

# Cross-sectional area of the wire
A = math.pi * (wire_thickness / 2) ** 2

# Estimate the length of wire l, assuming N turns and that the coil length is 50 mm
# Length per turn is approximately the circumference of the coil
length_per_turn = math.pi * coil_diameter
total_wire_length = length_per_turn * N

# Calculate the resistance of the wire
R = rho_copper * (total_wire_length / A)

# Calculate the current using Ohm's Law
I = V / R

# Permeability of free space
mu_0 = 4 * math.pi * 1e-7

# Calculate the magnetic field at the center of the solenoid
B = mu_0 * (N * I) / coil_length
B, I, R
"""

## 
