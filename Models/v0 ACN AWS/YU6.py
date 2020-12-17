def reward_function(params):

    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track =  params["all_wheels_on_track"]
    progress = params["progress"]
    steering = abs(params['steering_angle'])
    heading = abs(params['heading'])
    is_left_of_center = params['is_left_of_center']
    speed = params["speed"]
    steps = params["steps"]


    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.3 * track_width


    if all_wheels_on_track  == 1:
        reward = params["progress"]

        # Give higher reward if the car is closer to center line and vice versa
        if distance_from_center <= marker_1:
            reward += 10.0
        elif distance_from_center <= marker_2:
            reward += 5
        elif distance_from_center <= marker_3:
            reward += 0.01
        else:
            reward += -0.5  # likely crashed/ close to off track
    else:
        reward = -1

    ABS_STEERING_THRESHOLD = 25
    if steering > ABS_STEERING_THRESHOLD:
        reward += -1

    return float(reward)
