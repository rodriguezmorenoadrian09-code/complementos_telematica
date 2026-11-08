# Complementos de Telemática – Seminario 1

**Autor:** Adrián Rodríguez Moreno

## Qué hace el script

`prueba.py` muestra por pantalla los 100 primeros números primos (del 2 al 541)
y, al final, cuántos de ellos son pares.

Para ello:

- define la función `es_primo(n)`, que devuelve `True` si `n` es primo, probando
  divisores desde 2 hasta la raíz cuadrada de `n`;
- recorre los números a partir del 2 con un bucle `while` y va imprimiendo los
  que son primos hasta llevar 100;
- con un segundo contador (`even_count`) cuenta los primos pares y lo muestra
  al terminar.

## Cómo se ejecuta

Hace falta tener Python 3 instalado. Desde una terminal, en la carpeta del script:

```bash
python prueba.py
```

También se puede abrir en VS Code y pulsar el botón ▶ (*Run Python File*).

Salida (resumida):

```
2
3
5
...
523
541
Cantidad de números primos pares: 1
```

## Cómo lo hice con Copilot

### Prompt utilizado

> Escribe un programa que recorra los 100 primeros números primos y los imprima en pantalla.

### Qué pregunté a Copilot

- **¿Por qué si n es menor que 1 se hace un `return False`?**
  Copilot explicó que un número primo tiene que ser un natural mayor que 1 con
  exactamente dos divisores (1 y él mismo). Por eso el `if n <= 1: return False`
  descarta el 0, el 1 y los negativos, y el `return` termina la función en ese
  momento sin probar ningún divisor.

### Qué cambié

- Pedí que, además de lo que ya hacía, el programa contara cuántos de esos
  primos son pares. Se añadió el contador `even_count`, que suma 1 cada vez que
  un primo es divisible entre 2, y un `print` final con el resultado.
- El resultado es 1, porque el único número primo par es el 2: cualquier otro
  número par es divisible entre 2 y, por tanto, no es primo.
- **Cambio hecho a mano (sin Copilot):** el límite de 100 primos estaba escrito
  directamente en el `while`. Lo he sacado a una variable, `limite`, al
  principio del programa, para poder mostrar otra cantidad de primos cambiando
  solo ese valor.
