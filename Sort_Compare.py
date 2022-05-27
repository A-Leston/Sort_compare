import random
import time


def selection_sort(a_list):
  for fill_slot in range(len(a_list) - 1, 0, -1):
     pos_of_max = 0
     for location in range(1, fill_slot + 1):
        if a_list[location] > a_list[pos_of_max]:
           pos_of_max = location
     temp = a_list[fill_slot]
     a_list[fill_slot] = a_list[pos_of_max]
     a_list[pos_of_max] = temp


def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp


def merge_sort(a_list):
    #print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0
        j=0
        k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i=i+1
            else:
                a_list[k] = right_half[j]
                j=j+1
            k=k+1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j=j+1
            k=k+1


def main():
    overall_limit = 120                 # 120 sec limit for each search method
    limit = 60                          # 60 sec limit for each search

    n = 10000
    runtime = 0
    overall_time = 0
    while runtime < limit and overall_time < overall_limit:  # while each search takes less than
        my_list = []                                         # 60 sec individually or 120 sec cumulatively
        for i in range(n):
            x = random.randint(1, 99)   # creating random data set
            my_list.append(x)
        start = time.time()
        selection_sort(my_list)         # running select sort and getting time
        end = time.time()
        runtime = (end - start)         # getting time for each search
        print(str(n) + " values using selection sort: " + str(runtime) + " seconds")
        overall_time += runtime         # keep track of total runtime for loop
        n += 10000                      # increment n so next test larger

    print("-------------------")        # resetting values for next test
    n = 10000
    runtime = 0
    overall_time = 0
    while runtime < limit and overall_time < overall_limit:
        my_list = []
        for i in range(n):
            x = random.randint(1, 99)
            my_list.append(x)
        start = time.time()
        bubble_sort(my_list)
        end = time.time()
        runtime = (end - start)
        print(str(n) + " values using bubble sort: " + str(runtime) + " seconds")
        overall_time += runtime
        n += 10000

    print("-------------------")        # resetting values for next test
    n = 10000
    runtime = 0
    overall_time = 0
    while runtime < limit and overall_time < 10:   # overrode the hard limit of 120 sec because it ran super fast
        my_list = []
        for i in range(n):
            x = random.randint(1, 99)
            my_list.append(x)
        start = time.time()
        merge_sort(my_list)
        end = time.time()
        runtime = (end - start)
        print(str(n) + " values using merge sort: " + str(runtime) + " seconds")
        overall_time += runtime
        n += 10000


if __name__ == "__main__":
    main()
