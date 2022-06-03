lista=[]
i=0
n=int(input())
x=n
def fibonacci(n):  
   if n == 1 or n == 0:
       return (1)
       
       
   else:   
       return 1 +(fibonacci(n-1) + fibonacci(n-2))
def Fibo(n):
    if n<=1:   
        return (n)
       
       
    else:
       
        return (Fibo(n-1) + Fibo(n-2))
    

chamadas= (fibonacci(n))
fibo= Fibo(x)
print(f'Fib({n})= {fibo} ({chamadas} chamadas)')

 
 
