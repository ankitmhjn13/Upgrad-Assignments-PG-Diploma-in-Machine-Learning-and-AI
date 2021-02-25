# Import routines

import numpy as np
import math
import random
from itertools import permutations


# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_space = [(0, 0)] + list(permutations([i for i in range(m)], 2))
        self.state_space = [[M, T, D] for M in range(m) for T in range(t) for D in range(d)]
        self.state_init = random.choice(self.state_space)
        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input
    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        if not state:
            retur 
        state_encod = [0] * (m+t+d)
        state_encod[state[0]] = 1
        state_encod[state[1] + m] = 1
        state_encod[state[2] + m + t] = 1
        return state_encod

    ## Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        requests = 0
        if location == 0:
            requests = np.random.poisson(2)
        elif location == 1:
            requests = np.random.poisson(12)
        elif location == 2:
            requests = np.random.poisson(4)
        elif location == 3:
            requests = np.random.poisson(7)
        elif location == 4:
            requests = np.random.poisson(8)
        if requests >15:
            requests = 15

        possible_actions_index = random.sample(range(1, (m-1)*m +1), requests) + [0] # (0,0) is not considered as customer request
        actions = [0,0] + [self.action_space[i] for i in possible_actions_index]
        return possible_actions_index,actions   



    def reward_func(self, wait_time, transit_time, ride_time):
        """Takes in state, action and Time-matrix and returns the reward"""
        idle_time = wait_time + transit_time
        reward = (R * ride_time) - (C * (ride_time + idle_time))
        return reward

    
    def step(self, state, action, Time_matrix):
        next_state, wait_time, transit_time, ride_time = self.next_state_func(state, action, Time_matrix)
        rewards = self.reward_func(wait_time, transit_time, ride_time)
        total_time = wait_time + transit_time + ride_time
        return rewards, next_state, total_time


    def reset(self):
        return self.action_space, self.state_space, self.state_init


    def update_time_day(self, time, day, ride_duration):
        ride_duration = int(ride_duration)
        if (time + ride_duration) < 24:
            time = time + ride_duration
        else:
            time = (time + ride_duration) % 24 
            num_days = (time + ride_duration) // 24
            day = (day + num_days ) % 7
        return time, day
    
    
    def next_state_func(self, state, action, Time_matrix):
        next_state = []
        total_time = 0
        transit_time = 0
        wait_time = 0
        ride_time = 0
        
        cur_loc = state[0]
        st_loc = action[0]
        end_loc = action[1]
        curr_time = state[1]
        curr_day = state[2]
        next_loc = cur_loc
        
        if st_loc == 0 and end_loc == 0:
            wait_time = 1
            next_loc = cur_loc
        elif cur_loc == st_loc:
            ride_time = Time_matrix[cur_loc][end_loc][curr_time][curr_day]
            next_loc = end_loc
        else:
            transit_time = Time_matrix[cur_loc][st_loc][curr_time][curr_day]
            new_time, new_day = self.update_time_day(curr_time, curr_day, transit_time)
            ride_time = Time_matrix[cur_loc][end_loc][new_time][new_day]
            next_loc = end_loc

        total_time = (wait_time + transit_time + ride_time)
        next_time, next_day = self.update_time_day(curr_time, curr_day, total_time)
        next_state = [next_loc, next_time, next_day]
        return next_state, wait_time, transit_time, ride_time

    