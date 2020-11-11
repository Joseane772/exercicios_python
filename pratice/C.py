moxit = 0
for n in range(10, 12):
    maxi = 0
    for x in range(1, 2):
        name = str(input('what is the name of the student?:'))
        nl = int(input('How many books did it read?:'))
        if nl > maxi:
            maxi = nl
            name = name
    if maxi > moxit:
        moxit = maxi

print('The student the read more books was:', name,
      '\nThe  month whit more books read is :', moxit)
