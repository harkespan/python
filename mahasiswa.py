def show_mhs(mahasiswa):
    #fungsi ini digunakan untuk menampilkan semua data mahasiswa
    print(f'{"No":<3} | {"NIM":<20} | {"Nama":<30} | {"Alamat":<20} ')
    print('------------------------------------------------------------------------------------------------')
    i = 1
    for mhsid,mhs in mahasiswa.items():
        print(f'{i:<3} | {mhs["nim"]:<20} | {mhs["nama"]:<30} | {mhs["alamat"]:<20}')
        i+=1

def insert_mhs(mahasiswa):
    #fungsi ini digunakan untuk insert data mahasiswa
    print("-----fungsi insert data mahasiswa dijalankan-----")

def update_mhs(mahasiswa):
    #fungsi ini digunakan untuk melakukan update data mahasiswa
    print("---- fungsi update mahasiswa dijalankan----")

def delete_mhs(mahasiswa):
    #fungsi ini digunakan untuk delete data mahasiswa
    print("-----fungsi delete mahasiswa dijalankan-----")


def input_nilai(nilai):
    #fungsi untuk input nilai
    print("----fungsi input nilai mahasiswa dijalankan----")
    
def edit_nilai():
    #fungsi ini digunakan untuk mengedit nilai mahasiswa berdasarkan nim yang dimasukkan
    print("-----fungsi edit nilai mahasiswa dijalankan-----")

def tampil_nilai_mahasiswa():
    #fungsi ini digunakan untuk menampilkan data nilai semua mahasiswa
    print("------fungsi tampil nilai mahasiswa dijalankan----")

def insert_krs():
    #fungsi ini digunakan untuk menambah data krs mahasiswa
    print("------fungsi insert krs dijalankan-----")

def update_krs():
    #fungsi ini digunakan untuk mengubah data krs mahasiswa
    print("------fungsi update krs dijalankan------")

def show_krs():
    #fungsi ini digunakan untuk menampilkan data krs mahasiswa
    print("------fungsi show krs dijalankan---------")

def delete_krs():
     #fungsi ini digunakan untuk menghapus data krs mahasiswa
    print("------fungsi delete krs dijalankan---------")

if __name__ == "__main__":
    mahasiswa = {
        0 : {'nim':'A11.2000.00001','nama':'John Doe','alamat':'Jalan Nakula I 5-11 Semarang'},
        1 : {'nim':'A11.2000.00002','nama':'Jane Defoe','alamat':'Jalan Siliwangi 65 Semarang'},
    }

    nilai = {
        0 : {'A11.2000.00001':80},
    }

    krs = {
        0 : {'A11.2000.00001':'Daspro','sks':3},
        1 : {'A11.2000.00001':'Pancasila','sks':2},
    }

    
