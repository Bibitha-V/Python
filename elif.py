num=eval(input("enter a number"))
multiplier=eval(input("enter the multiplier"))

if(num>50):
    print("number is greater than 50")

elif(num%multiplier==0):
    print("the num",num,"is a mutiple of number",multiplier)

else:
    print("the num",num,"is not a mutiple of number",multiplier)