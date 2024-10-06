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

```python
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
```

## Wire Length and Weight

1. **Wire Length**:  
   The total length of the copper wire required to build the coil is calculated using the formula:

   \[
   \text{Total Length of Wire} = N \times \text{Length per Turn}
   \]
   Where:
   - \( N \) is the number of turns (1000 turns),
   - \( \text{Length per Turn} = \pi \times \text{Coil Diameter} \).

   This gives the total wire length needed to wrap the coil.

2. **Wire Weight**:  
   The weight of the wire is calculated by first determining its volume and then multiplying by the density of copper:
   
   \[
   \text{Volume of Wire} = \text{Cross-Sectional Area} \times \text{Total Length of Wire}
   \]
   
   The cross-sectional area \( A \) of the wire is the area of a circle:
   
   \[
   A = \pi \times \left(\frac{\text{Wire Thickness}}{2}\right)^2
   \]
   
   Finally, the weight is obtained by multiplying the volume of the wire by the density of copper \( \rho_{\text{copper}} \):
   
   \[
   \text{Weight of Wire} = \text{Volume of Wire} \times \rho_{\text{copper}}
   \]
   
   Where the density of copper is \( 8960 \, \text{kg/m}^3 \).


```python
import math

# Given values
N = 1000  # number of turns
coil_diameter = 75 / 1000  # coil diameter in meters
wire_thickness = 0.5 / 1000  # wire thickness in meters
copper_density = 8960  # density of copper in kg/m^3

# Cross-sectional area of the wire
A = math.pi * (wire_thickness / 2) ** 2

# Length per turn (circumference of the coil)
length_per_turn = math.pi * coil_diameter

# Total length of the copper wire
total_wire_length = length_per_turn * N

# Volume of the copper wire
wire_volume = A * total_wire_length

# Total weight of copper wire
total_weight = wire_volume * copper_density

```

## Power Dissipation and Temperature

To calculate the **power dissipation** in the coil, we can use Joule's Law for power:

\[
P = I^2 \cdot R
\]

Where:
- \( P \) is the power dissipated in watts (W),
- \( I \) is the current through the coil,
- \( R \) is the resistance of the coil.

Next, for estimating the **temperature rise** of the coil, we can use the formula for heat dissipation, assuming the coil reaches thermal equilibrium. The temperature rise is related to power dissipation and the coil's ability to radiate or convect heat to the surroundings. A basic approximation of the temperature rise (\( \Delta T \)) can be:

\[
\Delta T = \frac{P}{A \cdot h}
\]

Where:
- \( A \) is the surface area of the coil (in square meters),
- \( h \) is the heat transfer coefficient, which for natural convection in air can be approximately \( 10 \, \text{W/m}^2\cdot\text{K} \).

The estimated final temperature of the coil would then be:

\[
T_{\text{coil}} = T_{\text{ambient}} + \Delta T
\]

```python
# Power dissipation in watts (P = I^2 * R)
P = I**2 * R

# Surface area of the coil (cylinder area = 2 * pi * r * L + 2 * pi * r^2 for the ends)
r_coil = coil_diameter / 2  # radius of the coil
A_surface = (2 * math.pi * r_coil * coil_length) + (2 * math.pi * r_coil**2)

# Heat transfer coefficient (natural convection in air, approximated as 10 W/m^2K)
h = 10  # W/m^2K

# Temperature rise (Delta T = P / (A * h))
delta_T = P / (A_surface * h)

# Ambient temperature in Celsius
T_ambient = 30  # degrees Celsius

# Final temperature of the coil
T_coil = T_ambient + delta_T

# Organize output with additional information
output = f"""
Magnetic Field Strength (B): {B:.6f} Tesla
Current (I): {I:.6f} Amps
Resistance (R): {R:.6f} Ohms
Total Length of Copper Wire: {total_wire_length:.6f} meters
Total Weight of Copper Wire: {total_weight:.6f} kg
Power Dissipation (P): {P:.6f} Watts
Temperature Rise (ΔT): {delta_T:.6f} °C
Estimated Coil Temperature: {T_coil:.6f} °C
"""

```

