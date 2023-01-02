def is_capitalized(word):
    if word.islower():
        return True
    elif word.isupper():
        return True
    elif word.istitle():
        return True
    else:
        return False

# Test the function
print(is_capitalized('Hello')) # True
print(is_capitalized('hello')) # True
print(is_capitalized('HELLO')) # True
print(is_capitalized('HeLLo')) # False
