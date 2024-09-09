def is_armstrong(num):
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))
def find_armstrong(start, end):
    for num in range(start, end + 1):
        if is_armstrong(num):
            print(num, end=" ")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
find_armstrong(start, end)
