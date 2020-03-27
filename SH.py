#SH.py
import os, sys, time
os.system('clear')
def main (kata):
        for e in kata:
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.2)
print ("""
\033[1;91m      ____  _   _ _____ _     _     
     / ___|| | | | ____| |   | |    
     \___ \| |_| |  _| | |   | |    
\033[1;37m      ___) |  _  | |___| |___| |___ 
     |____/|_| |_|_____|_____|_____|
               \033[1;33mversi \033[1;92m9.9
""")
print ("\033[1;91m[\033[1;37m=======================================\033[1;91m]")
main("""
        \033[1;37mSelamat datang Gaess \033[1;92m>_

   \033[1;37mSemoga bermanfaat buat kalian \033[1;92m>_<

""")
print ("\033[1;91m[\033[1;37m=======================================\033[1;91m]")
nama = input('\033[1;34m( \033[1;33mSTAR \033[1;34m) \033[1;92m--> \033[1;91mEnter \033[1;92m: ')
time.sleep(3)
print ('\n')
main('  \033[1;92mLoading\033[1;37m....')
time.sleep(4)
os.system('clear')
print ("""
       \033[1;91m(\033[1;33mAuthor\033[1;91m) \033[1;92m: \033[1;37mM_aref

       \033[1;34m(\033[1;37mYoutub\033[1;34m) \033[1;92m: \033[1;33mThe-X-Cyber
""")
main("""
\033[1;37mStep by step Programming with Bash Shell
=======================================
Sama halnya dengan pemrograman lainnya, Bash Shell programming juga dapat melakukan fungsi-fungsi seperti baca input, tulis output, looping, condition statement, dan sebagainya. Berikut adalah langkah-langkah untuk membuat script bash programming
=======================================
1.Masuk ke terminal

2.Login sebagai root (kita bisa membuat script tanpa harus login sebagai root)

3.Buat script dengan format .sh pada direktori yang diinginkan dengan syntax .ssh

contoh:
=======================================
keterangan syntax:

vi : untuk membuka editor vi yang akan digunakan untuk menuliskan script. Penggunaan vi dapat diganti dengan editor lain seperti pico, nano, dan sebagainya
test : nama file
.sh : format data standard yang digunakan dalam bash programming
=======================================
4.Buat script pada editor. Tekan key Insert terlebih dahulu sebelum menulikan script pada editor. Berikut adalah contoh program sederhana

Setelah selesai menuliskan script, tekan key Esc untuk keluar dari editor lalu masukkan mode yang diinginkan. Ada beberapa mode yang dapat dilakukan saat akan keluar dari editor:
=======================================
– :q keluar editor. Jika ada perubahan, maka akan muncul peringatan
– :q! keluar editor tanpa menyimpan perubahan
– :wq: keluar editor dengan menyimpan perubahan yang dilakukan
=======================================
5.Setelah menyimpan perubahan dengan perintah wq ubah dulu mode dari script agar bisa dieksekusi dengan perintah chmod ut, jalankan script dengan perintah ./namafile, seperti terlihat dibawah ini
=======================================
Menambah user baru dari file

1.Buat file userlist.txtyang berisi daftar nama user baru yang ingin dibuat

2.Buat file script dengan nama adduser.sh. Tulis script berikut pada editor

Penjelasan script:
Sistem akan membaca daftar nama user baru yang disimpan dalam file userlist.txtsatu per satu dan disimpan dalam variabel $0. Setelah itu sistem akan menjalankan perintah useradd -m $0 hingga nama user terakhir.
=======================================
3.Ubah mode file adduser.shdengan perintah chmod u+x adduser.shkemudian eksekusi program dengan perintah ./adduser.sh

4.Cek apakah semua nama user baru telah dibuat dengan perintah cat /etc/group
=======================================
Mengubah masa aktif password dari anggota grup

Biasanya sys admin harus mengatur masa aktif password satu per satu untuk setiap user dengan menjalankan perintah chage. Bayangkan jika terdapat 1000 user yang harus diubah masa aktif password nya. Tentu pekerjaan tersebut membutuhkan waktu yang lama. Namun dengan membuat sebuah script, proses tersebut dapat diotomisasi. Berikut adalah contoh script untuk mengubah masa aktif user dalam suatu grup.
a. Buat file script dengan nama test.sh. Tulis script berikut pada editor
=======================================
Penjelasan script:
Sistem akan mengambil semua nama user dalam grup MURID kemudian disimpan dalam filelistuser.txt. Selanjutkan sistem akan membaca nama user satu per satu dari fileuser.txt dan disimpan dalam variabel $0. Setelah itu sistem akan menjalankan perintah chage -M 100 $0 hingga nama user terakhir. Karena listuser.txt hanya file sementara yang digunakan untuk membantu program ini, maka setelah program selesai file tersebut dihapus.
=======================================
1.Ganti mode file agar dapat dieksekusi

2.Eksekusi program
=======================================
Mencari file dengan ekstensi tertentu ada dalam sebuah direktori

1.buat file script dengan nama test01.sh. Tulis script berikut pada editor

Penjelasan script:
Program di atas akan melakukan pengecekan apakah dalam suatu direktori terdapat file dengan ekstensi .txt atau tidak. Jika ada file dengan format txt maka akan ditampilkan pesan “File(s) exists.”. Sebalikanya jika tidak ada maka akan muncul pesan “File does not exist”.
=======================================
2.Ubah mode file test01.sh kemudian eksekusi file tersebut seperti yang telah dijelaskan di atas.
=======================================
Penggunaan Array dan For Loop

Potongan script di atas menunjukan cara penggunaan array dan for loop dalam bash programming. Program tersebut akan membaca isi file kemudian disimpan dalam sebuah array. selanjutnya isi file tersebut akan ditampilkan oleh program sebagai output. Untuk mengeksekusi program tersebut jalankan perintah ./. Berikut adalah contoh keluaran program tersebut.
=======================================
Membandingkan variabel

Potongan script di atas menunjukan cara membandingkan dua buah variabel dalam bash programming. Disini hanya dicontohkan 2 tipe variabel yaitu integer (NUM1 dan NUM2) serta string (S1 dan S2). Berikut contoh keluaran dari program tersebut.
=======================================
""")
time.sleep(4)
os.system("python3 SH.py")
