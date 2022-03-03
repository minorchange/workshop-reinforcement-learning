import numpy as np
from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete 
from course_001_FlowerField import FlowerField


class FlowerFiledEnv(Env):

    def __init__(self):
        
        self.action_space = Discrete(11)
        self.observation_space = Box(low=np.array([1]).astype(np.float32), 
                                     high=np.array([1]).astype(np.float32))
        self.reset()
        
    def _change_state_accorging_to_action(self, action):
        return self.state

    def _calculate_reward(self, action):
        flower_id = action
        amount_of_polen = self.ff.visit_flower_nr(flower_id)
        reward = amount_of_polen
        return reward

    def _check_if_done(self):   
        self.n_trips += 1 
        done = False
        if self.n_trips >= 50: 
            done = True
        return done

    def _create_info(self):
        info = {"some important information": "can go here"}        
        return info

    def step(self, action):
        
        observation = self._change_state_accorging_to_action(action)
        reward = self._calculate_reward(action)
        done = self._check_if_done()
        info = self._create_info()
        
        return observation, reward, done, info

    def render(self):
        print(self.n_trips)
    
    def reset(self):
        self.ff = FlowerField()
        self.n_trips = 0
        # The state of the filed is not changed by the action in this (boring) example ther is only one state
        self.state = np.array([1]).astype(np.float32)
        return self.state