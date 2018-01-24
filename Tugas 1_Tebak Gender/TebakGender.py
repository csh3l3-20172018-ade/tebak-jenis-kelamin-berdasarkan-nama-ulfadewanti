# Mengambil input
nama = input("Siapa nama kamu: ")

#menentukan kemungkinan gender dgn menghitung huruf pada nama berdasarkan aturan
laki = 0
pr = 0

#huruf yang dapat di prediksi dapat dalam huruf besar atau kecil
for i in nama:
    if ((i == "i") or (i == "a") or (i == "u") or (i == "e") or (i == "t")
        or (i == "I") or (i == "A") or (i == "U") or (i == "E") or (i == "T")):
        pr = pr + 1
    elif ((i == "b") or (i == "d") or (i == "o")
          or (i == "B") or (i == "D") or (i == "O")):
        laki = laki + 1


# Menampilkan output
if (laki < pr):
    print("Gender = female")
elif (laki > pr):
    print("Gender = laki")
else:
    print("Gender = Tidak Diketahui")





