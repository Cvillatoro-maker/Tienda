# products and their prices
products = {
    "Laptop": 1000,
    "Phone": 500,
    "Headphones": 100,
    "Charger": 25
}

# Shopping cart to store selected products
cart = []

# Function to display available products
def mostrar_menu():
    print("Productos disponibles:")
    for product, price in products.items():
        print(f"{product}: ${price}")
        
# Function to add products to the cart
def agregar_carrito(producto, cantidad):
    if producto in products:
        cart.append((producto, cantidad, products[producto] * cantidad))
        print(f"Se agregó {cantidad} {producto}(s) al carrito.")
    else:
        print("Producto no disponible.")
        
# Function to calculate the total price
def calcular_total():
    total = sum(item[2] for item in cart)
    print(f"Total: ${total}")
    return total

# Function to apply discount based on total
def aplicar_descuento(total):
    discount = 0
    if total > 500:
        discount = 0.1 * total  # 10% discount
        print(f"Se ha aplicado un descuento de ${discount:.2f}.")
    return discount

# Function to finalize the purchase
def finalizar_compra():
    total = calcular_total()
    descuento = aplicar_descuento(total)
    total_final = total - descuento
    print(f"El total final después de descuentos es: ${total_final:.2f}")
    generar_reporte()

# Function to generate a report
def generar_reporte():
    print("\n--- Resumen de la compra ---")
    for producto, cantidad, subtotal in cart:
        print(f"{producto} (x{cantidad}): ${subtotal}")
    print("---------------------------")

# Main loop for the store simulation
def tienda_en_linea():
    cliente = input("Ingrese su nombre: ")
    print(f"Bienvenido a la tienda en línea, {cliente}!")
    
    while True:
        mostrar_menu()
        producto = input("Seleccione un producto (o 'salir' para finalizar): ")
        if producto.lower() == 'salir':
            break
        cantidad = int(input("Ingrese la cantidad: "))
        agregar_carrito(producto, cantidad)
    
    finalizar_compra()

# Run the store simulation
if __name__ == "__main__":
    tienda_en_linea()
