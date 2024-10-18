"""
Solutions to module VA 4

Student: Alexander Hedene
Mail: Correct file
"""
#!/usr/bin/env python3

from person import Person
import time as t
import matplotlib.pyplot as plt
"""
Write a script that gives a plot for comparison of two approaches for Fibonacci numbers
"""
def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)


def main():
	f = Person(50)
	py_lst = []
	age_lst_py = [i for i in range(10, 40, 1)]

	for age in age_lst_py:
		start_time_py = t.perf_counter()
		fib_py(age)
		end_time_py = t.perf_counter()
		py_lst.append(end_time_py - start_time_py)


	Cpp_lst = []
	age_lst_Cpp = [i for i in range(10, 48, 1)]
	for age in age_lst_Cpp:
		f.setAge(age)
		start_time_cpp = t.perf_counter()
		print(f.fib())
		end_time_cpp = t.perf_counter()
		Cpp_lst.append(end_time_cpp - start_time_cpp)


	plt.scatter(age_lst_py, py_lst, label="Python Time")
	plt.scatter(age_lst_Cpp, Cpp_lst, label="Cpp Time")
	plt.xlabel("Number n")
	plt.ylabel("Time [s]")
	#plt.savefig("Fib_Cpp_vs_Py")
	plt.show()
	print("From the graph it can be shown how both follow tge same O(2^n) but they have different c values. The C value for C is approximatly 10-20 times smaller thanthe c value for python.")
	print(f"Time for 47{Cpp_lst[47]}")
if __name__ == '__main__':
	main()


"""What is the result for Fibonacci with n=47? Why?
	The result for n = 47 is negative. This is because we are using int32 type. fib(47) is above this limits which makes the integer negative instead.
	A solution would be to use int64 instead. 
"""
