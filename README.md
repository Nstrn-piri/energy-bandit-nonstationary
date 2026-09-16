# Non-Stationary Energy Bandit

## Project Overview

This project implements a simple Reinforcement Learning agent
for energy-management decision making in a non-stationary environment.

The agent learns to choose between three energy actions:

- Buy electricity from the grid
- Use the battery
- Sell electricity to the grid

The environment changes after 500 steps, so the best action
before and after the change is different.

## Actions

| Action | Decision |
|---|---|
| 0 | Buy electricity |
| 1 | Use battery |
| 2 | Sell electricity |

## Reinforcement Learning Method

The agent uses:

- Epsilon-Greedy action selection
- Constant Alpha Q-value update
- Non-Stationary Bandit environment

## Environment

Before step 500:

- Buy: -3
- Battery: +2
- Sell: +4

After step 500:

- Buy: +4
- Battery: +6
- Sell: +1

Random noise is added to the rewards to simulate uncertainty.

## Project Structure

```text
energy-bandit-nonstationary/
│
├── README.md
├── requirements.txt
├── environment.py
├── agent.py
├── train.py
├── plots.py
└── plots/
Installation
pip install -r requirements.txt
Run
python train.py
Results

The agent should learn that:

Sell is more valuable before the environment changes.
Battery becomes more valuable after the environment changes.

The Q-value plot shows how the agent adapts to the environmental change.

Limitation

This project is a simplified Bandit model.

The current action does not explicitly change the next system state.

A realistic photovoltaic-battery energy-management problem requires
a Markov Decision Process (MDP), where the state can include:

Battery SOC
PV generation
Load
Electricity price
Time
Grid power

The MDP formulation will be developed in the next stage of the project.

Future Work
Introduce states
Model battery SOC dynamics
Add PV and load data
Add electricity prices
Formulate the problem as an MDP
Implement Q-Learning
Implement Deep Q-Network (DQN)# energy-bandit-nonstationary
