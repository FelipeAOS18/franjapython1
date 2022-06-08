#diccionario
diccionario={}
diccionario_capitales={
    'Chile':'Santiago',
    'España':'Madrid',
    'Argentina':'Mendoza'
}
print(diccionario_capitales['España'].upper())


for pais, capital in diccionario_capitales.items():
    print(pais)