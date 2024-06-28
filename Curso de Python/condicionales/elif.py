# ejemplo de if anidados y else if (elif)

ingreso_mensual = 11000
gasto_mensual = 12000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0: 
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien")
    else: 
        print("OMG, estas gastando una banda")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")

elif ingreso_mensual > 500:
    print("estas bien en Dominicana")
    
elif ingreso_mensual > 200:
    print("estas bien en Haiti")

else:
    print("sos pobre")