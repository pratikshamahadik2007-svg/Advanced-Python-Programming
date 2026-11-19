import threading
import time

def count_numbers(n):
    for i in range(1, n + 1):
        print(f"Count: {i}")
        time.sleep(0.5)

def calculate_square(numbers):
    for n in numbers:
        print(f"Square of {n}: {n * n}")
        time.sleep(0.5)

def calculate_cube(numbers):
    for n in numbers:
        print(f"Cube of {n}: {n * n * n}")
        time.sleep(0.5)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    # Creating threads for each task
    t1 = threading.Thread(target=count_numbers, args=(5,))
    t2 = threading.Thread(target=calculate_square, args=(nums,))
    t3 = threading.Thread(target=calculate_cube, args=(nums,))

    # Starting the threads
    t1.start()
    t2.start()
    t3.start()

    # Waiting for all threads to complete
    t1.join()
    t2.join()
    t3.join()

    print("All threads have finished execution.")