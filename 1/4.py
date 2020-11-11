import random
p= str(input ('aluno1:'))
t= str(input ('aluno2:'))
s= str(input ('aluno3:'))
d= str(input ('aluno4:'))
l= [p,t,s,d]
e= random.choice(l)
print('e o escolhido da ves é: {}'.format(e))
