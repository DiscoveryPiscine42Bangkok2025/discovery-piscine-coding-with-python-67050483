import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    your_word = input("What was the parameter? : ")

    if your_word != param:
        print("Nope, sorry...")
    else:
        print("Good job!")
