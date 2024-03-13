import random
class DFA_MultiplosTres:
    def __init__(self):
        self.estado_actual = 0

    def transicion(self, entrada):
        if entrada == '0':
            self.estado_actual = (self.estado_actual * 2) % 3
        elif entrada == '1':
            self.estado_actual = (self.estado_actual * 2 + 1) % 3
        else:
            raise ValueError("Entrada inválida. Solo se permiten 0 y 1.")

    def es_estado_final(self):
        return self.estado_actual == 0

def verificar_multiplo_de_tres(numero_binario):
    dfa = DFA_MultiplosTres()
    if numero_binario == ">>":
        return True
      #cadena vacia 
    if not numero_binario:
        return dfa.es_estado_final()
    for bit in numero_binario:
        dfa.transicion(bit)
    return dfa.es_estado_final()

def generar_cadena_binaria(longitud, aceptar):
    while True:
        cadena_binaria = ''.join(random.choice('01') for _ in range(longitud))
        if verificar_multiplo_de_tres(cadena_binaria) == aceptar:
            return cadena_binaria
if __name__ == "__main__":
    print("Probando el AFD con cadenas de longitud 1000000")
    cadena_aleatoria1 = generar_cadena_binaria(1000000, True)
    resultado_prueba1 = verificar_multiplo_de_tres(cadena_aleatoria1)
    print(f"El AFD {'acepta' if resultado_prueba1 else 'rechaza'} la cadena")
    cadena_aleatoria2 = generar_cadena_binaria(1000000, False)
    resultado_prueba2 = verificar_multiplo_de_tres(cadena_aleatoria2)
    print(f"El AFD {'acepta' if resultado_prueba2 else 'rechaza'} la cadena")
    while True:
        cadena_ingresada = input("Ingresa la cadena a evaluar, escribe 'exit' para finalizar: ")
        if cadena_ingresada == "exit":
            break
        resultado_evaluacion = verificar_multiplo_de_tres(cadena_ingresada)
        print(f"El AFD {'acepta' if resultado_evaluacion else 'rechaza'} la cadena")
