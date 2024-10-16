"""
Solutions to module VA 1
Student: 
Mail:
"""

def exchange(a, coins) -> list: 
    """ Count possible way to exchange a with the coins in coins. Use memoization"""
    memo = [[None for _ in range(a+1)] for _ in range(len(coins)+1)]
    def exchange(a, coins):
        if a == 0:
            return 1
        elif a < 0 or len(coins) == 0:
            return 0
        else:
            return exchange(a, coins[1:]) + exchange(a-coins[0], coins)

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
    l1 = [1,2,3]
    l2 = zippa(l1, [])
    l1.append(4)
    print(l2)


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 1

What time did it take to calculate large sums such as 1000 and 2000? 

What happens if you try to calculate e.g. 10000?
  
"""
