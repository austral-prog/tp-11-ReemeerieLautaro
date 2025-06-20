def read_file_to_dict(nombre_archivo):
    ventas_dict = {}
    try:
        with open(nombre_archivo, 'r') as archivo:
            linea = archivo.readline().strip()
            ventas = linea.split(';')

            for venta in ventas:
                if venta:  
                    try:
                        producto, valor = venta.split(':')
                        valor = float(valor)
                        if producto in ventas_dict:
                            ventas_dict[producto].append(valor)
                        else:
                            ventas_dict[producto] = [valor]
                    except ValueError:
                        print(f"Error en el formato de venta: {venta}")
        return ventas_dict

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return {}
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return {}

def process_dict(diccionario_ventas):
    for producto, montos in diccionario_ventas.items():
        total = sum(montos)
        promedio = total / len(montos) if montos else 0
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
        
if __name__ == "__main__":
    ventas = read_file_to_dict("datos.csv")
    if ventas: 
        process_dict(ventas)
