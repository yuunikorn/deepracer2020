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

    reward = params["progress"]


    #REWARDS
    multiplier = 1.5
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1 and all_wheels_on_track:
        reward += 50.0*multiplier
    elif distance_from_center <= marker_2 and all_wheels_on_track:
        reward += 5*multiplier
    elif distance_from_center <= marker_3 and all_wheels_on_track:
        reward += 0.01*multiplier
    elif all_wheels_on_track == 0 or distance_from_center > marker_3:
        reward *= 0.3

    #PENALTY
    ABS_STEERING_THRESHOLD = 15
    if steering <= ABS_STEERING_THRESHOLD and all_wheels_on_track:
        reward *= 1.1
    elif steering > ABS_STEERING_THRESHOLD and all_wheels_on_track:
        reward *= 0.7

    if is_offtrack:
        reward *= 0.3
    else:
        reward *= 1.1

    if is_crashed:
        reward = -100

    if is_reversed:
        reward = -100

    return float(reward)











# Action number
# Steering
# Speed
# 0
# -30degrees
# 1.33m/s
# 1
# -30degrees
# 2.67m/s
# 2
# -30degrees
# 4m/s
# 3
# -20degrees
# 1.33m/s
# 4
# -20degrees
# 2.67m/s
# 5
# -20degrees
# 4m/s
# 6
# -10degrees
# 1.33m/s
# 7
# -10degrees
# 2.67m/s
# 8
# -10degrees
# 4m/s
# 9
# 0degrees
# 1.33m/s
# 10
# 0degrees
# 2.67m/s
# 11
# 0degrees
# 4m/s
# 12
# 10degrees
# 1.33m/s
# 13
# 10degrees
# 2.67m/s
# 14
# 10degrees
# 4m/s
# 15
# 20degrees
# 1.33m/s
# 16
# 20degrees
# 2.67m/s
# 17
# 20degrees
# 4m/s
# 18
# 30degrees
# 1.33m/s
# 19
# 30degrees
# 2.67m/s
# 20
# 30degrees
# 4m/s

# 
# Hyperparameter
# Value
# Gradient descent batch size	64
# Entropy	0.005
# Discount factor	0.6
# Loss type	Huber
# Learning rate	0.0000001
# Number of experience episodes between each policy-updating iteration	10
# Number of epochs	3
