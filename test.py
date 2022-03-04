from clevr_robot_env.env import ClevrEnv

env = ClevrEnv()

for step in range(1000):
    action = env.sample_random_action()
    env.step(action)
    env.render()
