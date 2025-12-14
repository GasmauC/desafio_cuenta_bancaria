class Persona:
    
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre, apellido,numero_cuenta, balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido},\nNumero de cuenta: {self.numero_cuenta}, Balance: {self.balance}"
    
    def depositar(self,monto_depositado):
        if monto_depositado > 0:
            self.balance += monto_depositado
            print(f"Depósito de ${monto_depositado} realizado exitosamente.")
        else:
            print("El monto debe ser positivo.")
        

    def retirar(self,monto_retirado):
        if self.balance > monto_retirado:
            self.balance -= monto_retirado
            print(f"Su saldo actual es de: {self.balance}")
        else:
            print("ERROR!!!: saldo insuficiente")
            print(f"Su saldo actual es de: {self.balance}")
        

def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cta = 123456789
    saldo_inicial = 1000
    cliente = Cliente(nombre,apellido,numero_cta,saldo_inicial)
    return cliente
        
    


mi_cliente = crear_cliente()
print(mi_cliente)

while True:
    op = input("\n[D] Depositar\n[R] Retirar\n[S] Salir\n>>> Seleccione opción: ").upper()
    
    match op:
        case 'D':
            deposito = int(input("Ingrese el monto a depositar: "))
            mi_cliente.depositar(deposito)
            
        case 'R':
            retiro = int(input("Ingrese el dinero a retirar: "))
            mi_cliente.retirar(retiro)
            
        case 'S':
            print("Saliendo del sistema...")
            break 
            
        case _: 
            print("Opción incorrecta, intente de nuevo.")  # El guion bajo captura cualquier otra tecla no valida
                                                           
      
