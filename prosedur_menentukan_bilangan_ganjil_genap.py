# Prosedur tentukan ganjil genap
def tentukan_ganjil_genap(angka):
    if angka > 0:
        if angka %2==0:
            print ("adalah bilangan genap")
        else:
            print("adalah bilangan ganjil: ")
    else:
        print("adalah nol atau bukan bilangan positif")
#main 
angka = int(input("masukkan anglka: "))
tentukan_ganjil_genap(angka)
