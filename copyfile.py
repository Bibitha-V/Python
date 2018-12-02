f=open(r"E:\python\pplclick\pycharm\temp\simple.txt",'r')
f1=open("F:\Assignment\copy.txt",'w')
for x in f.readlines():
    f1.write(x)
f.close()
f1.close()
