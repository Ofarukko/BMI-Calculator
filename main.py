import tkinter

# screen
window = tkinter.Tk()
window.title("Vucut Indeksi Hesaplayici")
window.config(padx = 20 ,pady= 20)

# calculate BMI
def hesapla_bmi():
    kilo_input = kilo_entry.get()
    boy_input = boy_entry.get()

    if kilo_input == "" or boy_input == "":
        sonuc_label.config(text="Lutfen boy ve kilo degerlerini giriniz !")
    else:
        try:
            bmi = float(kilo_input) / (float(boy_input) / 100) ** 2
            sonuc = sonuc_yazdir(bmi)
            sonuc_label.config(text= sonuc)
        except:
            sonuc_label.config(text="Lutfen boy ve kilo degerlerinizi dogru giriniz")

# write result
def sonuc_yazdir(bmi):
    sonuc = f"Vucut indeksiniz : {round(bmi,2)}, Siz "
    if bmi <= 18.5:
        sonuc += "Zayifsiniz"
    elif 18.5 < bmi < 24.99:
        sonuc += "Normal kilodasiniz"
    elif 25 < bmi < 29.99:
        sonuc += "Fazla kilodasiniz"
    else:
        sonuc += "Obezsiniz"
    return sonuc

# kilo label
kilo_label = tkinter.Label(text="Lutfen Kilonuzu Giriniz (kg)",font=('Arial',12,"normal"))
kilo_label.config(fg="black")
kilo_label.pack()

# kilo entry
kilo_entry = tkinter.Entry(width=10)
kilo_entry.pack()

# boy label
boy_label = tkinter.Label(text="Lutfen Boyunuzu Giriniz (cm)",font=('Arial',12,"normal"))
boy_label.config(fg="black")
boy_label.pack()

# boy entry
boy_entry =tkinter.Entry(width=10)
boy_entry.pack()

# calculate button
hesapla_button = tkinter.Button(text="Hesapla",command=hesapla_bmi,font=('Arial',14,'bold'),)
hesapla_button.config(fg="black")
hesapla_button.config(bg="light green")
hesapla_button.pack()

# sonuc label
sonuc_label = tkinter.Label()
sonuc_label.pack()


window.mainloop()