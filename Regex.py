import re

# Patrones

# Caracteres especiales
# .     coincide cualquier caracter
# ^     coincide con el inicio del string
# $     coincide con el final del string
# *     coincide con 0 o mas caracteres
# +     coincide con 1 o mas caracteres
# ?     coincide 0 o 1 carater
# {m}   coincide m caracteres
# {m,n} coincide entre m y n caracteres
# \  caracteres especiales
# [] cpnjunto de caracteres
# (...) captura un grupo

# Metodos
# match, puede imitar a search indicandole en el patron
patron = '[0-9]+$'
result = re.match(patron, '146068123223234')

if result:
    print(result)
    print(result.string)

patron2 = '[0-9]{10}'
result = re.match(patron2, '65421411432')

if result:
    print(result)
    print(result.string)

patron3 = '[0-9]{10}$'
result = re.match(patron3, '3655625676')

if result:
    print(result)
    print(result.string)



a = '3'
b = 5
patron4 = '[0-9]*$'
ra = re.match(patron4, str(a))
rb = re.match(patron4, str(b))

if ra and rb:
    print((int(a)+int(b)))
else:
    print("error con los numero ingresados")





# metodo Search
# buscara en cualquier parte del texto

result = re.search(patron2, '54643564356')

if result:
    print(result)
    print(result.string)

# No contendra letras
patron = '[^a-zA-Z]'
print("No letras: ", True if re.match(patron, "sudhf3424") else False)
print("No letras: ", True if re.match(patron, "3452345") else False)
print("No letras: ", True if re.match(patron, "fdhsdfh") else False)

# solo numeros
patron = '[0-9]+$'
# patron = '\d+$'
print("solo numeros: ", True if re.match(patron, "sudhf3424") else False)
print("solo numeros: ", True if re.match(patron, "3452345") else False)
print("solo numeros: ", True if re.match(patron, "2435$546") else False)

# Solo maysculas
patron = '[A-Z]+$'
print("Solo maysculas: ", True if re.match(patron, "SDFGSH") else False)
print("Solo maysculas: ", True if re.match(patron, "SHSFDHs") else False)
print("Solo maysculas: ", True if re.match(patron, "SFGHSGH!") else False)

# no numeros
patron = '[^0-9]'
# patron = '[^0-9]$' si se quiere que en toda la cadena no existan numeros
print("no numeros: ", True if re.match(patron, "4363a") else False)
print("no numeros: ", True if re.match(patron, "gfh456sdfg") else False)
print("no numeros: ", True if re.match(patron, "SFGHSGH!") else False)


# findall
# regresa una lista con todas las coincidencias

f = open('C:/Users/JMaya/PycharmProjects/untitled2/ejemplo/file.txt')
file = f.read()
print(file)
f.close()

patron = '[Pp]ython'
# patron = '[Tt]he'

fa = re.findall(patron, file)
print(len(fa))

# split
# una lista donde el string se divide por coincidencias
f = open('C:/Users/JMaya/PycharmProjects/untitled2/ejemplo/file.txt')
file = f.read()
print(file)
f.close()

s = re.sub('[PYTHONpython]', '<<PYTHON>>', file)
f = open('PYTHON.txt', 'w')
f.write(s)
# sub
# reemplaza una o mas coincidencias
