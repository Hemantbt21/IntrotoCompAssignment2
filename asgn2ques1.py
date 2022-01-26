#ques1_take input string"Python is a case sensitive language"

x=str(input('Enter string:'))

#a_Length of input string

print('string length =',len(x))

#b_reverse the order of the string

z=x[::-1]
print('string reversed =',z)

#c_Using slice function to store "a case sensitive" in new string

y=x[10:27]
print('sliced string=',y)

#d_

m=x.replace('a case sensitive','object oriented')
print('string replaced =',m)

#e_index of 'a' in input string

n=x.index('a')
print('index of a =',n)

#f

p=x.replace(' ','')
print('white_spaces_removed =',p)


