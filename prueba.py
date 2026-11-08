# Seminario 1 - Prueba de GitHub Copilot
# Escribe un programa que recorra los 100 primeros números primos y los imprima en pantalla.

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
even_count = 0
num = 2
while count < 100:
    if es_primo(num):
        print(num)
        count += 1
        if num % 2 == 0:
            even_count += 1
    num += 1

print(f"Cantidad de números primos pares: {even_count}")

