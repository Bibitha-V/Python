print("Program for Simple Interest")
principle =eval(input("Enter the principle"))
rate = eval(input("Enter the rate"))
time = eval(input("Enter the time"))

if(rate == 0):
    print("Simple Interest is Zero")
else:
    simple_iterest = (principle*time*rate)/100
    print(simple_interest)
