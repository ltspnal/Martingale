import random

HEADS = "heads"  # Represents the outcome of the coin flip: heads
TAILS = "tails"  # Represents the outcome of the coin flip: tails
COIN_VALUES = [HEADS, TAILS]  # List of possible coin values

def flip_coin():
    """Function to simulate flipping a coin."""
    return random.choice(COIN_VALUES)  # Returns a random choice from coin values

def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    """
    Function to play using the Martingale strategy.

    Parameters:
        starting_funds: Initial amount of money.
        min_bet: Minimum bet amount.
        max_bet: Maximum bet amount.

    Returns:
        Number of steps until losing all funds.
    """
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds > 0:
        steps_to_loose += 1
        current_funds -= current_bet
        flipped_coin_value = flip_coin()
        if flipped_coin_value == HEADS:
            win = current_bet * 2
            current_bet += win
            current_bet = min_bet
        else:
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds
    
    return steps_to_loose

def simulate_martingale_for_n_players(*, starting_funds: int, min_bet: int, max_bet: int, n_games: int) -> float:
    """
    Function to simulate Martingale strategy for multiple players.

    Parameters:
        starting_funds: Initial amount of money for each player.
        min_bet: Minimum bet amount for each player.
        max_bet: Maximum bet amount for each player.
        n_games: Number of games to simulate for each player.

    Returns:
        Average number of steps until losing all funds for all players.
    """
    total_steps_to_loose = 0
    for i in range(n_games):
        step_to_loose = play_martingale(starting_funds = starting_funds, min_bet = min_bet, max_bet = max_bet)
        total_steps_to_loose += step_to_loose

    return total_steps_to_loose / n_games

print(
    simulate_martingale_for_n_players(
        n_games = 10,
        starting_funds = 1000,
        min_bet = 1,
        max_bet = 100
    )
)
