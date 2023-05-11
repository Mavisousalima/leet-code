def fizzBuzz(n: int):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result


assert fizzBuzz(3) == [1, 2, "Fizz"]
assert fizzBuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
assert fizzBuzz(15) == [1, 2, "Fizz", 4, "Buzz", "Fizz",
                        7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
