#ques4_To find the greatest of three numbers entered by the user
x=int(input('enter first no:'))
y=int(input('enter second no:'))
z=int(input('enter third no:'))
largest=x
for i in[x,y,z]:
    if largest<i:
        largest=i
print('largest no is:',largest)
    
