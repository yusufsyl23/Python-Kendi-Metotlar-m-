# Matrisin satır ve sütunlarını sözlük haline getirme

m = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

sütunlar = {j: [] for j in range(len(m[0]))}
satırlar = {i: [] for i in range(len(m))}

for i in range(len(m)):
    for j in range(len(m[i])):
        sütunlar[j].append(m[i][j])
        satırlar[i].append(m[i][j])

print(sütunlar)
print(satırlar)

