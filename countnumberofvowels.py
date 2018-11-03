s1=['a','e','i','o','u']
sum = 0
s2=input("enter the string")
sum=sum+s2.count(s1[0])
sum=sum+s2.count(s1[1])
sum=sum+s2.count(s1[2])
sum=sum+s2.count(s1[3])
sum=sum+s2.count(s1[4])

print("the number of vowels is",sum)
