def sum_of_natural(n):
    return n * (n + 1) // 2
num = int(input("Enter a number: "))
print(f"Sum of natural numbers up to {num} is {sum_of_natural(num)}")
