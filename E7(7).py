class TarjetaCredito:
    def __init__(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta

    @staticmethod
    def validar(numero):
        digitos = [int(d) for d in str(numero)][::-1]  
        for i in range(1, len(digitos), 2):
            digitos[i] *= 2
            if digitos[i] > 9:
                digitos[i] -= 9
        return sum(digitos) % 10 == 0  

# Ejemplo de uso:
numero = 1050278574  
print(TarjetaCredito.validar(numero)) 

