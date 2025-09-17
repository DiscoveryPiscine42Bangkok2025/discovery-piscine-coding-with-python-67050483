age = int(input("Please tell me your age : "))

print("You are currently " + str(age) + " years old.")

for i in range (1,4) :
    print("In " + str(i*10) +  " years, you'll be " + str(age + 10) + " years old.")
    age += 10 
