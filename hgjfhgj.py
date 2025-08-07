n1 = int(input('число 1'))
n2 = int(input('число 2'))
orif = input('действие')


def kalkulitir(n1, n2, orif):
    if orif == '+':
        result = n1 + n2
        return result
    elif  orif == '-':
        result = n1 - n2
        return result
    elif  orif == '/':
        result = n1 / n2
        return result
    elif  orif == '*':
        result = n1 * n2
        return result
    
kalkulatar = kalkulitir(n1, n2, orif)
print(kalkulatar)
