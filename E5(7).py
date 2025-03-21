class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._titular = titular
        self._saldo = saldo

    def depositar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero.")
        self._saldo += monto

    def retirar(self, monto: float):
        if monto > self._saldo:
            raise ValueError("Fondos insuficientes.")
        self._saldo -= monto

    def obtener_saldo(self) -> float:
        return self._saldo

    def obtener_titular(self) -> str:
        return self._titular

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular: str, saldo: float, interes_anual: float):
        super().__init__(titular, saldo)
        if interes_anual < 0:
            raise ValueError("El interés anual no puede ser negativo.")
        self.__interes_anual = interes_anual

    def aplicar_interes(self):
        self._saldo += self._saldo * (self.__interes_anual / 100)

    def obtener_interes_anual(self) -> float:
        return self.__interes_anual

# Ejemplo de uso
cuenta = CuentaAhorro("Cristian Conde", 1000, 5)
print(f"Titular: {cuenta.obtener_titular()}, Saldo: {cuenta.obtener_saldo()}, Interés Anual: {cuenta.obtener_interes_anual()}%")

cuenta.aplicar_interes()
print(f"Saldo después de aplicar interés: {cuenta.obtener_saldo()}")
