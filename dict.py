arabaler={
    "araba1":{"marka": "ford", "yıl": 2000, "rengi": "mor"},
    "araba2":{"marka": "opel", "yıl": 1956, "rengi": "mavi"},
    "araba3":{"marka": "şahin", "yıl": 1923, "rengi": "kırmızı"} }
a= arabaler.keys()#values kulanabilirsin değisken için
print(a)

for x in a:
    print(arabaler[x])
    a1= arabaler[x].keys()
    for y in a1:
        print(arabaler[x][y])
        
        
print(arabaler["araba2"]["rengi"])