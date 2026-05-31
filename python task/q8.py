angles = [30, -15, 45, 200, 60, 90]

def valid_angle(angle):
    return 0 <= angle <= 180

valid_angles = list(filter(valid_angle, angles))

def servo_command(angle):
    return angle * 10

commands = list(map(servo_command, valid_angles))

print("Valid Angles:", valid_angles)
print("Servo Commands:", commands)