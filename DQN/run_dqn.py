import gym
import time
import numpy as np
from dqn_pixels import TrainDQN
# from dqn import TrainDQN
import tensorflow as tf


def main():
    with tf.Session() as sess:
        # env_name = 'CartPole-v0'
        env_name = 'CubeCrash-v0'
        env = gym.make(env_name)
        dqn = TrainDQN(env,
                       sess,
                       # conv
                       max_steps=0,
                       load_path=f'checkpoints/{env_name}.ckpt')

        num_episodes = 100
        obs = env.reset()
        reward = 0

        while num_episodes > 0:
            env.render()
            obs, rew, done, _ = env.step(dqn.act(obs))
            reward += rew
            time.sleep(0.01)
            if done:
                num_episodes -= 1
                obs = env.reset()
                print('Episode Reward:', reward)
                reward = 0


if __name__ == '__main__':
    main()
