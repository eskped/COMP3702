import gym
import numpy as np

env = gym.make('FrozenLake-v1', desc=None, map_name='4x4', is_slippery=True)


n_episode = 1000
max_timestep_per_episode = 100

alpha = 0.1
epsilon = 0.1
gamma = 0.99
Q = np.random.rand(env.observation_space.n, env.action_space.n)
Q[-1, :] = np.zeros(env.action_space.n)

print(Q)


def epsilon_greedy(Q, s, epsilon):
    if np.random.rand() < epsilon:
        return np.random.randint(env.action_space.n)
    else:
        return np.argmax(Q[s, :])


for ep in range(n_episode):
    s, _ = env.reset()  # initialize state

    for t in range(max_timestep_per_episode):
        a = epsilon_greedy(Q, s, epsilon)
        s_next, r, terminated, _, _ = env.step(a)

        # print(
        #     f'ep: {ep}, t: {t}, s: {s}, a: {a}, r: {r}, s_next: {s_next}, terminated: {terminated}')
        Q[s, a] += alpha * (r + gamma*np.max(Q[s_next, :]) - Q[s, a])

        s = s_next
        if terminated:
            # print(f'Episode {ep} finished after {t+1} timesteps')
            break

policy = np.argmax(Q, axis=1)
for s in range(env.observation_space.n):
    policy[s] = np.argmax(Q[s, :])

print(policy)
