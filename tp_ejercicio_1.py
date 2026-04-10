# Caja del Kiosco #
# Simular una compra con validaciones y cálculo de total. #
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while). #
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while). #
# 3. Por cada producto (usar for): #
# Pedir precio (entero, validar .isdigit()). #
# Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula). #
# Si tiene descuento: aplicar 10% al precio de ese producto. #
# 4. Al final mostrar: #
# Total sin descuentos #
# Total con descuentos #
# Ahorro total #
# Promedio por producto (usar float y formatear con :.2f, #
# Validaciones obligatorias #
# Sin try/except. # 
# No aceptar vacío en nombre (si queda vacío, es error). #
# Cantidad > 0 (si ingresa 0, volver a pedir). # 

userName = input("Ingrese el nombre de su usuario por favor: ")
userCheck = userName.isalpha();
order = f"Nombre de usuario: {userName}, "
totalOrder = 0
totalUnitary = 0
totalSaving = 0
counterCheck = 0
counterQuantity = 0

if userCheck:
    promProduct = 0
    order = f"Nombre de usuario: {userName}, "
    
    while userCheck:
        productsQuantity = input("Ingrese la cantidad de productos por favor: ")
        quantityCheck =  productsQuantity.isdigit()
        if quantityCheck:
            productsQuantity = int(productsQuantity)
            
            while quantityCheck and counterCheck < productsQuantity:
                    counterCheck += 1
                    if productsQuantity > 0 and counterQuantity < productsQuantity:
                        order += f"Cantidad de productos: {productsQuantity}, "
                        counterQuantity += 1
                        for x in range(productsQuantity):
                            productPrice = input("Ingrese el precio de su producto por favor: ");
                            priceCheck = productPrice.isdigit()
                            productPrice = int(productPrice)
                            if priceCheck and productPrice > 0:

                                order+= f"Precio unitario del producto: {productPrice}, "
                                promProduct+= productPrice
                                totalUnitary+=productPrice
                                productDiscount = input("Ingrese si su producto tiene descuento, insertando S o N por favor: ").lower()

                                while productDiscount == "S" or productDiscount == "N":
                                    if productDiscount == "S":
                                        productWithDiscount = productPrice * 0.90
                                        discount = productPrice * 0.10
                                        order+= f" Precio del producto con el descuento del 10%: {productWithDiscount}, "
                                        totalSaving+=discount
                                        totalOrder+= productWithDiscount
                                        break
                                    else:
                                        order+= f" Precio del producto no el descuento del 10%: N "
                                        break;
                                if productDiscount != "S" or productDiscount != "N":
                                    order+= f" Precio del producto no tiene el descuento del 10% "
                                    break;
                                    
                            else:
                                print("El precio que has ingresado es inválido, por favor intenta nuevamente ingresando un valor númerico.")
                    else: 
                        print("Ha ingresado una cantidad inválida, por favor intente nuevamente.")
            if productsQuantity:       
                quantityCheck = False
                print(productsQuantity)
                print(promProduct)
                promProduct = productsQuantity / promProduct
                order+= f" Total sin descuentos: {totalUnitary}, Total con descuentos: {totalOrder},  Ahorro total: {totalSaving}, Promedio por producto: {promProduct:.2f}" 
                print(order)
                print("Orden finalizada")
                userCheck = False; 
        else:
            print("Error: Has ingresado un valor no número, por favor intenta nuevamente")

else:
    print("Error: Ingrese su nuevamente nombre de usuario sin espacios ni tampoco números por favor.")



