from cuenta import CuentaBancaria

cuenta = CuentaBancaria("MIcaela Torrejon", 1000)
cuenta.mostrar_saldo()
cuenta.depositar(500)
cuenta.retirar(2000)
cuenta.retirar(300)
cuenta.mostrar_saldo()
cuenta.mostrar_movimientos()

