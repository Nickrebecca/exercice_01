cotes1 = "23"
max1 = 250

cotes2 = "175"
max2 = 350

cotes3 = "370"
max3 = 380
x=((int(cotes1)+int(cotes2)+int(cotes3))/(max1+max2+max3))*100
#x=(int(cotes1)/max1)*100
print("pourcentage1 "+str(int(cotes1)/(max1)*100))
print("pourcentage2 "+"{0}".format((int(cotes2)/max2)*100))
print("pourcentage3 "+"{0}".format((int(cotes3)/max3)*100))
print("pourcentagetot "+"{0}".format(x))
#print("{o}"(int(cotes1)/max1)*100)
#print("age" {max1})
#print("{0}".format(max1))

#sans modifier le code ci-haut, afficher le pourcentage obtenu pour chaque cote et apres le pourcentange sur toutes les cotes optenus en reunissant les max
