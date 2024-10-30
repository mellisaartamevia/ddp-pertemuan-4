#Soal 1: Bilangan Genap atau Ganjil

bilangan =(input ("masukan angka/n= "))
print(type(bilangan))

hasil =  bilangan % 2 
if hasil == 0:
    print(f"Angka {bilangan} merupakan angka genap")
elif hasil == 1:
    print(f"Angka {bilangan} merupakan angka ganjil")


