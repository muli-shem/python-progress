#Question 1: FizzBuzz
for num in range(1,101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#Question 2: Fibonacci Sequence
def fabonacci(limit):
     a, b = 0, 1
     while a< limit:
        print(a, end=" ")
        a, b = b ,a + b
fabonacci(100)

#uestion 3: Power of Two

def is_power_of_two(num):
    return num>0 and(num & (num-1))==0
print(is_power_of_two(8))
print(is_power_of_two(6))

#Question 4: Capitalize Words

def capitalize_words(text):
    return text.title()
print(capitalize_words("hi"))
print(capitalize_words("i love programing"))

#Question 5: Reverse Integer

def reverse_integer(num):
    sign = -1 if num <0 else 1
    num = abs(num)
    reversed_num = 0
    while num >0:
        reversed_num = (reversed_num*10)+(num % 10)
        num //= 10
    return sign * reversed_num
print(reverse_integer(12345))
print(reverse_integer(55003434))
print(reverse_integer(4544203))

#Question  6: Count Vowels

def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    for char in text:
        vowels_count +=1
    return vowels_count

print(count_vowels("Hello World"))
