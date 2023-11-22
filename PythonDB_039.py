import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

uiApp = tk.Tk()
uiApp.configure(background='pink')
uiApp.geometry("600x800")
uiApp.title("PILIHAN PRODI")

#make canvas
inputFrame = tk.Frame(uiApp)
inputFrame.pack(padx=10,fill="x", expand=True)

#make label
inputLabel = ttk.Label(inputFrame, text="NILAI SISWA")
inputLabel.pack(padx=10, pady=10, fill="x", expand=True)

#1. Membuat input nama dan nilai mapel
labelInputNAMA = ttk.Label(inputFrame, text="MASUKKAN NAMA SISWA")
labelInputNAMA.pack(padx=10, pady=5, fill="x", expand=True)

entryInputNAMA = ttk.Entry(inputFrame, text="MASUKKAN NAMA SISWA")
entryInputNAMA.pack(padx=10, pady=5, fill="x", expand=True)

#2
labelInputBIO = ttk.Label(inputFrame, text="MASUKKAN NILAI BIOLOGI")
labelInputBIO.pack(padx=10, pady=5, fill="x", expand=True)

entryInputBIO = ttk.Entry(inputFrame, text="MASUKKAN NILAI BIOLOGI")
entryInputBIO.pack(padx=10, pady=5, fill="x", expand=True)

#3
labelInputFISIKA = ttk.Label(inputFrame, text="MASUKKAN NILAI FISIKA")
labelInputFISIKA.pack(padx=10, pady=5, fill="x", expand=True)

entryInputFISIKA = ttk.Entry(inputFrame, text="MASUKKAN NILAI FISIKA")
entryInputFISIKA.pack(padx=10, pady=5, fill="x", expand=True)

#4
labelInputING = ttk.Label(inputFrame, text="MASUKKAN NILAI B INGGRIS")
labelInputING.pack(padx=10, pady=5, fill="x", expand=True)

entryInputING = ttk.Entry(inputFrame, text="MASUKKAN NILAI B INGGRIS")
entryInputING.pack(padx=10, pady=5, fill="x", expand=True)

def klikButton ():
    BIOLOGI = entryInputBIO.get()
    FISIKA = entryInputFISIKA.get()
    ING = entryInputING.get()
    
    if BIOLOGI > FISIKA and BIOLOGI > ING:
        HASIL = "KEDOKTERAN"
    elif FISIKA > BIOLOGI and FISIKA > ING:
        HASIL = "TEKNIK"
    elif ING > BIOLOGI and ING > FISIKA:
        HASIL = "BAHASA"
    else:
        HASIL = "NILAI YANG DIINPUTKAN MEMILIKI BOBOT SAMA"
    
    messagebox.showinfo("HASIL PREDIKSI :", f'{HASIL}')

def simpan_data_ke_sqlite(nilai1,nilai2, prodi_terpilih):
    # Membuka atau membuat database SQLite
    conn = sqlite3.connect("Windya1.db")
    cursor = conn.cursor()
    
    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    NAMA TEXT,
                    BIOLOGI REAL, 
                    FISIKA REAL,
                    ING REAL,
                    HASIL_PREDIKSI TEXT)''')
    
    # Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO NILAI (NAMA, BIOLOGI, FISIKA, ING, HASIL_PREDIKSI) VALUES (?, ?, ?, ?, ?)",
    (NAMA, BIOLOGI, FISIKA, ING, HASIL))
    
    # Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

buttonSubmit = ttk.Button(inputFrame, text="PREDIKSI SEKARANG", command=klikButton)
buttonSubmit.pack(padx=10, pady=10, fill="x", expand=True)

uiApp.mainloop()