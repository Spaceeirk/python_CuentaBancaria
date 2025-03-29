import datetime

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.movimientos = []  # Lista de tuplas: (fecha, tipo, monto, saldo)

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.movimientos.append((fecha, 'Depósito', monto, self.saldo))
            print(f"Depósito de {monto} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto > 0:
            if self.saldo >= monto:
                self.saldo -= monto
                fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.movimientos.append((fecha, 'Retiro', monto, self.saldo))
                print(f"Retiro de {monto} realizado. Nuevo saldo: {self.saldo}")
            else:
                print("Fondos insuficientesd para realizar el retiro")
        else:
            print("El monto a retirar debe ser positivo")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

    def mostrar_movimientos(self):
        if self.movimientos:
            print("Historial de movimientos:")
            for movimiento in self.movimientos:
                fecha, tipo, monto, saldo = movimiento
                print(f"{fecha} - {tipo}: {monto} - Saldo después de la transacción: {saldo}")
        else:
            print("No hay movimientos registrados")
