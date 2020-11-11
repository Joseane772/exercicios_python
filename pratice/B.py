na = int(input('what is the total number of students?'))
NV = 0
Lx = 0
Lz = 0
EB = 0
EM = 0
Vb = 0

for n in range(0, na):
    v = str(input('which list will you vote for(X or Z)'))
    NE = str(input('what is your level of education (B or S)?'))
    if v == 'x':
        Lx = Lx + 1
    elif v == 'z':
        Lz = Lz + 1
    else:
        Vb = Vb + 1
    if NE == 'b':
        EB = EB + 1
    else:
        EM = EM + 1
nv = str(na)
lx = str(Lx)
lz = str(Lz)
eb = str(EB)
em = str(EM)
vb = str(Vb)

print('\nNumber of votes(total):' + nv +
      '\nNumber of votes(list X):' + lx +
      '\nNumber of votes(list Z):' + lz +
      '\nNumber of votes(null):' + vb +
      '\nNumber of votes(highschoolers):' + em +
      '\nNumber of votes(preschoolers):' + eb)
if Lx > Lz:
    print('The winner is X')
elif Lz < Lx:
    print('The winner is Z')