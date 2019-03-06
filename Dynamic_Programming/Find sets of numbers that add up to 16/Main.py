from Functions import rcc_without_dyamic_programming, rcc_with_dyamic_programming
import time
import random
mem = {}
list_len = 100
list_value = 230
list = random.sample(range(1, list_value), list_len)
list.sort()
sum = 200
print(list)
# With dynamic programming
start = time.time()
result_with_dynamic_programming = rcc_with_dyamic_programming(list, sum, len(list), mem)
end = time.time()
time_with = end - start
print("Number of sets(with dynamic programming):", result_with_dynamic_programming)
print("Time(with dynamic programming):", time_with)
print("**************")

# Without dynamic programming
start = time.time()
result_without_dynamic_programming = rcc_without_dyamic_programming(list, sum, len(list))
end = time.time()
time_without = end - start
print("Number of sets(without dynamic programming):", result_without_dynamic_programming)
print("Time(without dynamic programming):", time_without)
print("**************")

# Improvement
print("improvment:", time_with - time_without)