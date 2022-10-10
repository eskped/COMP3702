import gym

env = gym.make('FrozenLake-v1', desc=None, map_name='4x4', is_slippery=True)


# print(f'env.action_space: {env.action_space}')
# print(f'env.observation_space: {env.observation_space}')

n_episode = 3
max_timestep_per_episode = 100


for ep in range(n_episode):
    s, _ = env.reset()
    for t in range(max_timestep_per_episode):
        a = env.action_space.sample()
        s_next, r, terminated, _, _ = env.step(a)
        print(
            f'ep: {ep}, t: {t}, s: {s}, a: {a}, r: {r}, s_next: {s_next}, terminated: {terminated}')
        if terminated:
            print(f'Episode {ep} finished after {t+1} timesteps')
            break
