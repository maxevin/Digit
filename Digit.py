def digitAwal(a,b):
    pangkat = a**b

    # convert variable 'pangkat' from integer to string
    result = str(pangkat)

    # use 'string slicing' method to take the first character only
    return result[:1]

def digitAkhir(a,b):
    pangkat = a**b

    # convert variable 'pangkat' from integer to string
    result = str(pangkat)

    # use 'string slicing' method to take the last character only
    return result[-1]

print('Output dari Function \'digitAwal\' :')
print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))
print('')
print('Output dari Function \'digitAkhir\' :')
print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))