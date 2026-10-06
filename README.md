**Nama    : Muhammad Raffy Putra Triadi**
**Nim     : 2609116091**
**Kelas   : C**
**Tugas   : Ganjil**

<img width="960" height="540" alt="Screenshot 2026-10-06 202734" src="https://github.com/user-attachments/assets/5f687b2c-768c-4500-a640-ddacb3a06bdb" />
Pada bagian awal program terdapat import json dan import os. json digunakan untuk membaca dan menyimpan data mahasiswa ke dalam file JSON, sedangkan os digunakan untuk mengecek apakah file data sudah tersedia atau belum.
Kalau program kamu memang menggunakan nilai_mahasiswa.json, bagian path sebenarnya tidak perlu digunakan. Supaya lebih rapi, cukup gunakan file_data.

<img width="960" height="540" alt="Screenshot 2026-10-06 201600" src="https://github.com/user-attachments/assets/40beecee-e2d1-4205-9725-c8aa3125db99" />
<img width="960" height="540" alt="Screenshot 2026-10-06 201617" src="https://github.com/user-attachments/assets/f417a83b-5de4-4bc9-97de-8ba3d45f8582" />
Program ini menggunakan library json untuk membaca dan menyimpan data mahasiswa dalam file JSON. Library os digunakan untuk mengecek apakah file nilai_mahasiswa.json sudah tersedia atau belum. Jika file belum ada, program akan menganggap belum terdapat data.
Function baca_data() digunakan untuk membaca semua data yang ada di dalam file JSON. Function tampilkan_data() digunakan untuk menampilkan seluruh data nilai mahasiswa yang sudah tersimpan. Sedangkan function tambah_data() digunakan untuk memasukkan data mahasiswa baru seperti NIM, nama, mata kuliah, dan nilai.
Setelah data baru dimasukkan, data tersebut ditambahkan menggunakan append(). Selanjutnya seluruh data disimpan kembali ke file menggunakan json.dump(). Karena data lama tetap ikut disimpan, data yang sebelumnya ada tidak akan terhapus.
Pada bagian akhir program terdapat while True yang membuat menu terus berjalan. Program akan berhenti ketika pengguna memilih menu 3. Keluar dengan menggunakan break.

<img width="960" height="540" alt="Screenshot 2026-10-06 201526" src="https://github.com/user-attachments/assets/35845773-0c9e-4d52-8663-87efa785d495" />
program Sistem Pencatatan Nilai Mahasiswa sedang dijalankan melalui terminal. Saat program pertama dijalankan, saya memilih menu nomor 1 untuk melihat data nilai yang sudah tersimpan. Data yang muncul yaitu NIM 2609116091 atas nama Muhammad Raffy, mata kuliah Algoritma dan Pemrograman, dengan nilai 85.
Setelah itu saya memilih menu nomor 2 untuk mencoba menambahkan data nilai baru. Program meminta saya mengisi NIM, nama, mata kuliah, dan nilai. Setelah semua data diisi, muncul tulisan “Data berhasil ditambahkan dan disimpan.” yang menunjukkan bahwa data sudah berhasil dimasukkan ke dalam file JSON. Setelah proses tersebut selesai, menu program muncul kembali sehingga program masih bisa digunakan untuk melihat atau menambahkan data lainnya.
Screenshot ini juga menunjukkan bahwa program sudah berjalan menggunakan while loop, karena setelah melakukan satu proses program tidak langsung berhenti dan kembali menampilkan menu. Jadi, user bisa melakukan beberapa proses sampai memilih menu 3. Keluar.

<img width="960" height="540" alt="Screenshot 2026-10-06 201635" src="https://github.com/user-attachments/assets/1d9ca879-3674-4cda-a158-94a659b59fae" />
Pada isi file studikasus6 Mraffypt.json yang digunakan untuk menyimpan data nilai mahasiswa. Di dalam file tersebut terdapat tiga data mahasiswa, yaitu Muhammad Raffy dengan mata kuliah Algoritma dan Pemrograman dan nilai 85, Andi dengan mata kuliah Basis Data dan nilai 90, serta Budi dengan mata kuliah Pemrograman Python dan nilai 88. Setiap data memiliki empat bagian, yaitu nim, nama, mata_kuliah, dan nilai.
Data tersebut disimpan dalam bentuk JSON menggunakan tanda kurung siku [] yang menandakan kumpulan data. Setiap data mahasiswa ditulis di dalam kurung kurawal {} dan dipisahkan dengan tanda koma. Dari isi file ini juga bisa dilihat bahwa data baru seperti Andi dan Budi sudah masuk ke dalam file, sehingga data tidak hanya muncul di terminal tetapi benar-benar tersimpan di file JSON. Ini menjadi bukti bahwa program sudah berhasil menyimpan data nilai secara permanen.
