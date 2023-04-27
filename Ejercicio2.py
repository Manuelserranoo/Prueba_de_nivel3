class Pedido:
    def __init__(self, nombre, multiverso, descripcion):
        self.nombre = nombre
        self.multiverso = multiverso
        self.descripcion = descripcion
        
class ColaPedidos:
    def __init__(self):
        self.pedidos = []
    
    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)
    
    def atender_pedidos(self):
        bitacora = []
        while self.pedidos:
            mayor_prioridad = None
            for pedido in self.pedidos:
                prioridad = self.obtener_prioridad(pedido)
                if mayor_prioridad is None or prioridad > self.obtener_prioridad(mayor_prioridad):
                    mayor_prioridad = pedido
            self.pedidos.remove(mayor_prioridad)
            bitacora.append(mayor_prioridad)
        return bitacora
    
    def obtener_prioridad(self, pedido):
        if pedido.nombre == "Gran Conquistador" or pedido.multiverso == "616" or "El que permanece" in pedido.descripcion:
            return 3
        elif pedido.nombre == "Khan que todo lo sabe" or "Carnicero de Dioses" in pedido.descripcion or pedido.multiverso == "838":
            return 2
        else:
            return 1

def main():
    bitacora = []
    cola = ColaPedidos()
    cola.agregar_pedido(Pedido("Khan que todo lo sabe", "350", "Necesito ayuda para encontrar una Gema del Infinito"))
    cola.agregar_pedido(Pedido("Gran Conquistador", "616", "Debo encontrar a El que permanece en el universo 199999"))
    cola.agregar_pedido(Pedido("Solicitante 1", "1043", "Quiero conocer el multiverso donde Loki se convirtió en el rey de Asgard"))
    cola.agregar_pedido(Pedido("Solicitante 2", "838", "Necesito ayuda para detener al Carnicero de Dioses en mi universo"))
    cola.agregar_pedido(Pedido("Solicitante 3", "616", "Quiero conocer el multiverso donde Loki se convirtió en el rey de Asgard"))
    cola.agregar_pedido(Pedido("Solicitante 4", "1043", "Necesito ayuda para detener al Carnicero de Dioses en mi universo"))
    cola.agregar_pedido(Pedido("Solicitante 5","212","El que permanece me ha pedido ayuda para detener a ironman"))
    bitacora = cola.atender_pedidos()
    for pedido in bitacora:
        print(pedido.nombre, pedido.multiverso, pedido.descripcion)

if __name__ == "__main__":
    main()
