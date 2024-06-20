#    misol linli  https://www.codewars.com/kata/55466644b5d240d1d70000ba/train/python


def candies(candies_list):
    if len(candies_list) <= 1:
        return -1

    max_candies = max(candies_list)
    total_candies_given = sum(max_candies - candy for candy in candies_list)

    return total_candies_given


print(candies([5, 8, 6, 4]))
print(candies([1, 2, 4, 6]))
print(candies([1, 6]))
print(candies([]))
print(candies([6]))