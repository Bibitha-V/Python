num=eval(input("enter the number"))
if(isinstance(num,int)):
    for i in range(0,num,2):
        if(not i%3==0):
            print(i)