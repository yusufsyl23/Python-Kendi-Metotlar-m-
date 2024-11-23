# Listeyi Sıralama
# Bu kod küçükten büyüğe sıralar

liste = [9,8,2,5,7,1]

for i in range(1,len(liste)):
    key = liste[i]
    j = i - 1
    
    # Büyükten küçüğe sıralamak için liste[j] < key yazılması yeterli
     
    while (j >= 0 and liste[j] > key):
        liste[j+1] = liste[j]
        j -= 1
    liste[j+1] = key

print(liste)


