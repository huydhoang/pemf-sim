import math

# Given values
V = 19.5  # voltage in volts
N = 1000  # number of turns
coil_length = 50 / 1000  # coil length in meters (converted from mm)
wire_thickness = 0.5 / 1000  # wire thickness in meters (converted from mm)
coil_diameter = 75 / 1000  # coil diameter in meters (converted from mm)
rho_copper = 1.68e-8  # resistivity of copper in ohm meter
copper_density = 8960  # density of copper in kg/m^3

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

# Volume of copper wire (cross-sectional area * length of the wire)
wire_volume = A * total_wire_length

# Total weight of copper wire (volume * density)
total_weight = wire_volume * copper_density

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

print(output)
