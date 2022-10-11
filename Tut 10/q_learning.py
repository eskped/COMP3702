import gym
import numpy as np
import random

env = gym.make('FrozenLake-v1', desc=None, map_name='4x4', is_slippery=True)


n_episode = 10000
max_timestep_per_episode = 100

alpha = 0.1
epsilon = 0.1
gamma = 0.99
n_features = 10
w = np.random.rand(n_features)

Q = np.random.rand(env.observation_space.n, env.action_space.n)
# Q = np.zeros((env.observation_space.n, env.action_space.n))
Q[-1, :] = np.zeros(env.action_space.n)

print(Q)


def epsilon_greedy(Q, s, epsilon):
    if np.random.rand() < epsilon:
        return np.random.choice(env.action_space.n)
    else:
        return np.argmax(Q[s, :])


def get_feature(s, a):
    return


for ep in range(n_episode):
    s, _ = env.reset()  # initialize state

    for t in range(max_timestep_per_episode):
        a = epsilon_greedy(Q, s, epsilon)
        s_next, r, terminated, _, _ = env.step(a)

        # tabular Q-learning update
        Q[s, a] += alpha * (r + gamma*np.max(Q[s_next, :]) - Q[s, a])
        # w = w + alpha * (r + gamma * np.max(Q_approx[s_next, :]) - Q[s, a])*Q[s,a] # linear Q-learning update

        def Q_approx(s, a):
            f_sa = get_feature(s, a)  # 3-element vector
            value = np.dot(w, f_sa)
            return value

        s = s_next
        if terminated:
            # print(f'Episode {ep} finished after {t+1} timesteps')
            break

policy = np.argmax(Q, axis=1)
for s in range(env.observation_space.n):
    policy[s] = np.argmax(Q[s, :])

print(f'policy: {policy}')
