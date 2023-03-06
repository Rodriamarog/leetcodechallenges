def romanToInt(self, s: str) -> int:
    romans_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

    result = 0
    prev_value = 0

    for letter in s:
        curr_value = romans_dict[letter]

        if curr_value > prev_value:
            result -= prev_value
        else:
            result += prev_value

        prev_value = curr_value

    result += prev_value

    return result