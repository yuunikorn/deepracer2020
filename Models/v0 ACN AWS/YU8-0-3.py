def reward_function(params):

    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track =  params["all_wheels_on_track"]
    progress = params["progress"]

    steering = abs(params['steering_angle']) # agent's steering angle in degrees
    heading = abs(params['heading']) # agent's yaw in degrees

    is_left_of_center = params['is_left_of_center'] # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    speed = params["speed"] # float # agent's speed in meters per second (m/s)
    steps = params["steps"] #int # number steps completed

    closest_waypoints = params["closest_waypoints"]  #[int, int] # indices of the two nearest waypoints.
    waypoints = params["waypoints"]   #[(float, float), ] #list of (x,y) as milestones along the track center

    is_crashed = params["is_crashed"]   # Boolean flag to indicate whether the agent has crashed.
    is_reversed = params["is_reversed"] # Boolean, flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    is_offtrack = params["is_offtrack"]  # Boolean flag to indicate whether the agent has gone off track.

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.3 * track_width

    reward = 0.0001

    #REWARDS
    if all_wheels_on_track  == 1:
        reward = params["progress"]

        # Give higher reward if the car is closer to center line and vice versa
        if distance_from_center <= marker_1:
            reward += 10.0
        elif distance_from_center <= marker_2:
            reward += 5
        elif distance_from_center <= marker_3:
            reward += 0.01
        # else:
        #     reward += 0.000001  # likely crashed/ close to off track
    # else:
    #     reward = 0.0001

    #PENALTY
    ABS_STEERING_THRESHOLD = 10
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    if is_offtrack:
        reward *= 0.7
    else:
        reward *= 1.1

    if is_crashed:
        reward *= 0.6

    if is_reversed:
        reward *= 0.5

    return float(reward)



# Action number
# Steering
# Speed
# 0
# -30degrees
# 0.33m/s
# 1
# -30degrees
# 0.67m/s
# 2
# -30degrees
# 1m/s
# 3
# 0degrees
# 0.33m/s
# 4
# 0degrees
# 0.67m/s
# 5
# 0degrees
# 1m/s
# 6
# 30degrees
# 0.33m/s
# 7
# 30degrees
# 0.67m/s
# 8
# 30degrees
# 1m/s
