import folium
diccionarioObjetos = {1: ['Cordoba' , [0, 677, 824, 698] , [-31.4135, -64.18105]],
                      2: ['Corrientes' , [646, 0, 677, 830] , [ -27.461195,-58.836841]],
                      3: ['Formosa' , [792, 677, 0, 968], [-26.18489, -58.17313]] ,
                      4: ['La Plata' , [698, 830, 968, 0] , [-34.92145, -57.95453]]}

recorridos = [1,4,3,2]
ubicaciones = []
for i in recorridos:
    ciudad = diccionarioObjetos[i]
    ubicaciones.append(ciudad[2])

print("Ubicaciones: ",ubicaciones)



m = folium.Map(location=[-38.416097, -63.616672], zoom_start = 5)

"""probando = folium.RegularPolygonMarker(location=ubicaciones, fill_color='blue', number_of_sides=3, radius=10, rotation=180).add_to(m)"""
route = folium.PolyLine(
    locations = ubicaciones, #Conectar puntos de coordenadas
    peso = 3, # el tamaño de la línea es 3
    color = 'orange', # El color de la línea es naranja
    opacidad = 0.8 #transparencia de la línea
) .add_to (m) #Agregue esta línea al área m justo ahora

folium.Marker(
    location= ubicaciones[0],
    popup="First Location",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(m)

folium.Marker(
    location= ubicaciones[3],
    popup="Last Location",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(m)

m.save("index.html")