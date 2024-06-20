#    misol linli      https://www.codewars.com/kata/5899e054aa1498da6b0000cc/train/python


def reverse_invert(array):
    def reverse_and_invert(num):
        reversed_num = int(str(abs(num))[::-1])
        return -reversed_num if num > 0 else reversed_num

    return [reverse_and_invert(x) for x in array if isinstance(x, int)]

result = reverse_invert([1, 12, 'a', 3.4, 87, 99.9, -42, 50, 5.6])
print(result)
