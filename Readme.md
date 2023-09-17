# Testing Data Infrastructure & Analysis
Silahkan mengerjakan sesuai kemampuan Anda, Deadline 18 September 2023, jam 10:00 WIB. Fork repository ini, kirim "Pull Request" jika anda sudah selesai atau kirim email ke royyan@satunol.com.
## Kuis

- [?] Anda memiliki tabel "Orders" dengan kolom-kolom berikut: "OrderID," "CustomerID," "OrderDate," dan "TotalAmount." Tuliskan sebuah kueri SQL untuk menampilkan semua pesanan yang dibuat oleh pelanggan dengan ID tertentu pada tanggal tertentu.

  Jawab :

  ```
  SELECT *
  FROM Orders
  WHERE (CustomerID = ....) AND (OrderDate = '....')
  ```
  atau
  ```
  SELECT *
  FROM Orders
  WHERE (CustomerID = ....) AND (OrderDate BETWEEN '...' AND '...')
  ```
- [?] Bagaimana Anda akan mengimplementasikan pengolahan data real-time dalam infrastruktur data? Berikan contoh kasus penggunaan di mana pengolahan data real-time sangat penting.

  Jawab :

  Data yang dikumpulkan secara real time dari aplikasi maupun sumber data lainnya dapat diproses dengan bantuan stream processor yang nantinya bisa disimpan di database atau langsung ke tools untuk analitik seperti Power BI, Tableau, dsb. Real time data sangat penting untuk proses yang membutuhkan respon cepat, contohnya untuk aplikasi pembelian atau pembayaran. Bisa juga digunakan untuk memonitor proses bisnis agar dapat mengambil tindakan atau membuat prediksi tren kedepannya dengan lebih cepat dan akurat.
- [?] Mengapa keamanan data sangat penting dalam infrastruktur data? Sebutkan beberapa langkah atau teknik yang dapat digunakan untuk melindungi data yang disimpan dan diproses.

  Jawab :

  Karena data bisa saja berisi informasi yang confidental seperti data pribadi karyawan atau customer yang apabila bocor dapat disalahgunakan oleh pihak yang tidak bertanggung jawab. Cara untuk melindungi data bisa dengan membatasi akses, menggunakan firewall, menggunakan enkripsi, dan metode-metode lainnya.
- [?] Bagaimana Anda akan menangani situasi di mana server database mengalami gangguan atau kegagalan yang mengancam kontinuitas operasional? Jelaskan tindakan darurat yang akan Anda lakukan.

  Jawab :

  Yang pertama kali dilakukan terkait isu kegagalan pada database adalah mempersiapkan sistem dengan baik seperti melakukan pencadangan database secara berkala sehingga nantinya dapat dipulihkan apabila pada server utama terjadi kegagalan yang bisa berujung pada hilangnya data. Kemudian apabila terjadi mmasalah pada server, perlu dilakukan troubleshoot untuk melihat root dari masalahnya dan menentukan apa yang harus dilakukan. Bisa juga dengan mengecek apa server database sedang running atau tidak, mereset password database, atau menggunakan VPN.
- [?] Bagaimana Anda akan merencanakan dan mengembangkan infrastruktur data yang lebih besar untuk mendukung pertumbuhan bisnis? Jelaskan tahapan utama yang akan Anda lakukan.

  Jawab :
  
  Pertama adalah mempelajari ke arah mana bisnis akan bergerak, kemudian mencatat data apa saja yang akan dibutuhkan dan dari mana sumber data akan diperoleh. setelah itu mendesain struktur database termasuk isi data tiap tabel dan hubungan antar tabel. Kemudian merencanakan sistem untuk mengekstrak dan menyimpan datanya, ketika sistem sudah terbentuk lalu dilakukan testing untuk melihat apa sistem dan output yang dihasilkan sesuai dengan perencanaan.
- [?] Mengapa visualisasi data penting dalam analisis data? Berikan contoh alat atau teknik yang biasa digunakan untuk membuat visualisasi data yang efektif.

  Jawab :

  Visualisasi data membantu user untuk lebih mudah dan lebih cepat melihat tren pada data. Alat yang bisa digunakan untuk visualisasi data antara lain Excel, Power BI, Tableau, dan Lookers Studio. Macam-macam diagram yang digunakan untuk visualisasi data diantaranya:
  -  Scatter plot    =  untuk melihat korelasi dari 2 variabel
  -  Bar chart       =  untuk melihat komparasi dari berbagai item
  -  Line chart      =  untuk melihat tren naik/turun secara historis
  -  Pie chart       =  untuk melihat proporsi tiap item dari total keseluruhan
  -  dsb.
- [?] Jelaskan apa yang anda ketahui tentang: Race Condition, Deadlock, Indexing, Normalization, Replication, Backup and Restore, Data Migration dalam database. Jelaskan juga pengalaman anda yang pernah anda hadapi berhubungan dengan istilah-istilah tersebut.

  Jawab :
  -  Race Condition  = jika ada banyak user yang ingin melakukan perubahan pada database di waktu yang sama, maka yang prosesnya selesai duluan yang akan terproses dan yang lainnya akan mengalami error
  -  Deadlock        = ketika ada 2 atau lebih proses yang menunggu satu sama lain untuk menyelesaikan prosesnya sehingga semua proses tidak akan bisa selesai
  -  Indexing            = penandaan pada database untuk mempermudah pencarian data
  -  Normalization       = mengelompokkan data, misal data user dikumpulkan dalam satu tabel, data produk dikumpulkan dalam satu tabel.
  -  Replication         = mengcopy data dari suatu database untuk disimpan di tempat lain dan dijaga konsistensinya
  -  Backup and Restore  = pencadangan database secara berkala sehingga ketika terjadi kegagalan database dan kehilangan data maka data bisa dipulihkan dari cadangan yang telah dibuat
  -  Data Migration      = memindahkan data dari suatu database ke database baru
 
  Pengalaman yang pernah dialami : perusahaan memiliki beberapa platform dan ingin agar data dari tiap platform dapat terintegrasi dengan mudah, akhirnya diputuskan untuk membuat database baru dan melakukan migrasi data untuk menggabungkan data dari berbagai platform ke dalam satu database. Yang saya lakukan sebagai data analis adalah menentukan data apa saja dari masing-masing platform yang perlu dimigrasi ke database baru, kemudian melakukan penataan struktur database dan melakukan testing untuk melihat apakah data yang tersimpan sudah benar atau belum

## Alghoritma
Kerjakan dengan menggunakan bahasa pemograman yg anda kuasai, buat folder terpisah untuk soal ini
- [!] Anda memiliki dua buah array, yaitu DATA dan QUERIES, tentukan berapa kali setiap kata dalam QUERIES muncul dalam array DATA. Buatlah sebuah fungsi atau program untuk menghasilkan output yang berisi jumlah kemunculan setiap kata dalam QUERIES dalam DATA. 
Contoh:  
```
DATA = ['aple', 'banana', 'cherry', 'banana', 'apple']
QUERIES = ['apple', 'banana', 'grape']

# Fungsi atau program Anda akan menghasilkan output berupa list, seperti ini:
# [2, 2, 0]

# Penjelasan:
# - Kata 'apple' muncul 2 kali dalam DATA.
# - Kata 'banana' juga muncul 2 kali dalam DATA.
# - Kata 'grape' tidak muncul sama sekali dalam DATA.
```
- [!] Silahkan cari hasil dari pengurangan dari jumlah diagonal sebuah matrik NxN Contoh:

Contoh:
```
Matrix = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]

diagonal pertama = 1 + 5 + 9 = 15 
diagonal kedua = 0 + 5 + 7 = 12 

maka hasilnya adalah 15 - 12 = 3
```

- [!] Dengan menggunakan [Mapbox](https://docs.mapbox.com/help/glossary/mapbox-gl-js/) tambahkan polygon pada peta dengan tiga garis warna yang berbeda. 

![Contoh gambar.](mapbox.jpg)

## Challenge
Rancang solusi untuk mengolah data streaming secara real-time, seperti data sensor dari perangkat IoT. Rinci alat atau teknologi yang akan digunakan, serta langkah-langkah yang akan diambil dalam mengatasi masalah data streaming. Tambahkan link figma atau canva untuk mendukung penjelasan konsep anda dengan gambar flowchart yang baik.

Jawab : https://www.canva.com/design/DAFuhX17lMo/rklD2o-mnmaiIrat06ISKw/view?utm_content=DAFuhX17lMo&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink
