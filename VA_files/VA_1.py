"""
Solutions to module VA 1
Student: Alexander Hedene
Mail: alex.hedene@gmail.com
"""
import time as t

def exchange(a, coins) -> int:
    """Count the possible ways to exchange 'a' with the coins in 'coins'. Use memoization."""
    memo = {}

    def _exchange(a, coins):
        if a == 0: 
            return 1
        elif a < 0 or len(coins) == 0:  
            return 0
        else:
            if (a, len(coins)) in memo:  
                return memo[(a, len(coins))]

            memo[(a, len(coins))] = _exchange(a, coins[1:]) + _exchange(a - coins[0], coins)

            return memo[(a, len(coins))] 

    return _exchange(a, coins)

def zippa(l1: list, l2: list) -> list: 
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    if len(l1) == 0 and len(l2) == 0:
        return []
    elif len(l1) == 0:
        return l2.copy()
    elif len(l2) == 0:
        return l1.copy()
    else:
        return [l1[0]] + [l2[0]] + zippa(l1[1:], l2[1:])


def main():
    print('\nCode that demonstates my implementations\n')
    start = t.perf_counter()
    exchange(991,[1,5,10,100,200])
    end = t.perf_counter()
    print(f"Time for a = 991: t = {end-start}")


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 1

What time did it take to calculate large sums such as 1000 and 2000? 
One problem with exchange which i cant come around is always hitting the recursion limit. This is because i have 1 as a coin.
This will make a recursion step for where i start with a, then i need to calculate a-1, and for this i need a-2....
This results in a recursion depth = a. This is a problem for a bigger than 994 for my computer. 
The time for a = 993 is: t = 6.47ms

What happens if you try to calculate e.g. 10000?
  Cant because of recursion length
"""
