"""
Tarea práctica: crear una función basada en un problema de la vida real
Problema elegido: cálculo del salario semanal de un trabajador
a partir de las horas trabajadas y el pago por hora.

Pseudocódigo guía:

FUNCION calcularSalarioSemanal(horasTrabajadas, pagoPorHora)
    salario ← horasTrabajadas * pagoPorHora
    RETORNAR salario
FIN FUNCION

Uso de la función:
horas ← 40
pago ← 5
resultado ← calcularSalarioSemanal(horas, pago)
IMPRIMIR resultado
"""


def calcularSalarioSemanal(horasTrabajadas, pagoPorHora):
    """
    Calcula el salario semanal de un trabajador.

    Parámetros:
        horasTrabajadas (float): número de horas trabajadas en la semana.
        pagoPorHora (float): pago que recibe el trabajador por cada hora.

    Retorna:
        float: el salario total correspondiente a la semana.
    """
    salario = horasTrabajadas * pagoPorHora
    return salario


if __name__ == "__main__":
    horas = 40
    pago = 5.50

    resultado = calcularSalarioSemanal(horas, pago)

    print("Horas trabajadas:", horas)
    print("Pago por hora: $", pago)
    print("Salario semanal a pagar: $", resultado)