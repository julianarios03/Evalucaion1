Frutas = []

def costo_total():
    total=0
    for fruta in Frutas:
        total+=fruta['precio_unitario'] * fruta['cantidad']
    return total 

def mostrar_frutasordenadas():
    frutas_ordenadas=sorted(Frutas, key=lambda x: x['precio_unitario'], reverse=True)   
    for fruta in frutas_ordenadas:
        print(f"{fruta['nombre']}:${fruta['precio_unitario']} por unidad")    
        
def mostrar_frutas():
    fruta_mas_barata = min(Frutas, key=lambda  x: x['precio_unitario'])        
    fruta_mas_cara = max(Frutas, key=lambda  x: x['precio_unitario'])  
    print(f"Fruta mas barata:{fruta_mas_barata['nombre']} (${fruta_mas_barata['precio_unitario']}por unidad)")
    print(f"Fruta mas cara:{fruta_mas_cara['nombre']} (${fruta_mas_cara['precio_unitario']}por unidad)")
    
N = int(input("Ingrese la cantidad de frutas que desea registrar:"))


for i in range (N):
    print(f"Ingrese los datos de la fruta {i+1}:")
    id_fruta= input("Id:")
    nombre_fruta= input("Nombre:")
    precio_unitario_fruta= float(input("precio unitario:"))
    cantidad_fruta = int(input("Cantidad:"))
    
    Frutas.append({
        'id': id_fruta,
        'nombre': nombre_fruta,
        'precio_unitario': precio_unitario_fruta,
        'cantidad': cantidad_fruta
    })
    
    print(f"Costo total del salpicon: ${costo_total()}")
    
    print("Frutas ordenadas por precio:")
    mostrar_frutasordenadas
    
    mostrar_frutas()
    
    