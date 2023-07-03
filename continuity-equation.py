# Import necessary libraries
import math

# Function to calculate the cross-sectional area in the continuity equation
def calculate_cross_sectional_area(flow_rate, velocity):
    # Calculate the cross-sectional area using the continuity equation
    area = flow_rate / velocity
    return area

# Inputs required:
flow_rate = 10.0  # Flow rate of the fluid in m^3/s
fluid_velocity = 2.0  # Velocity of the fluid in m/s

# Calculate the cross-sectional area using the continuity equation
cross_sectional_area = calculate_cross_sectional_area(flow_rate, fluid_velocity)

# Print the result
print("Cross-Sectional Area:", cross_sectional_area, "m^2")

