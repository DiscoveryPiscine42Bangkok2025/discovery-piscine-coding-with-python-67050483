num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter Second number : "))

result = num_1 * num_2

print(str(num_1) + " x " + str(num_2) + " = " + str(result))

if result > 0 :
    print("the result is positive")
elif result == 0 : 
    print("the result is positive and negative")
else :
    print("the result is negative")
