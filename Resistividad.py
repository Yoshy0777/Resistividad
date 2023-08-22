#Resistencia en un conductor electrico
#R=P * (L/S)
# Este programa va a contener cararcteristicas y materiales precargados

Resistividad = {"Al":(0.028, "Aluminio"),
                "Cu":(0.017, "Cobre"),
                "Au":(0.023,"Oro"),
                "Fe":(0.13, "Hierro"),
                "Ag":(0.16, "Plata"),
                "Hg":(0.96, "Mercurio"),
                "Pb":(0.22, "Plomo"),
                "Pt":(0.11, "Platino"),
                "Zn":(0.061, "Zinc")}

L = float(input("Ingresa la longitud en Metros (m) "))
S = float(input("Ingresa la seccion del conductor en (mm2) "))

while True:
    Material = input("Ingresa el simbolo del material ")
    if (Material in Resistividad):
        print("--- Material encontrado ---")
        break
    else:
        print("Error, Elemento no encontrado")
P = Resistividad[Material][0]
print("Resistividad de ",Resistividad[Material][1], " = [ohm.mm1/m]")

if S==0:
    print("Error. No puede ser cero")
else:
    R = P*L/S
    print("La resistividad de: ",R,"Ohms")