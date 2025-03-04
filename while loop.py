# Example1
'''
count=1
while count <=5:
    print(count)
    count+=1


#example2
i=0
num=0
while num<=10:
    print(i)
    i+=1
    num+=1


# example3

a=0
while a<=50:
    print("even mumners of 50:",(a))
    a+=2


# example4
number=10
factorial=1
while number >0:
    factorial*=number
    number-=1
    print("the factorial of 10 is",(factorial))


# eaxmple 5

num=1
while num<11:
    print(f"5 X {num} = {5*num}")
    num+=1

# example 6

a, b = 0, 1
while a <= 100:
    print(a)
    a, b = b, a + b
'''
# example 7
num = int(input("Enter a number to count its digits: "))
count_digits = 0
while num > 0:
    count_digits += 1
    num //= 10
print("Number of digits:", count_digits)

#example8
num = 2
while num <= 20:
    is_prime = True
    div = 2
    while div <= num // 2:
        if num % div == 0:
            is_prime = False
            break
        div += 1
    if is_prime:
        print(num)
    num += 1

#exmaple9
num = int(input("Enter a number to check if it's a palindrome: "))
original_num = num
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
if original_num == reverse_num:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

#example10
num = int(input("Enter a number to calculate the sum of its digits: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print("Sum of digits:", sum_digits)


