number1 = int(input("введите первое число:"))
number2 = int(input("введите второе число:"))
number3 = int(input("введите третье число:"))
print(number1+number2+number3)
print(number1*number2*number3)


dlina1 = int(input("введите первую длину ромба:"))
dlina2 = int(input("введите вторую длину ромба:"))
print((dlina1 * dlina2) / 2)

num = int(input("введите четырёхзначное число: "))

digit1 = num // 1000
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10
digit4 = num % 10

product = digit1 * digit2 * digit3 * digit4
print("Произведение цифр:", product)



