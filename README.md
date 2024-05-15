Martingale Strategy Simulation
This Python script simulates the famous casino gambling strategy known as the Martingale strategy.

Introduction
The Martingale strategy is a popular betting strategy that suggests doubling the bet after each loss to recover previous losses and potentially gain a profit. This script provides a simulation of this strategy for multiple players over a series of games.

Usage
To use this script, simply run heads_tails.py. You can adjust the parameters such as starting funds, minimum and maximum bets, and the number of games to simulate for each player directly in the script.

How It Works
The script contains two main functions:

play_martingale(): This function implements the Martingale strategy. It simulates a player's betting process until they run out of funds. The player doubles their bet after each loss and resets it to the minimum bet after a win.

simulate_martingale_for_n_players(): This function conducts a simulation of the Martingale strategy for multiple players. It repeats the betting process for a specified number of games and calculates the average number of steps until the player goes bankrupt.

Example
Here's an example of how to run the script:

python heads_tails.py
This will simulate the Martingale strategy for a predefined number of games and print out the average number of steps until a player goes bankrupt.

Disclaimer
Please note that this script is for educational purposes only and should not be considered financial advice. The Martingale strategy is a high-risk betting strategy that can lead to significant losses.
