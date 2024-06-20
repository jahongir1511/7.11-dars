#    misol linli  https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a/train/python


def replace_all(array, old, new):
    if isinstance(array, list):
        return [new if item == old else item for item in array]
    elif isinstance(array, str):
        return array.replace(old, new)
    else:
        raise TypeError("Expected list or string input")

if __name__ == "__main__":
    array1 = [1, 2, 2]
    old_value = 1
    new_value = 2
    result_list = replace_all(array1, old_value, new_value)
    print(f"List example: {result_list}")

    string1 = "hello world"
    old_char = 'o'
    new_char = '0'
    result_string = replace_all(string1, old_char, new_char)
    print(f"String example: {result_string}")
