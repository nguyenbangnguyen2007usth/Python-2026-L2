"""
# --- Exercise 1: Area of a circle ---
radius = float(input("Enter circle radius? "))
area = 3.14 * (radius ** 2)
print(f"Circle area = {area}")

# --- Exercise 2: Celsius to Fahrenheit ---
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = (celsius * 9/5) + 32
print(f"{int(celsius)} (C) = {fahrenheit} (F)")

# --- Exercise 3: Prime number check ---
num = int(input("Enter a number? "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is a NOT prime number")

# --- Exercise 4: Perfect number check ---
num = int(input("Enter a number? "))
sum_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num and num > 0:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is a NOT perfect number")

# --- Exercise 5: Favorite color ---
colors = ["Blue", "Yellow", "Black", "Red", "White"]
color = input("What is your favorite color? ")

if color in colors:
    index = colors.index(color)
    print(f"Your color is at index {index} in my list")
else:
    print("Sorry, I could not find your color")

# --- Exercise 6: range() sequences ---
range1 = list(range(7))
range2 = list(range(1, 11, 3))
range3 = list(range(5, 0, -1))
range4 = list(range(6, -3, -2))

print(f"range1 {range1}")
print(f"range2 {range2}")
print(f"range3 {range3}")
print(f"range4 {range4}")

# --- Exercise 7: Remove dollar sign ---
def remove_dollar_sign(s):
    return s.replace("$", "")

# --- Exercise 8: Extract even items ---
def extract_even(l):
    even_list = []
    for num in l:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# --- Exercise 9: Factorial ---
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# --- Exercise 10: Get all divisors ---
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# --- Exercise 11: Compute distance ---
import math

def compute_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# --- Exercise 12: Print m x n hollow pattern ---
def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
"""
