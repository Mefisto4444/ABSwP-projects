
def high_and_low(numbers):
    number_lst = []
    for number in numbers.split(" "):
        number_lst.append(int(number))
    numbers = f"{max(number_lst)} {min(number_lst)}"
    return numbers
print(high_and_low("1 2 -3 4 5"))