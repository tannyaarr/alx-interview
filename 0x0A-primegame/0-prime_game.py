#!/usr/bin/python3
"""prime game giving the winner"""


def isWinner(x, nums):
"""give a winner"""
    if x < 1 or not nums:
        return None
    
    # Find the maximum value in nums to create sieve up to that value
    max_n = max(nums)
    
    # Sieve of Eratosthenes to find all primes up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
                
    # Function to determine the winner of a single game
    def determine_winner(n):
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        turn = 0  # 0 for Maria's turn, 1 for Ben's turn
        
        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            turn = 1 - turn  # Switch turns
        
        return turn  # 0 if Ben wins, 1 if Maria wins
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = determine_winner(n)
        if winner == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
