# Cada lego cuantas partes tienes

McLaren_P1 = [811, 99, 572, 63, 1, 825, 33, 14, 920, 304]
Ferrari_LaFerrari = [957, 65, 11, 745, 900, 370, 2, 820, 57, 63]
Bugatti_Chiron = [593, 215, 9, 800, 92, 600, 45, 15, 701, 240]
Lamborghini_Aventador = [721, 35, 650, 503, 120, 299, 33, 87, 800, 450]
Porsche_918 = [917, 200, 45, 99, 14, 750, 3, 865, 30, 321]
Tesla_Roadster = [43, 567, 890, 212, 310, 82, 14, 76, 299, 999]
Koenigsegg_Agera = [630, 555, 875, 422, 1, 332, 11, 678, 13, 98]
AstonMartin_Vanquish = [815, 230, 3, 675, 510, 2, 18, 36, 999, 411]
Paggani = [902, 33, 17, 590, 11, 300, 35, 270, 13, 678]
Mercedes_Maybach = [520, 150, 22, 81, 700, 290, 49, 11, 900, 67]

print("Numero de bolsas del Porsche 918:",len(Porsche_918))
print("Máximo número de piezas en una bolsa del MclarenP1:",max(McLaren_P1))
print("Mínimo número de piezas en una bolsa del Koenigsegg:", min(Koenigsegg_Agera))


minValor = Ferrari_LaFerrari[0]

for i in Ferrari_LaFerrari:
    if i < minValor:
        minValor = i
print("Mínimo:", minValor)


maxValor = Ferrari_LaFerrari[0]

for i in Ferrari_LaFerrari:
    if i > maxValor:
        maxValor = i
print("Máximo: ", maxValor)