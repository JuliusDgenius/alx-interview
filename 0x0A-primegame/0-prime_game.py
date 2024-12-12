#!/usr/bin/python3
"""
Prime Game: Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n, they take turns choosing
a prime number from the set and removing that number and its multiples.
The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """
    Determine the winner of x rounds of the prime game.
    Args:
        x (int): Number of rounds
        nums (list): Array of n for each round
    Returns:
        string: Name of winner (Maria/Ben) or None if tie/invalid
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    # For each round
    for n in nums:
        if n < 1:
            continue

        # Create Sieve of Eratosthenes array
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        # Generate prime numbers using Sieve
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        # Count prime numbers
        prime_count = sum(1 for i in range(2, n + 1) if primes[i])

        # If prime_count is even, Ben wins, else Maria wins
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
