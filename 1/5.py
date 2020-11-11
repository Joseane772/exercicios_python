import random
p= str(input ('aluno1:'))
s= str(input ('aluno2:'))
t= str(input ('aluno3:'))
c= str(input ('aluno4:'))
l= [p,s,t,c]
random.shuffle(l)
print('a ordem é:')
print(l)
