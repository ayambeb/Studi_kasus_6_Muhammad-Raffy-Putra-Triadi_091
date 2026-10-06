import json
import os
path = r"D:\PRATIKUM\studikasus6 Mraffypt.json"

file_data = "nilai_mahasiswa.json"


def baca_data():
    if not os.path.exists(file_data):
        return []

    with open(file_data, "r") as file:
        return json.load(file)


def tampilkan_data():
    data = baca_data()

    if len(data) == 0:
        print("\nBelum ada data nilai.")
    else:
        print("\n=== DATA NILAI MAHASISWA ===")
        for i, mahasiswa in enumerate(data, 1):
            print(f"{i}. NIM       : {mahasiswa['nim']}")
            print(f"   Nama      : {mahasiswa['nama']}")
            print(f"   Mata Kuliah : {mahasiswa['mata_kuliah']}")
            print(f"   Nilai     : {mahasiswa['nilai']}")
            print()


def tambah_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    mata_kuliah = input("Masukkan Mata Kuliah: ")
    nilai = input("Masukkan Nilai: ")

    data = baca_data()

    data_baru = {
        "nim": nim,
        "nama": nama,
        "mata_kuliah": mata_kuliah,
        "nilai": nilai
    }

    data.append(data_baru)

    with open(file_data, "w") as file:
        json.dump(data, file, indent=4)

    print("\nData berhasil ditambahkan dan disimpan.")


while True:
    print("\n=== SISTEM PENCATATAN NILAI MAHASISWA ===")
    print("1. Tampilkan Data Nilai")
    print("2. Tambah Data Nilai")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        tambah_data()

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")