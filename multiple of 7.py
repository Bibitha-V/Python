num=eval(input("enter a number"))

if(not isinstance(num,int)):
    print("wrong input")
else:
    if(num % 7==0):
        print("the entered number is multiple of 7")

    else:
        print("num is not a multiple ")
