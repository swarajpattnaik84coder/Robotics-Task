def decide_movement(sensors):

    if all(x == 0 for x in sensors):
        return "Stop Robot"

    if all(x == 1 for x in sensors):
        return "Junction Detected"

    if sensors[2] == 1 or sensors[3] == 1:
        return "Move Forward"

    if sensors[0] == 1 or sensors[1] == 1:
        return "Turn Left"

    if sensors[4] == 1 or sensors[5] == 1:
        return "Turn Right"