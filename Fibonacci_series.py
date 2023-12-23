n=int(input("How many numbers for Fibonacci series: "))

f=[0]*n
f[0]=0
f[1]=1

for i in range(2,n,1):
    f[i]=f[i-1]+f[i-2]

print("Fibonacci series is \n", f)