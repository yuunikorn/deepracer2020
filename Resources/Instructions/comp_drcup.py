def reward_function(params):
    '''
    Example of rewarding the agent to stay inside two borders
    and penalizing getting too close to the objects in front
    '''

    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    progress = params["progress"]
    speed = params["speed"] # float # agent's speed in meters per second (m/s)

    objects_distance = params['objects_distance']
    _, next_object_index = params['closest_objects']
    objects_left_of_center = params['objects_left_of_center']
    is_left_of_center = params['is_left_of_center']


    steering = abs(params['steering_angle']) # agent's steering angle in degrees
    heading = abs(params['heading']) # agent's yaw in degrees

    is_left_of_center = params['is_left_of_center'] # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    steps = params["steps"] #int # number steps completed

    closest_waypoints = params["closest_waypoints"]  #[int, int] # indices of the two nearest waypoints.
    waypoints = params["waypoints"]   #[(float, float), ] #list of (x,y) as milestones along the track center

    is_crashed = params["is_crashed"]   # Boolean flag to indicate whether the agent has crashed.
    is_reversed = params["is_reversed"] # Boolean, flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    is_offtrack = params["is_offtrack"]  # Boolean flag to indicate whether the agent has gone off track.


    # Initialize reward with a small number but not zero
    # because zero means off-track or crashed
    reward = 1e-3

    # Reward if the agent stays inside the two borders of the track
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward += params["progress"]
        reward_lane = 1.0
    else:
        reward_lane = 1e-3

    # Penalize if the agent is too close to the next object
    reward_avoid = 1.0

    # Distance to the next object
    distance_closest_object = objects_distance[next_object_index]
    # Decide if the agent and the next object is on the same lane
    is_same_lane = objects_left_of_center[next_object_index] == is_left_of_center

    if is_same_lane:
        if 0.5 <= distance_closest_object < 0.8:
            reward_avoid *= 0.5
        elif 0.3 <= distance_closest_object < 0.5:
            reward_avoid *= 0.2
        elif distance_closest_object < 0.3:
            reward_avoid = 1e-3 # Likely crashed

    #self added
    ABS_STEERING_THRESHOLD = 15
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.9

    if is_offtrack:
        reward *= 0.7
    else:
        reward *= 1.1

    if is_crashed:
        reward *= 0.6

    if is_reversed:
        reward *= 0.5

    # Calculate reward by putting different weights on
    # the two aspects above
    reward += 1.0 * reward_lane + 4.0 * reward_avoid

    return reward


# # # # Gradient descent batch size: 128
# # # # Number of epochs: 5
# # # # Learning rate: 0.0003
# # # # Entropy: 0.1
# # # # Discount factor: 0.99
# # # # Loss type: Huber
# # # # Number of experience episodes between each policy-updating iteration: 5
