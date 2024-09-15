"""
Solutions to module 1
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def multiply(m: int, n: int) -> int: 
    if m == 0 or n == 0:
        return 0
    else:
        return n + multiply(m-1,n)
  

def harmonic(n: int) -> float:              
    if n == 1 or n == 0:
        return 1
    else:
        return 1/n + harmonic(n-1)

def get_binary(x: int) -> str:
    # 1: 1,  2: 10,  3: 11,  4: 100,  5: 101,  6: 110,  7: 111,  8: 1000         
    if x < 0:
        return "-" + get_binary(-x)
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    
    return get_binary(x//2) + str(x % 2)


def reverse_string(s: str) -> str: 
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s     
    else:
        return s[-1] + reverse_string(s[:-1])
              
def largest(a: iter):
    if len(a) == 1:
        return a[0]
    else:
        return a[0] if a[0] > largest(a[1:]) else largest(a[1:])


def count(x, s: list) -> int:                
    """ Counts the number of occurences of x on all levels in s"""
    if len(s) == 0:
        return 0
    elif x == s[0]:
        return 1 + count(x,s[1:])
    elif type(s[0]) == list:
        return count(x,s[0]) + count(x,s[1:])
    else:
        return count(x,s[1:])
 

def bricklek(f: str, t: str, h: str, n: int) -> str:  
# 1: f->t
# 2: f->h, f->t, h->t
# 2: bricklek(f, h, t, n-1) + bricklek(f, t, h, 1) + bricklek(h, t, f, n-1)
# 3: f->t, f->h, t->h, f->t, h->f, h->t, f->t # Ändra plats på f,t,h 
# 3: bricklek(f, h, t, n-1) + bricklek(f, t, h, 1) + bricklek(h, t, f, n-1)
    if n == 0:
        return []
    return bricklek(f, h, t, n-1) + [f + "->" + t] + bricklek(h, t, f, n-1)
    


def fib(n: int) -> int:                      
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_mem(n:int) -> int:
    memory = {0:0, 1:1}
    def fib(n: int) -> int:
        if n not in memory:
            memory[n] = fib(n-1) + fib(n-2)
        return memory[n]
    return fib(n)

def main():
    print('\nCode that demonstates my implementations\n')



    print('\n\nCode for analysing fib\n')
    # Calculates the constant to find the time for each n
    start_time = time.perf_counter()
    fib(39)
    end_time = time.perf_counter()
    c = (end_time - start_time)/(1.618**39)

    c_array = []
    print("The next lines will compare the actual times of fib(35) - fib(39) with a calculated value of c*1.618^n")   
    for i in range(35, 40):
        start_time = time.perf_counter()
        fib(i)
        end_time = time.perf_counter()
        print(f"Theoretical time: {(c * 1.618**i):.2e}s, Actual time: {(end_time - start_time):.2e}s")
        c_array.append((end_time - start_time)/(1.618**i))
    c_mean = sum(c_array)/len(c_array)
    print(f"The avarage c value for my computer for n = 35 - 39 is {(c_mean):.2e} which results in the time function t(n) = {(c_mean):.2e}*1.618^n")
    print(f"This results in a calculated time for fib(50) = {c_mean*1.618**50/(60):.2f} minutes, and fib(100) = {c_mean*1.618**100/(365*24*3600*10**6):.2f}*10^6 years")
    print('\n\nCode for analysing fib_mem\n')
    
    start_time = time.perf_counter()
    print(f"fubonachi number 100: {fib_mem(100)}")
    end_time = time.perf_counter()
    print(f"The total time for fib_mem(100) = {end_time - start_time:.3e} seconds")
    print('\nBye!')
    


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
  
    I should assume each tile takes 1 second to move. This means that t(n) = h(n) = 2^n - 1 which means that the
    total time for 50 tiles would be (2^50 + 1)/(365*24*3600) = 35.70 * 10^6 years

  
  
  Exercise 9: Time for Fibonacci:
    The t(n) function for my stationary computer is ~(7.67*10^-8)*1.618^n. 
    This results in:
    t(50) = 35.96 minutes
    fib(100) = 1.92*10^6 years

  
  
  Exercise 10: Time for fib_mem:
    fubonachi number 100: 354224848179261915075
    The total time for fib_mem(100) = 4.810e-05 seconds
  
  
  Exercise 11: Comparison sorting methods:
  Both functions takes 1 second for 1000 random numbers.
  
  Insertion sort: 
    
  The time fucntion is given by:
  t(n) = c_insert * n^2
  t(1000) = 1 = c_insert * 10^6 ==>  c_insert = 10^-6
  this means that:
  
  t(10^6) = 10^-6 * 10^12 = 10^6 seconds = 11.57 days
  t(10^9) = 10^-6 * 10^18 = 10^12 seconds = 31.71 * 10^3 years
  
  Merge sort:
    The time fucntion is given by:
    t(n) = c_merge * n * log(n)
    t(1000) = 1 = c_insert * 1000 * log(1000) ==>  c_insert = 1/3*10^-3
    this means that:
    
    t(10^6) = 1/3*10^-3 * 6*10^6 = 2*10^3 seconds = 33.33 minutes
    t(10^9) = 1/3*10^-3 * 9*10^9 = 3*10^6 seconds = 34.72 days
  
  
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
  t_A(n) = n
  t_B(n) = c* n log(n),    t_B(10) = 1  ==>  c = 1/(10*1) = 1/10,
  t_B(n) = 1/10 * n log(n)
  
  To find the n which A takes less time we need to solve t_A(n) < t_B(n)
  ==>   n < 1/10 n log(n)  ==>  log(n) > 10  ==>  n  >  10^10                       
  
"""
