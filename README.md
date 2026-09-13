# Tarea práctica: Función basada en un problema de la vida real

**Estudiante:** Aaron Jardiel Toapanta Balseca
**Curso:** Fundamentos de Programación
**Fecha:** 07 al 13 de septiembre de 2026

## Descripción del problema

Se resuelve el problema de calcular el **salario semanal** de un trabajador
a partir de dos datos: las **horas trabajadas** durante la semana y el
**pago por hora** que recibe. El programa define una función que recibe
ambos valores como parámetros, calcula el salario multiplicándolos y
retorna el resultado, el cual se muestra luego en consola.

## Pseudocódigo

```
FUNCION calcularSalarioSemanal(horasTrabajadas, pagoPorHora)
    salario ← horasTrabajadas * pagoPorHora
    RETORNAR salario
FIN FUNCION

Uso de la función:
horas ← 40
pago ← 5
resultado ← calcularSalarioSemanal(horas, pago)
IMPRIMIR resultado
```

## Archivo

- `salario.py`: contiene la función `calcularSalarioSemanal(horasTrabajadas, pagoPorHora)`
  y su llamada desde el bloque `if __name__ == "__main__":`, donde se
  imprime el resultado con `print()`.

## Cómo ejecutar

```bash
python3 salario.py
```

### Salida esperada

```
Horas trabajadas: 40
Pago por hora: $ 5.5
Salario semanal a pagar: $ 220.0
```