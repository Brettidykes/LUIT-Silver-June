input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)


