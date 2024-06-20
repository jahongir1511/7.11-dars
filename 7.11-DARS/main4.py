#    misol linli   https://www.codewars.com/kata/58029cc9af749f80e3001e34/train/python


def get_new_notes(salary, bills):
    total_bills = sum(bills)

    disposable_income = salary - total_bills

    if disposable_income < 5:
        return 0
    else:
        return disposable_income // 5


print(get_new_notes(1000, [300, 150, 200]))
print(get_new_notes(500, [100, 100, 300]))
print(get_new_notes(50, [30, 10]))
print(get_new_notes(25, [10, 5]))
print(get_new_notes(15, [5, 5, 5]))
