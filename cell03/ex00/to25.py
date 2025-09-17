num = int(input("Enter a number less than 25 : "))

if num >= 25 :
    print("Error")

while num < 26 :
    print("Inside the loop, my variable is " + str(num))
    num +=1
    if num >= 25 :
        exit
