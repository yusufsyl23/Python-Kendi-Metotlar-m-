


# Aşağıdaki kod bir sözlüğün anahtar değerlerini büyükten küçüğe sıralar
"""
my_dict = {7: [10, 6, 9, 1], 4: [7, 5, 11, 2], 10: [4, 8, 3, 15]}

# Aşağıdaki kod ile sorted_keys = [10,7,4] olur
sorted_keys = sorted(my_dict.keys(),reverse=True)

# Eğer küçükten büyüğe sıralamak istersek reverse = True yu silmemiz yeterli

# Aşağıdaki kod ise yukarıdaki sorted_keys listesinden gelen key değerlerini yeni bir sözlüğe sıralı bir şekilde ekler
sorted_dict = {}
for key in sorted_keys:
    sorted_dict[key] = my_dict[key]

print(sorted_dict)
"""
# Aşağıdaki kod bir sözlüğün value değerlerini küçükten büyüğe sıralar

my_dict = {"a": 10, "b": 5, "c": 8, "d": 7}

sorted_dict = sorted(my_dict.items(),key = lambda x: x[1])

# Eğer büyükten küçüğe sıralamak istersek lambda fonksiyonun yanına reverse = True yazarız
# Yukarıda sorted_dict ile value değerlerini sıraladık ama sözlük formatında olmadı 
# Aşağıdaki kod ile sorted_dict i sözlük haline getirmiş olduk 

new_dict = {key:value for (key,value) in sorted_dict}
print(new_dict)

# sorted_dict = sorted(my_dict.items(),key = lambda x: x[1]) fonksiyonu mantığı
"""
1-) sorted() fonksiyonu: Bu fonksiyon bir dizi veya sözlük gibi iterable (yineleyici) veri yapılarını sıralamak için kullanılır.

2-) my_dict.items(): Bu, my_dict adlı sözlüğün anahtar-değer çiftlerini içeren bir görünüm nesnesi oluşturur. Anahtar-değer çiftleri bir dizi içinde 
demetler şeklinde yer alır. Örneğin, [("a", 10), ("b", 5), ("c", 8), ("d", 7)].

3-) key=lambda x: x[1]: Bu, sorted() fonksiyonuna bir anahtar fonksiyonu sağlar. lambda x: x[1], bir lambda ifadesidir ve x adında bir girdi alır. 
Burada, x demetin kendisidir, ve x[1] demetin ikinci elemanıdır, yani değeridir. Bu anahtar fonksiyonu, sözlükteki her bir elemanın ikinci öğesine 
(yani değerine) göre sıralama yapar.

4-) Sonuç: sorted() fonksiyonu, belirtilen anahtar fonksiyonuna göre sözlükteki öğeleri sıralar ve sıralanmış anahtar-değer çiftlerini bir liste olarak döndürür.

Özetle, sorted_dict değişkeni, my_dict sözlüğünün değerlerine göre küçükten büyüğe sıralanmış anahtar-değer çiftlerini içeren bir liste olacaktır.
"""









