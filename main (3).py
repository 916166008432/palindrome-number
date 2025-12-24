def reverse(n):
    a=n
    out=0
    while n>0:
        rem=n%10
        out=out*10+rem
        n=n//10
    if a==out:
        return ("palindrome number")
    else:
        return("not palindrome number")
n=int(input("enter the number:"))
print(reverse(n))
        