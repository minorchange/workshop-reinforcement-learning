import gym 
from IPython import display
import matplotlib.pyplot as plt
# %matplotlib inline


# In case you run the notebooks from a jupyter hub server
# you will not be able to render the evns output in a popup window.
# In this case you can use this render_jh funciton:
def render_jh(env):
    plt.imshow(env.render(mode='rgb_array'))
    display.display(plt.gcf())
    display.clear_output(wait=True)

    
env = gym.make('Pong-ram-v0')
env.reset()
for _ in range(100):
    render_jh(env)
    action = env.action_space.sample()
    env.step(action)
    
    