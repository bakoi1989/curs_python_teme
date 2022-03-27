# Tema 2 - 27.03.2022

# Ex.1 Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
# numere întregi sau reale

# your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3)

def my_function (a, b, c, d, e):
    print(a + b + c)


my_function(1, 5, -3, 'abc', [12, 56, 'cad'])

# your_function() va returna 0.

def my_function_2(a):
    print(a - a)


my_function_2(5)

# your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4)

def my_function_3 (a ,b, c, param_1=2):
    print(a + b)


my_function_3(2 , 4, 'abc')


# Ex.2 Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:

#  suma tuturor numerelor de la [0, n]

def suma_numerelor(n):
    if n == 0:
        return 0

    return n + suma_numerelor (n-1)


suma = suma_numerelor(11)
print(suma)

# suma numerelor pare de la [0, n]

def suma_numerelor_pare(n):
    if n == 0:
       return 0


    return n + suma_numerelor_pare (n-1)


suma_pare = suma_numerelor_pare(6)
print(suma_pare)

# # suma numerelor impare de la [0. n]
#
# def suma_numerelor_impare(n):
#     if n == 0:
#         if n // 2 != 0:
#            return 0
#
#
#     return n + suma_numerelor_impare (n-1)
#
#
# suma_impare = suma_numerelor_impare(6)
# print(suma_impare)
#
# # Ex.3 Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează
# # valoarea 0

numar_introdus = input('Alege un numar: ')
try:
    numar_introdus = int(numar_introdus)
    print(f'Numarul tau ales este: {numar_introdus}')
except numar_introdus != int(numar_introdus):
     print('0')
