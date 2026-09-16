import numpy as np
import matplotlib.pyplot as plt
import os


def plot_q_values(q_history):

    q_history = np.array(q_history)

    plt.figure()

    plt.plot(q_history[:, 0], label="Buy")
    plt.plot(q_history[:, 1], label="Battery")
    plt.plot(q_history[:, 2], label="Sell")

    plt.axvline(
        500,
        linestyle="--",
        label="Environment Change"
    )

    plt.xlabel("Step")
    plt.ylabel("Q Value")

    plt.title("Q Values in Non-Stationary Energy Bandit")

    plt.legend()

    plt.tight_layout()
    os.makedirs("plots", exist_ok=True)

    plt.savefig("plots/q_values.png")

    plt.show()


def plot_cumulative_reward(rewards):

    cumulative_reward = np.cumsum(rewards)

    plt.figure()

    plt.plot(cumulative_reward)

    plt.xlabel("Step")
    plt.ylabel("Cumulative Reward")

    plt.title("Cumulative Reward")

    plt.tight_layout()
    os.makedirs("plots", exist_ok=True)

    plt.savefig("plots/cumulative_reward.png")

    plt.show()


def plot_action_counts(action_counts):

    plt.figure()

    plt.bar(
        ["Buy", "Battery", "Sell"],
        action_counts
    )

    plt.xlabel("Action")
    plt.ylabel("Count")

    plt.title("Action Selection Counts")

    plt.tight_layout()
    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/actions.png")

    plt.show()