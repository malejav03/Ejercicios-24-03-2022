palabra= input('introduzca una palabra:')

longitud_palabra = len(palabra)

vocal_a = palabra.count('a')
vocal_e = palabra.count('e')
vocal_i = palabra.count('i')
vocal_o = palabra.count('o')
vocal_u = palabra.count('u')

metrica = longitud_palabra * (vocal_a + vocal_e + vocal_i + vocal_o + vocal_u)
print(metrica)
