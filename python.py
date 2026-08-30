#   ques 1
no=int(input("entr the number"))

if no % 2!=0:
    print("odd")
elif no >=2 and no <=5:
    print("not weird..!")
elif no >=6 and no <= 20:
    print("more weird..!")
else:
    print("more and more weird..!")

    # question 2

a = int(input())
b = int(input())
    
print(a+b)
print(a-b)
print(a*b)

    # question 3
a = int(input())
b = int(input())
    
print(a//b) 
print(a/b)

# ques 4

n = int(input())
    
for i in range(n):
    print(i**2)

#  ques 5

yr=int(input())


def is_leap(yr):
   if yr % 400 == 0:
    return True
   elif yr % 100 == 0:
    return False
   elif yr % 4 == 0:
     return True
   else:
     return False

print(is_leap(yr))


# ques 6

no=int(input())
for i in range(1,no+1):

    print(i,end="")
