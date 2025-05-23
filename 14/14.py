import time


limit: int = 1_000_000
maximum: int = 1

start_t = time.perf_counter()
for number in range(limit, 1, -1):
    test_number = number

    count: int = 1
    while test_number != 1:
        if test_number % 2 == 0:
            test_number //= 2
        else:
            test_number = 3 * test_number + 1

        count += 1

    if maximum < count:
        maximum = count
        answer = number

end_t = time.perf_counter()
print(answer)
print("number of items in the sequence:", maximum)
print(f'{end_t-start_t:.3f}')
