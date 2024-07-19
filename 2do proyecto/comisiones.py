print("/////////////////////////////////////")
print("/////- Generador de Comisiones -/////")
print("/////////////////////////////////////\n")

nombre_empleado = input("Dime tu nombre: ")
venta = float(input("Dime las ventas totales del mes: "))

comision = round(((venta/100)*13),2)

print(f"\nSeñor/a {nombre_empleado} su comision es de {comision}")





