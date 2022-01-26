#ques6_To check if a triangle can be formed by given three lengths entered by the user
a=int(input('side a:'))
b=int(input('side b:'))
c=int(input('side c:'))
outcome='No'
if (a+b>c) & (b+c>a) & (c+a>b):
    outcome='Yes'
print(outcome)


