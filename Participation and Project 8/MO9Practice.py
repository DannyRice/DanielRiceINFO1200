import random


def main():
    # create list
    nums = [1, 3, 23, 1, 7, 7, 19, 0]
    print(nums)
    print("----------------------")

    # add to list
    nums.append(11)
    print(nums)
    print("----------------------")

    nums.insert(2, 43.1)
    print(nums)
    print("----------------------")

    num = nums[-1]
    print(num)
    print(nums)
    num1 = nums.pop()
    print(num1)
    print(nums)
    print("----------------------")

    if 7 in nums:
        nums.remove(7)
    print(nums)
    print("----------------------")

    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    print("Total: ", total)
    print(f"Average: {total / len(nums)}")
    print("----------------------")

    total = 0
    for num in nums:
        total += num
    print(total)
    print("----------------------")

    newnumber = 99
    add_to_list(newnumber, nums)
    print(newnumber)
    print(nums)
    print("----------------------")

    nums.sort()
    print(nums)
    print("----------------------")

    random.shuffle(nums)
    print(nums)
    print("----------------------")

    randnum = random.choice(nums)
    print(randnum)
    print("----------------------")


def add_to_list(newnum, allnums):
    newnum = 100
    print(newnum)
    allnums.append(newnum)
    print(allnums)


if __name__ == "__main__":
    main()
