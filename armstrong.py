n= int(input("Enter a number"))
sum= 0
temp= n
while temp>0:
    digit= temp%10
    sum= sum+digit**3
    temp= temp//10
if n==sum:
    print("The number is armstrong")
else:
    print("The number is not armstrong")