# -*- coding: utf-8 -*-
"""Cópia de PythonBasico_ListaRevisao_ProgWeb_Resolvidas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m3ZZKeDB-T5FdtIQiBS2Gn_SEqVtnbga

# Primeiro trimestre - Revisão Python


Exercícios para treinar sintaxe e uso básico da linguagem Python.
Os exercícios desta lista são auto-corrigíveis.

## Lista 1 - Variáveis e inicialização de listas e dicionários

### exercicio 1

Na linha abaixo, crie uma variável chamada **on_mars_right_now** e atribua a ela o valor booleano **False**
"""

on_mars_right_now = False

assert on_mars_right_now == False, "Se você ver um 'Name Error', certifique-se de criar a variável e atribuir um valor."
print("Exercício 1 está correto.")

"""### Exercício 2

Crie uma variável chamada **fruits** e atribua a ela uma lista de frutas contendo os seguintes nomes de frutas como strings:
**manga, banana, goiaba, kiwi e morango.**
"""

fruits = ["manga", "banana", "goiaba", "kiwi", "morango"]

assert fruits == ["manga", "banana", "goiaba", "kiwi", "morango"], "Se você ver um erro de assert, verifique se a variável contém todas as strings na ordem fornecida"
print("Exercício 2 está correto.")

"""### exercicio 3

Crie uma variável chamada **vegetables** e atribua a ela uma lista de vegetais contendo os seguintes nomes de vegetais como strings:
**berinjela, brócolis, cenoura, couve-flor e abobrinha**
"""

vegetables = ["berinjela", "brócolis", "cenoura", "couve-flor", "abobrinha"]

assert vegetables == ["berinjela", "brócolis", "cenoura", "couve-flor", "abobrinha"], "Certifique-se de que a variável contenha todas as strings na ordem fornecida"
print("Exercício 3 está correto.")

"""### exercicio 4

Crie uma variável chamada **numbers** e atribua a ela uma lista de números: **1, 2, 3, 4, 5, 6, 7, 8, 9, 10**
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


assert numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Certifique-se de que a variável contenha os números de 1 a 10 na ordem."
print("Exercício 4 está correto.")

"""### exercicio 5

Dada a seguinte atribuição da lista de frutas, adicione **"tomate"** ao final da lista.
"""

fruits.append("tomate")

assert fruits == ["manga", "banana", "goiaba", "kiwi", "morango", "tomate"], "Certifique-se de que a variável contenha todas as strings na ordem correta"
print("Exercício 5 está correto")

"""### exercicio 6

Dada a seguinte atribuição da lista de vegetais, adicione **"tomate"** ao final da lista.
"""

vegetables.append("tomate")

assert vegetables == ["berinjela", "brócolis", "cenoura", "couve-flor", "abobrinha", "tomate"], "Certifique-se de que a variável contenha todas as strings na ordem fornecida"
print("Exercício 6 está correto")

"""### exercicio 7

Dada a lista de números definida abaixo, **inverta a lista** de números que você criou acima.
"""



assert numbers == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "O erro de assert significa que a resposta está incorreta."
print("Exercício 7 está correto.")

"""### exercicio 8

**Ordene** os vegetais em ordem alfabética
"""



assert vegetables == ['abobrinha', 'berinjela', 'brócolis', 'cenoura', 'couve-flor', 'tomate']
print("Exercício 8 está correto.")

"""### exercicio 9

Escreva o código necessário para **classificar** as frutas em ordem alfabética inversa
"""



assert fruits == ['tomate', 'morango', 'manga', 'kiwi', 'goiaba', 'banana']
print("Exercício 9 está correto.")

"""### exercicio 10

Escreva o código necessário para produzir uma única lista que contenha todas as frutas e depois todos os vegetais na ordem em que foram classificados acima.
"""



assert fruits_and_veggies == ['tomate', 'morango', 'manga', 'kiwi', 'goiaba', 'banana', 'abobrinha', 'berinjela', 'brócolis', 'cenoura', 'couve-flor', 'tomate']
print("Exercício 10 está correto")

"""## Lista 2 - Funções e operações numéricas

### Utilitarios

alguns utilitarios disponibilizados pelo professor e adaptado por mim para seguir minha necessidade e logica
"""

import random

par_positivo = random.randrange(2,101,2)
print("O número randomico par e positivo é: ", par_positivo)

import random

par_negativo = random.randrange(-100,-1,2)
print("O número randomico par e negativo é: ", par_negativo)

import random

impar_positivo = random.randrange(1, 100, 2)
print("O número randomico ímpar e positivo é: ", impar_positivo)

import random

impar_negativo = random.randrange(-101,0,2)
print("O número randomico ímpar e negativo é: ", impar_negativo)

"""### exercicio 1

Escreva uma **definição de função** para uma função chamada **add_one** que **recebe um número** e retorna esse **número mais um**.
"""


assert add_one(2) == 3, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert add_one(0) == 1, "Zero mais um é um."
assert add_one(par_positivo) == par_positivo + 1, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert add_one(impar_negativo) == impar_negativo + 1, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
print("Exercício 1 está correto.")

"""### exercicio 2

Escreva uma **definição de função** chamada ***is_positive*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se esse **número for positivo**.
"""


assert is_positive(impar_positivo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_positive(par_positivo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_positive(impar_negativo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_positive(par_negativo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_positive(0) == False, "Zero não é um número positivo."
print("Exercício 2 está correto.")

"""### exercicio 3

Escreva uma **definição de função** chamada ***is_negative*** que **recebe um número** e **retorna** **Verdadeiro** ou **Falso** se esse número **for negativo**.
"""



assert is_negative(impar_positivo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_negative(par_positivo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_negative(impar_negativo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_negative(par_negativo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_negative(0) == False, "Zero não é um número negativo."
print("Exercício 3 está correto.")

"""### exercicio 4

Escreva uma **definição de função** chamada ***is_odd*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se esse **número for ímpar**.
"""




assert is_odd(impar_positivo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_odd(par_positivo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_odd(impar_negativo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_odd(par_negativo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
print("Exercício 4 está correto.")

"""### exercicio 5

Escreva uma definição de **função** chamada ***is_even*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se esse **número for par**.
"""



assert is_even(2) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_even(impar_positivo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_even(par_positivo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_even(impar_negativo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_even(par_negativo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
print("Exercício 5 está correto.")

"""### exercicio 6

Escreva uma definição de **função** chamada ***identity*** que **recebe qualquer argumento** e **retorna o valor** desse argumento. Não pense demais nisso!
"""



assert identity(impar_positivo) == impar_positivo, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert identity(par_positivo) == par_positivo, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert identity(impar_negativo) == impar_negativo, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert identity(par_negativo) == par_negativo, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
print("Exercício 6 está correto.")

"""### exercicio 7

Escreva uma definição de **função** chamada ***is_positive_odd*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o valor for **maior que zero** e **ímpar**
"""



assert is_positive_odd(3) == True, "Verifique sua sintaxe e lógica"
assert is_positive_odd(impar_positivo) == True, "Verifique sua sintaxe e lógica"
assert is_positive_odd(par_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_positive_odd(impar_negativo) == False, "Verifique sua sintaxe e lógica"
assert is_positive_odd(par_negativo) == False, "Verifique sua sintaxe e lógica"
print("Exercício 7 está correto.")

"""### exercicio 8

Escreva uma definição de **função** chamada ***is_positive_even*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o valor for **maior que zero** e **par**
"""


assert is_positive_even(4) == True, "Verifique sua sintaxe e lógica"
assert is_positive_even(impar_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_positive_even(par_positivo) == True, "Verifique sua sintaxe e lógica"
assert is_positive_even(impar_negativo) == False, "Verifique sua sintaxe e lógica"
assert is_positive_even(par_negativo) == False, "Verifique sua sintaxe e lógica"
print("Exercício 8 está correto.")

"""### exercicio 9

Escreva uma definição de **função** chamada ***is_negative_odd*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o valor for **menor que zero** e **ímpar**.
"""



assert is_negative_odd(-3) == True, "Verifique sua sintaxe e lógica"
assert is_negative_odd(impar_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_negative_odd(par_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_negative_odd(impar_negativo) == True, "Verifique sua sintaxe e lógica"
assert is_negative_odd(par_negativo) == False, "Verifique sua sintaxe e lógica"
print("Exercício 9 está correto.")

"""### exercicio 10

Escreva uma definição de **função** chamada ***is_negative_even*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o valor for **menor que zero** e **par**.
"""


assert is_negative_even(-4) == True, "Verifique sua sintaxe e lógica"
assert is_negative_even(impar_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_negative_even(par_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_negative_even(impar_negativo) == False, "Verifique sua sintaxe e lógica"
assert is_negative_even(par_negativo) == True, "Verifique sua sintaxe e lógica"
print("Exercício 10 está correto.")

"""### exercicio 11

Escreva uma definição de **função** chamada ***half*** que **recebe um número** e **retorna a metade** do número fornecido.
"""



assert half(4) == 2
assert half(-5) == -2.5
assert half(impar_positivo) == impar_positivo / 2
assert half(par_positivo) == par_positivo / 2
assert half(impar_negativo) == impar_negativo / 2
assert half(par_negativo) == par_negativo / 2
print("Exercício 11 está correto.")

"""### exercicio 12

Escreva uma definição de **função** chamada ***double*** que **recebe um número** e **retorna o dobro** do número fornecido.
"""



assert double(4) == 8
assert double(-5) == -10
assert double(impar_positivo) == impar_positivo * 2
assert double(par_positivo) == par_positivo * 2
assert double(impar_negativo) == impar_negativo * 2
assert double(par_negativo) == par_negativo * 2
print("Exercício 12 está correto.")

"""### exercicio 13

Escreva uma definição de **função** chamada ***triple*** que **recebe um número** e **retorna o triplo** do número fornecido.
"""


assert triple(4) == 12
assert triple(-5) == -15
assert triple(impar_positivo) == impar_positivo * 3
assert triple(par_positivo) == par_positivo * 3
assert triple(impar_negativo) == impar_negativo * 3
assert triple(par_negativo) == par_negativo * 3
print("Exercício 13 está correto.")

"""### exercicio 14

Escreva uma definição de **função** chamada ***reverse_sign*** que **recebe um número** e **retorna o número** fornecido, mas **com o sinal revertido**.
"""



assert reverse_sign(4) == -4
assert reverse_sign(-5) == 5
assert reverse_sign(impar_positivo) == impar_positivo * -1
assert reverse_sign(par_positivo) == par_positivo * -1
assert reverse_sign(impar_negativo) == impar_negativo * -1
assert reverse_sign(par_negativo) == par_negativo * -1
print("Exercício 14 está correto.")

"""### exercicio 15

Escreva uma definição de **função** chamada ***absolute_value*** que **recebe um número** e **retorna o valor absoluto** do número fornecido
"""



assert absolute_value(4) == 4
assert absolute_value(-5) == 5
assert absolute_value(impar_positivo) == impar_positivo
assert absolute_value(par_positivo) == par_positivo
assert absolute_value(impar_negativo) == impar_negativo * -1
assert absolute_value(par_negativo) == par_negativo * -1
print("Exercício 15 está correto.")

"""### exercicio 16

Escreva uma definição de **função** chamada ***is_multiple_of_three*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o número for **divisível por três**.
"""



assert Fizz(3) == True
assert Fizz(15) == True
assert Fizz(9) == True
assert Fizz(4) == False
assert Fizz(10) == False
print("Exercício 16 está correto.")

"""### exercicio 17

Escreva uma definição de **função** chamada ***is_multiple_of_five*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o número for **divisível por cinco**.
"""



assert Buzz(3) == False
assert Buzz(15) == True
assert Buzz(9) == False
assert Buzz(4) == False
assert Buzz(10) == True
print("Exercício 17 está correto.")

"""### exercicio 18

Escreva uma definição de **função** chamada ***FizzBuzz*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o número for **divisível** tanto por **três** quanto por **cinco**.
"""



assert FizzBuzz(15) == True
assert FizzBuzz(45) == True
assert FizzBuzz(3) == False
assert FizzBuzz(9) == False
assert FizzBuzz(4) == False
print("Exercício 18 está correto.")

"""### exercicio 19

Escreva uma definição de **função** chamada **square** que **recebe um número** e retorna o número **multiplicado** por **si mesmo**.
"""



assert square(3) == 9
assert square(2) == 4
assert square(9) == 81
assert square(impar_positivo) == impar_positivo * impar_positivo
print("Exercício 19 está correto.")

"""### exercicio 20

Escreva uma definição de **função** chamada ***add*** que **recebe dois números** e **retorna a soma**.
"""

assert add(3, 2) == 5
assert add(10, -2) == 8
assert add(5, 7) == 12
print("Exercício 20 está correto.")

"""### exercicio 21

Escreva uma definição de **função** chamada ***cube*** que **recebe um número** e **retorna** o número **multiplicado** por **si mesmo**, **multiplicado** por **si mesmo**.
"""


assert cube(3) == 27
assert cube(2) == 8
assert cube(5) == 125
assert cube(impar_positivo) == impar_positivo * impar_positivo * impar_positivo
print("Exercício 21 está correto.")

"""### exercicio 22

Escreva uma definição de **função** chamada ***square_root*** que **recebe um número** e **retorna a raiz quadrada** do número fornecido
"""



assert square_root(4) == 2.0
assert square_root(64) == 8.0
assert square_root(81) == 9.0
print("Exercício 22 está correto.")

"""### exercicio 23

Escreva uma definição de **função** chamada ***subtract*** que **recebe dois números** e retorna o primeiro número menos o segundo argumento.
"""


assert subtract(8, 6) == 2
assert subtract(27, 4) == 23
assert subtract(12, 2) == 10
print("Exercício 23 está correto.")

"""### exercicio 24

Escreva uma definição de **função** chamada ***multiply*** que **recebe dois números** e retorna o **primeiro** número **multiplicado** pelo **segundo** argumento.
"""



assert multiply(2, 1) == 2
assert multiply(3, 5) == 15
assert multiply(5, 2) == 10
print("Exercício 24 está correto.")

"""### exercicio 25

Escreva uma definição de **função** chamada ***divide*** que **recebe dois números** e retorna o **primeiro** argumento **dividido** pelo **segundo** argumento.
"""


assert divide(27, 9) == 3
assert divide(15, 3) == 5
assert divide(5, 2) == 2.5
assert divide(10, 2) == 5
print("Exercício 25 está correto.")

"""### exercicio 26

Escreva uma definição de **função** chamada **quotient** que **recebe dois números** e retorna **apenas** o **quociente da divisão** do primeiro argumento pelo segundo argumento.
"""



assert quotient(27, 9) == 3
assert quotient(5, 2) == 2
assert quotient(10, 3) == 3
print("Exercício 26 está correto")

"""### exercicio 27

Escreva uma definição de **função** chamada ***remainder*** que **recebe dois números** e retorna o **resto da divisão** do **primeiro** argumento pelo **segundo** argumento.
"""



assert remainder(3, 3) == 0
assert remainder(5, 2) == 1
assert remainder(7, 5) == 2
print("Exercício 27 está correto.")

"""### exercicio 28

Escreva uma definição de **função** chamada ***sum_of_squares*** que **recebe dois números**, **eleva cada número ao quadrado** e depois **retorna a soma** dos dois quadrados.
"""



assert sum_of_squares(3, 2) == 13
assert sum_of_squares(5, 2) == 29
assert sum_of_squares(2, 4) == 20
print("Exercício 28 está correto.")

"""### exercicio 29

Escreva uma definição de **função** chamada ***times_two_plus_three*** que **recebe um número**, **multiplica-o por dois**, **adiciona 3** e retorna o resultado.
"""



assert times_two_plus_three(0) == 3
assert times_two_plus_three(1) == 5
assert times_two_plus_three(2) == 7
assert times_two_plus_three(3) == 9
assert times_two_plus_three(5) == 13
print("Exercício 29 está correto.")


"""## Funções e laços aplicadas a listas

### Exercício 1
"""

# ## Aplicando funções a listas

# Exercício 1)
  # a) Escreva a definição de função chamada obter_maior_numero que recebe uma sequência de números e retorna o maior número.



assert obter_maior_numero([1, 2, 3]) == 3
assert obter_maior_numero([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 5
assert obter_maior_numero([-5, -3, 1]) == 1
print("Exercício 1a) está correto.")

"""### Exercício 1 b)"""

# b) Escreva a definição de função chamada obter_menor_numero que recebe uma sequência de números e retorna o menor número.



assert obter_menor_numero([1, 3, 2]) == 1
assert obter_menor_numero([5, -5, -4, -3, -2, -1, 1, 2, 3, 4]) == -5
assert obter_menor_numero([-4, -3, 1]) == -4
print("Exercício 1b) está correto.")

"""### Exercício 1 c)"""

# c) Escreva a definição de função chamada apenas_números_ímpares que recebe uma sequência de números e retorna os números ímpares em uma lista.



assert apenas_números_ímpares([1, 2, 3]) == [1, 3]
assert apenas_números_ímpares([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -3, -1, 1, 3, 5]
assert apenas_números_ímpares([-4, -3, 1]) == [-3, 1]
assert apenas_números_ímpares([2, 2, 2, 2, 2]) == []
print("Exercício 1c) está correto.")

"""### Exercício 1 d)"""

# Escreva a definição de função chamada apenas_números_pares que recebe uma sequência de números e retorna os números pares em uma lista.


assert apenas_números_pares([1, 2, 3]) == [2]
assert apenas_números_pares([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-4, -2, 2, 4]
assert apenas_números_pares([-4, -3, 1]) == [-4]
assert apenas_números_pares([1, 1, 1, 1, 1, 1]) == []
print("Exercício 1d) está correto.")

"""### Exercício 2 a)"""

# Exercício 2)
# a) Escreva a definição de função chamada apenas_números_positivos que recebe uma sequência de números e retorna os números positivos em uma lista.
def apenas_números_positivos(sequencia):
  num_positivo = [numero for numero in sequencia  if numero> 0]
  return num_positivo

assert apenas_números_positivos([1, 2, 3]) == [1, 2, 3]
assert apenas_números_positivos([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert apenas_números_positivos([-4, -3, 1]) == [1]
print("Exercício 2a) está correto.")

"""### Exercício 2 b)"""

# b) Escreva a definição de função chamada apenas_números_negativos que recebe uma sequência de números e retorna os números negativos em uma lista.
def apenas_números_negativos(sequencia):
  num_negativo = [numero for numero in sequencia  if numero < 0]
  return num_negativo

assert apenas_números_negativos([1, 2, 3]) == []
assert apenas_números_negativos([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -4, -3, -2, -1]
assert apenas_números_negativos([-4, -3, 1]) == [-4, -3]
print("Exercício 2b) está correto.")


"""### Exercício 3 a)"""

# a) Escreva a definição de função chamada contar_pares que recebe uma sequência de números e retorna o número de números pares.

def contar_pares(sequencia):
    contador = 0

    for numero in sequencia:
        if numero % 2 == 0:
            contador += 1

    return contador

assert contar_pares([1, 2, 3]) == 1
assert contar_pares([2, 5, 6]) == 2
assert contar_pares([3, 3, 3]) == 0
assert contar_pares([5, 6, 7, 8] ) == 2
print("Exercício 3a) está correto.")

"""### Exercício 3 b)"""

# b) Escreva a definição de função chamada tem_ímpares que recebe uma sequência de números e retorna True se houver algum número ímpar na sequência.


assert tem_ímpares([1, 2, 3]) == True
assert tem_ímpares([2, 5, 6]) == True
assert tem_ímpares([3, 3, 3]) == True
assert tem_ímpares([2, 4, 6]) == False
print("Exercício 3c) está correto.")


