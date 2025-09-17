num_main = int(input("Enter number : "))

num_1 = 0

while num_1 < 13 :
    result = num_main * num_1
    print((str(num_main)) + " x " + (str(num_1)) + " = " + str(result))
    num_1 += 1
    
    if num_1 > 12 :
        exit
