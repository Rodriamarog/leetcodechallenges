def sum_even_numbers(listnums):
    sum = 0
    for number in listnums:
        if number % 2 == 0:
            sum += number 
    return sum 

listnums = []
for i in range(5):
    listnums.append(int(input("Tell me a number: ")))

print(sum_even_numbers(listnums))