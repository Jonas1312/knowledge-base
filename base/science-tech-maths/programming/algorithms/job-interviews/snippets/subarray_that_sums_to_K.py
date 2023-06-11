# find continous subarray that sums to K


# linear in time
# 1 in space
# only works for positive integers
def algo_1(input_array, K):
    begin = end = 0
    sum_ = 0
    while True:
        if sum_ == K:  # found match, we print and increase begin
            print(input_array[begin:end])
            sum_ -= input_array[begin]
            begin += 1
        elif sum_ < K:
            if end == len(
                input_array
            ):  # if end pointer can't move forward and sum_ too small, we're done
                break
            sum_ += input_array[end]
            end += 1
        elif sum_ > K:
            sum_ -= input_array[begin]
            begin += 1


# linear in time and space
# sum(i, j) = sum(0, j) - sum(0, i)
def algo_2(input_array, K):
    sums_dict = dict()
    sum_ = 0

    for i, x in enumerate(input_array):
        sum_ += x
        sums_dict[sum_] = i

        if sum_ - K in sums_dict.keys():
            begin = sums_dict[sum_ - K] + 1
            end = i + 1
            print(input_array[begin:end])


def main():
    algo_1([2, 6, 0, 9, 7, 3, 1, 4, 1, 10], K=15)  # {6, 0, 9}, {7, 3, 1, 4}, {4, 1, 10}
    print("-" * 50)
    algo_2([2, 6, 0, 9, 7, 3, 1, 4, 1, 10], K=15)  # {6, 0, 9}, {7, 3, 1, 4}, {4, 1, 10}
    print("-" * 50)
    algo_2(
        [0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10], K=15
    )  # {1, -4, 7, 6, 1, 4} or {4, 1, 10}
    print("-" * 50)
    algo_2([0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10], K=-3)  # {1, -4}


if __name__ == "__main__":
    main()
