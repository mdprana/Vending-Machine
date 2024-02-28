import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class VendingMachine:
    # Inisialisasi state dan pilihan user
    def __init__(self): 
        self.saldo = 0  
        self.selected_size = ''
        self.selected_color = ''
        self.product_name = '' 

    # Fungsi membangun GUI
    def create_widgets(self, master):
        # Buat judul
        self.master = master
        self.master.title("Vending Machine")
        self.master_label = tk.Label(self.master, text = "Vending Machine Baju", font = 'robotto 12 bold', relief = RAISED)
        self.master_label.pack(fill = tk.X)
        # Masukan foto
        self.frm1 = ttk.Frame(self.master, padding = 10)
        self.canvas = Canvas(self.frm1, width = 300, height = 200)
        self.img = Image.open("SizeChart.jpg")
        resized_image= self.img.resize((300,200), Image.Resampling.LANCZOS)
        self.img= ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(10, 10, anchor = NW, image = self.img)
        self.canvas.grid(row = 1, column = 0)
        self.frm1.pack()
        # Label pilihan
        self.frm2 = ttk.Frame(self.master, padding = 10)
        self.label_jenis_baju = ttk.Label(self.frm2, text = "Pilihan Jenis Baju")
        self.label_jenis_baju.grid(row = 1, column = 1, padx = 5)
        self.label_ukuran_baju = tk.Label(self.frm2, text = "Pilihan Ukuran Baju")
        self.label_ukuran_baju.grid(row = 1, column = 2, padx = 5)
        self.label_warna_baju = tk.Label(self.frm2, text = "Pilihan Warna Baju")
        self.label_warna_baju.grid(row = 1, column = 3, padx = 5)
        self.frm2.pack()
        # Label saldo
        self.frm3 = ttk.Frame(self.master, padding = 10)
        self.saldo_label = tk.Label(self.frm3, text="Saldo: Rp. 0")
        self.saldo_label.grid(row = 2, column = 1)
        self.frm3.pack()
        # Tombol masukan uang
        self.frm4 = ttk.Frame(self.master, padding = 10)
        button_money1 = tk.Button(self.frm4, text = "Rp. 10.000", command = self.add_money1)
        button_money1.grid(row = 3, column = 0)
        button_money2 = tk.Button(self.frm4, text = "Rp. 20.000", command = self.add_money2)
        button_money2.grid(row = 3, column = 1)
        button_money3 = tk.Button(self.frm4, text = "Rp. 50.000", command = self.add_money3)
        button_money3.grid(row = 3, column = 2)
        self.frm4.pack()
        # Tombol pilih jenis baju
        self.frm5 = ttk.Frame(self.master, padding = 10)
        self.jenis_label = tk.Label(self.frm5, text="Pilih Jenis Baju")
        self.jenis_label.grid(row = 4, column = 0)
        self.frm5.pack()
        self.frm6 = ttk.Frame(self.master, padding = 10)
        button_kaos_pendek = tk.Button(self.frm6, text = "Kaos Lengan Pendek (Rp. 50.000)", command = self.handle_kaos_pendek)
        button_kaos_pendek.grid(row = 5, column = 0)
        button_kaos_panjang = tk.Button(self.frm6, text = "Kaos Lengan Panjang (Rp. 60.000)", command = self.handle_kaos_panjang)
        button_kaos_panjang.grid(row = 5, column = 1)
        button_kemeja_pendek = tk.Button(self.frm6, text = "Kemeja Lengan Pendek (Rp. 70.000)", command = self.handle_kemeja_pendek)
        button_kemeja_pendek.grid(row = 6, column = 0)
        button_kemeja_panjang = tk.Button(self.frm6, text = "Kemeja Lengan Panjang (Rp. 80.000)", command = self.handle_kemeja_panjang)
        button_kemeja_panjang.grid(row = 6, column = 1)
        self.frm6.pack()
        # Tombol pilih ukuran baju
        self.frm7 = ttk.Frame(self.master, padding = 10)
        self.ukuran_label = tk.Label(self.frm7, text="Pilih Ukuran Baju")
        self.ukuran_label.grid(row = 7, column = 0)
        self.frm7.pack()
        self.frm8 = ttk.Frame(self.master, padding = 10)
        button_s = tk.Button(self.frm8, text = "Ukuran S", command = self.handle_s)
        button_s.grid(row = 8, column = 0)
        button_m = tk.Button(self.frm8, text = "Ukuran M", command = self.handle_m)
        button_m.grid(row = 8, column = 1)
        button_l = tk.Button(self.frm8, text = "Ukuran L", command = self.handle_l)
        button_l.grid(row = 8, column = 2)
        self.frm8.pack()
        # Tombol pilih warna
        self.frm9 = ttk.Frame(self.master, padding = 10)
        self.warna_label = tk.Label(self.frm9, text="Pilih Warna Baju")
        self.warna_label.grid(row = 9, column = 0)
        self.frm9.pack()
        self.frm10 = ttk.Frame(self.master, padding = 10)
        button_black = tk.Button(self.frm10, text = "Warna Hitam", command = self.handle_black)
        button_black.grid(row = 10, column = 0)
        button_white = tk.Button(self.frm10, text = "Warna Putih", command = self.handle_white)
        button_white.grid(row = 10, column = 1)
        self.frm10.pack()    
        # Tombol konfirmasi
        self.frm11 = ttk.Frame(self.master, padding = 10)
        button_confirm = tk.Button(self.frm11, text = "Konfirmasi", command = self.confirm)
        button_confirm.grid(row = 11, column = 1)
        self.frm11.pack()

    # Tambah Uang
    def add_money1(self):
        self.saldo += 10000
        self.update_saldo_label()

    def add_money2(self):
        self.saldo += 20000
        self.update_saldo_label()

    def add_money3(self):
        self.saldo += 50000
        self.update_saldo_label()

    # Pilih Jenis Baju
    def handle_kaos_pendek(self):
        if self.saldo < 50000:
            messagebox.showwarning("Saldo Kurang", "Harap Isi Saldo Terlebih Dahulu")
        elif self.product_name != '':
            messagebox.showwarning("Pilihan Invalid", "Harap Hanya Pilih Satu Jenis Baju")    
        else:
            self.product_name = 'Kaos Lengan Pendek'
            self.label_jenis_baju.config(text=f"Kaos Lengan Pendek")
            self.saldo -= 50000
            self.update_saldo_label()

    def handle_kaos_panjang(self):
        if self.saldo < 60000:
            messagebox.showwarning("Saldo Kurang", "Harap Isi Saldo Terlebih Dahulu")
        elif self.product_name != '':
            messagebox.showwarning("Pilihan Invalid", "Harap Hanya Pilih Satu Jenis Baju")
        else:
            self.product_name = 'Kaos Lengan Panjang'
            self.label_jenis_baju.config(text=f"Kaos Lengan Panjang")
            self.saldo -= 60000
            self.update_saldo_label()

    def handle_kemeja_pendek(self):
        if self.saldo < 70000:
            messagebox.showwarning("Saldo Kurang", "Harap Isi Saldo Terlebih Dahulu")
        elif self.product_name != '':
            messagebox.showwarning("Pilihan Invalid", "Harap Hanya Pilih Satu Jenis Baju")    
        else:
            self.product_name = 'Kemeja Lengan Pendek'
            self.label_jenis_baju.config(text=f"Kemeja Lengan Pendek")
            self.saldo -= 70000
            self.update_saldo_label()

    def handle_kemeja_panjang(self):
        if self.saldo < 80000:
            messagebox.showwarning("Saldo Kurang", "Harap Isi Saldo Terlebih Dahulu")
        elif self.product_name != '':
            messagebox.showwarning("Pilihan Invalid", "Harap Hanya Pilih Satu Jenis Baju")    
        else:
            self.product_name = 'Kemeja Lengan Panjang'
            self.label_jenis_baju.config(text=f"Kemeja Lengan Panjang")
            self.saldo -= 80000
            self.update_saldo_label()

    # Pilih Ukuran
    def handle_s(self):
        if self.product_name == '':
            messagebox.showwarning("Pilihan Invalid", "Harap Pilih Jenis Baju Terlebih Dahulu")    
        elif self.selected_size != '':
            messagebox.showwarning("Pilihan Invalid", "Harap Pilih Satu Ukuran Saja")
        else:
            self.label_ukuran_baju.config(text=f"Ukuran S")
            self.selected_size = 'Ukuran S'
            self.product_name += ' Ukuran S'                              

    def handle_m(self):
        if self.product_name == '':
            messagebox.showwarning("Pilihan Invalid", "Harap Pilih Jenis Baju Terlebih Dahulu")    
        elif self.selected_size != '':
            messagebox.showwarning("Pilihan Invalid", "Harap Pilih Satu Ukuran Saja")
        else:
            self.label_ukuran_baju.config(text=f"Ukuran M")
            self.selected_size = 'Ukuran M'
            self.product_name += ' Ukuran M'

    def handle_l(self):
        if self.product_name == '':
            messagebox.showwarning("Pilihan Invalid", "Harap Pilih Jenis Baju Terlebih Dahulu")    
        elif self.selected_size != '':
            messagebox.showwarning("Pilihan Invalid", "Harap Pilih Satu Ukuran Saja")
        else:
            self.label_ukuran_baju.config(text=f"Ukuran L")
            self.selected_size = 'Ukuran L'
            self.product_name += ' Ukuran L'

    # Pilih Warna
    def handle_black(self):
        if self.product_name == '':
            messagebox.showwarning("Pilihan Invalid", "Harap Pilih Jenis Baju Terlebih Dahulu")    
        elif self.selected_color != '':
            messagebox.showwarning("Pilihan Invalid", "Harap Pilih Satu Warna Saja")
        else:
            self.label_warna_baju.config(text=f"Warna Hitam")
            self.selected_color = 'Warna Hitam'
            self.product_name += ' Warna Hitam'
    
    def handle_white(self):
        if self.product_name == '':
            messagebox.showwarning("Pilihan Invalid", "Harap Pilih Jenis Baju Terlebih Dahulu")    
        elif self.selected_color != '':
            messagebox.showwarning("Pilihan Invalid", "Harap Pilih Satu Warna Saja")
        else:
            self.label_warna_baju.config(text=f"Warna Putih")
            self.selected_color = 'Warna Putih'
            self.product_name += ' Warna Putih'
    
    # Merubah Tampilan Saldo
    def update_saldo_label(self):
        self.saldo_label.config(text=f"Saldo: Rp. {self.saldo:.2f}")

    # Tombol konfirmasi
    def confirm(self):
        if self.selected_size != '' and self.selected_color != '':
            messagebox.showinfo("Anda Berhasil Membeli Barang", f"Sukses Membeli {self.product_name}, Kembalian Anda Adalah Rp. {self.saldo}")
            self.product_name = ''
            self.saldo = 0
            self.selected_size = ''
            self.selected_color = ''
            self.saldo_label.config(text=f"Saldo: Rp. {self.saldo:.2f}")
            self.label_jenis_baju.config(text=f"Pilihan Jenis Baju")
            self.label_ukuran_baju.config(text=f"Pilihan Ukuran Baju")
            self.label_warna_baju.config(text=f"Pilihan Warna Baju")
        elif 'Kaos Lengan Pendek' in self.product_name and (self.selected_size == '' or self.selected_color == ''):
            messagebox.showinfo("Pilihan Invalid", f"Uang Anda Kembali Sebesar Rp. {self.saldo + 50000}")
            self.saldo = 0   
            self.saldo_label.config(text=f"Saldo: Rp. {self.saldo:.2f}")
            self.product_name = ''
            self.selected_size = ''
            self.selected_color = ''
            self.label_jenis_baju.config(text=f"Pilihan Jenis Baju")
            self.label_ukuran_baju.config(text=f"Pilihan Ukuran Baju")
            self.label_warna_baju.config(text=f"Pilihan Warna Baju")
        elif 'Kaos Lengan Panjang' in self.product_name and (self.selected_size == '' or self.selected_color == ''):
            messagebox.showinfo("Pilihan Invalid", f"Uang Anda Kembali Sebesar Rp. {self.saldo + 60000}")
            self.saldo = 0   
            self.saldo_label.config(text=f"Saldo: Rp. {self.saldo:.2f}")
            self.product_name = ''
            self.selected_size = ''
            self.selected_color = ''
            self.label_jenis_baju.config(text=f"Pilihan Jenis Baju")
            self.label_ukuran_baju.config(text=f"Pilihan Ukuran Baju")
            self.label_warna_baju.config(text=f"Pilihan Warna Baju")
        elif 'Kemeja Lengan Pendek' in self.product_name and (self.selected_size == '' or self.selected_color == ''):
            messagebox.showinfo("Pilihan Invalid", f"Uang Anda Kembali Sebesar Rp. {self.saldo + 70000}")
            self.saldo = 0   
            self.saldo_label.config(text=f"Saldo: Rp. {self.saldo:.2f}")
            self.product_name = ''
            self.selected_size = ''
            self.selected_color = ''
            self.label_jenis_baju.config(text=f"Pilihan Jenis Baju")
            self.label_ukuran_baju.config(text=f"Pilihan Ukuran Baju")
            self.label_warna_baju.config(text=f"Pilihan Warna Baju")
        elif 'Kemeja Lengan Panjang' in self.product_name and (self.selected_size == '' or self.selected_color == ''):
            messagebox.showinfo("Pilihan Invalid", f"Uang Anda Kembali Sebesar Rp. {self.saldo + 80000}")
            self.saldo = 0   
            self.saldo_label.config(text=f"Saldo: Rp. {self.saldo:.2f}")
            self.product_name = ''
            self.selected_size = ''
            self.selected_color = ''
            self.label_jenis_baju.config(text=f"Pilihan Jenis Baju")
            self.label_ukuran_baju.config(text=f"Pilihan Ukuran Baju")
            self.label_warna_baju.config(text=f"Pilihan Warna Baju")
        else:
            messagebox.showinfo("Pilihan Invalid", f"Uang Anda Kembali Sebesar Rp. {self.saldo}")
            self.saldo = 0   
            self.saldo_label.config(text=f"Saldo: Rp. {self.saldo:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    vending_machine = VendingMachine()
    vending_machine.create_widgets(root)
    root.mainloop()
