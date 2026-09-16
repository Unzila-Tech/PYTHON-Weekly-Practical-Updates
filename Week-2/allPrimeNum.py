startNum=int(input("Enter first number: "))
endNum=int(input("Enter a ending number: "))

print("All prime number in range",startNum,"to",endNum)
for num in range(startNum,endNum+1):
    if num<2:
       continue
    prime= True
    
    for i in range(2,num):
        if num%i==0:
             prime =False
             break
    if prime:
        print(num)
       