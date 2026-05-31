from sensor import get_sensor_values
from movement import decide_movement

sensors, active = get_sensor_values()

print("Sensor Values:", sensors)
print("Active Sensors:", active)

action = decide_movement(sensors)

print("Robot Action:", action)