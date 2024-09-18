from tabulate import tabulate
from colorama import Fore, init
init(autoreset=True)

# Data Pengguna (Dictionary)
data_pengguna = {
    'admin': {'password': 'admin', 'role': 'Administrator'},
    'lecture': {'password': 'lecture', 'role': 'Lecture'},
    'student': {'password': 'student', 'role': 'Student'}
}

# Data Siswa (Dictionary)
data_siswa = {
    "0001": {"nama": "Joko Sampurno", "program": "Data Science",
             "exam1": 85, "cp1": 90, "exam2": 88, "cp2": 92, "exam3": 87, "cp3": 93},
    "0002": {"nama": "Raka Mulyono", "program": "Digital Marketing",
             "exam1": 78, "cp1": 82, "exam2": 80, "cp2": 85, "exam3": 79, "cp3": 84},
    "0003": {"nama": "Bowo Charlie", "program": "Web Development",
             "exam1": 90, "cp1": 88, "exam2": 92, "cp2": 89, "exam3": 94, "cp3": 91},
    "0004": {"nama": "Michael Rahman", "program": "Digital Marketing",
             "exam1": 81, "cp1": 85, "exam2": 83, "cp2": 88, "exam3": 80, "cp3": 86},
    "0005": {"nama": "Sarah Putri", "program": "Web Development",
             "exam1": 88, "cp1": 90, "exam2": 91, "cp2": 87, "exam3": 89, "cp3": 90}
}

# Fungsi login
def login():
    print(Fore.MAGENTA + '''
          ===============================================================
                SELAMAT DATANG DI PANGKALAN DATA NILAI SISWA (PDNS)
                                PURWADHIKA JAKARTA
          ===============================================================
          
Silakan melakukan login terlebih dahulu.
          ''')
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in data_pengguna and data_pengguna[username]['password'] == password:
        print(Fore.GREEN + f"Login berhasil sebagai {username} ({data_pengguna[username]['role']}).\n")
        return data_pengguna[username]['role'], username
    elif username in data_siswa and password == username:
        print(Fore.GREEN + f"Login berhasil sebagai {username} (Student).\n")
        return 'Student', username
    else:
        print(Fore.RED + "Username atau password salah.\n")
        while True:
            print("1. Coba lagi")
            print("2. Keluar")
            pilihan = input("\nPilih opsi (1-2): ")
            if pilihan == '1':
                return login()
            elif pilihan == '2':
                print(Fore.YELLOW + "Terima kasih! Program selesai.\n")
                exit()
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.\n")

# Fungsi generate tabel data siswa
def generate_tabel_siswa(data_siswa, id_siswa=None):
    tabel_data = []
    
    if id_siswa:
        siswa_list = [id_siswa]

    else:
        siswa_list = data_siswa.keys()
    
    for id_siswa in siswa_list:
        info_siswa = data_siswa[id_siswa]
        
        # Mengambil data exam dan capstone
        exams = [info_siswa['exam1'], info_siswa['exam2'], info_siswa['exam3']]
        capstones = [info_siswa['cp1'], info_siswa['cp2'], info_siswa['cp3']]
        
        # Menghitung rata-rata exam
        valid_exams = [float(x) for x in exams if x != ""]
        avg_exam = sum(valid_exams) / len(valid_exams) if valid_exams else 0.0
        
        # Menghitung rata-rata capstone
        valid_capstones = [float(x) for x in capstones if x != ""]
        avg_capstone = sum(valid_capstones) / len(valid_capstones) if valid_capstones else 0.0
        
        # Memasukkan data ke tabel
        tabel_data.append([
            id_siswa, info_siswa['nama'], info_siswa['program'],
            info_siswa['exam1'], info_siswa['cp1'],
            info_siswa['exam2'], info_siswa['cp2'],
            info_siswa['exam3'], info_siswa['cp3'],
            f"{avg_exam:.2f}", f"{avg_capstone:.2f}"
        ])

    # Header tabel
    headers = ["ID", "Nama", "Program",
               "Exam 1", "Capstone 1",
               "Exam 2", "Capstone 2",
               "Exam 3", "Capstone 3",
               "Rata-rata Exam", "Rata-rata Capstone"]
    
    # Tampilkan tabel
    return tabulate(tabel_data, headers, tablefmt="grid")

# Fungsi menampilkan data siswa
def tampilkan_data_siswa(role, username):
    if data_siswa:
        if role == 'Student':
            # Role Student hanya menampilkan data siswa tersebut
            print()
            print(Fore.GREEN + f"\nData siswa:")
            print(generate_tabel_siswa(data_siswa, username))
        else:
            # Role Administrator atau Lecture, menampilkan semua data siswa
            print(Fore.GREEN + f"\nData siswa:")
            print(generate_tabel_siswa(data_siswa))
            print()
    else:
        print(Fore.YELLOW + "\nBelum ada data siswa.")

# Fungsi menambahkan data siswa
def tambah_data_siswa():
    if data_siswa:
        id_siswa_terakhir = max(int(id_siswa) for id_siswa in data_siswa.keys())
    else:
        id_siswa_terakhir = 0

    while True:
        # Nama tidak boleh kosong
        while True:
            nama = input("\nMasukkan nama siswa baru (ketik '-' untuk kembali ke menu utama): ").title()
            if nama.lower() == '-':
                print()
                return
            elif nama.strip():
                break
            else:
                print(Fore.RED + "Nama tidak boleh kosong. Silakan masukkan nama dengan benar.")
        
        # Program tidak boleh kosong
        while True:
            program = input("\nMasukkan program baru (tidak boleh kosong): ").title()
            if program.strip():
                id_siswa_terakhir += 1
                id_siswa = str(id_siswa_terakhir).zfill(4)
                data_siswa[id_siswa] = {'nama': nama, 'program': program,
                                        "exam1": "", "cp1": "", "exam2": "", "cp2": "", "exam3": "", "cp3": ""}
                print(Fore.GREEN + f"Data siswa baru ditambahkan dengan ID: {id_siswa}\n")
                print(generate_tabel_siswa(data_siswa, id_siswa))
                break
            else:
                print(Fore.RED + "Program tidak boleh kosong. Silakan masukkan program dengan benar.")

# Fungsi untuk mengubah nama dan program siswa
def ubah_data_siswa():
    while True:
        id_siswa = input("\nMasukkan ID siswa yang datanya ingin diubah (ketik '-' untuk kembali ke menu utama): ")
        if id_siswa.lower() == '-':
            print()
            break
        if id_siswa in data_siswa:
            # Tampilkan data siswa sebelum diubah
            print(Fore.GREEN + f"\nData siswa ditemukan:")
            print(generate_tabel_siswa(data_siswa, id_siswa))
            
            # Input nama baru
            nama_baru = input("\nMasukkan nama baru (atau tekan Enter untuk tidak mengubah): ").title()
            if nama_baru.strip():
                data_siswa[id_siswa]['nama'] = nama_baru
            
            # Input program baru
            while True:
                program_baru = input("\nMasukkan program baru (atau tekan Enter untuk tidak mengubah): ").title()
                if program_baru.strip():
                    data_siswa[id_siswa]['program'] = program_baru
                    break
                elif program_baru == '':
                    break
                else:
                    print(Fore.RED + "Program tidak boleh kosong. Silakan coba lagi.")

            print(Fore.GREEN + f"Data siswa '{id_siswa}' diperbarui.\n")
            print(generate_tabel_siswa(data_siswa, id_siswa))
       
        else:
            print(Fore.RED + f"Siswa dengan ID '{id_siswa}' tidak ditemukan.")

# Fungsi input nilai siswa
def input_nilai_siswa():
    while True:
        id_siswa = input("\nMasukkan ID siswa yang nilainya ingin diubah atau input (ketik '-' untuk kembali ke menu utama): ")
        if id_siswa.lower() == '-':
            print()
            break
        
        if id_siswa in data_siswa:
            print(Fore.GREEN + f"\nData siswa ditemukan:")
            print(generate_tabel_siswa(data_siswa, id_siswa))
            
            while True:
                print("\nPilihan nilai:")
                nilai_mapping = {
                    '1': ('Exam 1', 'exam1'),
                    '2': ('Capstone 1', 'cp1'),
                    '3': ('Exam 2', 'exam2'),
                    '4': ('Capstone 2', 'cp2'),
                    '5': ('Exam 3', 'exam3'),
                    '6': ('Capstone 3', 'cp3')
                }

                for k, v in nilai_mapping.items():
                    print(f"{k}. {v[0]}")
                print("Ketik '-' untuk kembali ke input ID siswa.")
                
                pilihan_nilai = input("\nPilih nilai yang ingin diubah atau input (1-6): ")

                if pilihan_nilai.lower() == '-':
                    break

                if pilihan_nilai in nilai_mapping:
                    nilai_label, key = nilai_mapping[pilihan_nilai]
                    while True:
                        nilai_baru = input(f"\nMasukkan nilai baru untuk '{nilai_label}' (atau tekan Enter untuk mengosongkan nilai): ")
                        if nilai_baru == "":
                            data_siswa[id_siswa][key] = ""
                            print(Fore.YELLOW + f"Nilai {nilai_label} untuk {data_siswa[id_siswa]['nama']} dikosongkan.\n")
                            print(generate_tabel_siswa(data_siswa, id_siswa))
                            break
                        else:
                            try:
                                nilai_float = float(nilai_baru)
                                if 0 <= nilai_float <= 100:
                                    data_siswa[id_siswa][key] = nilai_float
                                    print(Fore.GREEN + f"Input nilai {nilai_label} untuk {data_siswa[id_siswa]['nama']} berhasil.\n")
                                    print(generate_tabel_siswa(data_siswa, id_siswa))
                                    break
                                else:
                                    print(Fore.RED + "Nilai harus berada dalam rentang 0-100.\n")
                                    print(generate_tabel_siswa(data_siswa, id_siswa))
                            except ValueError:
                                print(Fore.RED + "Masukkan nilai yang valid.\n")
                                print(generate_tabel_siswa(data_siswa, id_siswa))
                
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
            
            # Tampilkan kembali data siswa setelah input nilai
            print(Fore.GREEN + f"\nData Siswa setelah perubahan nilai:")
            print(generate_tabel_siswa(data_siswa, id_siswa))
        
        else:
            print(Fore.RED + f"Siswa dengan ID '{id_siswa}' tidak ditemukan.")

# Fungsi hapus data siswa
def hapus_data_siswa():
    while True:
        id_siswa = input("\nMasukkan ID siswa yang datanya ingin dihapus (ketik '-' untuk kembali ke menu utama): ")
       
        if id_siswa.lower() == '-':
            break
       
        if id_siswa in data_siswa:
            nama_siswa = data_siswa[id_siswa]['nama']
            print(Fore.GREEN + f"\nData siswa ditemukan:")
            print(generate_tabel_siswa(data_siswa, id_siswa))
            
            while True:
                konfirmasi = input(f"\nApakah Anda yakin ingin menghapus data siswa tersebut? (y/n): ").lower()
                if konfirmasi == 'y':
                    del data_siswa[id_siswa]
                    print(Fore.GREEN + f"Data siswa '{nama_siswa}' berhasil dihapus.")
                    break
                elif konfirmasi == 'n':
                    print(Fore.RED + f"Penghapusan data siswa '{nama_siswa}' dibatalkan.")
                    break
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan masukkan 'y' untuk ya atau 'n' untuk tidak.")
       
        else:
            print(Fore.RED + f"Siswa dengan ID '{id_siswa}' tidak ditemukan.")

# Fungsi untuk mencari data siswa berdasarkan nama atau ID
def cari_data_siswa():
    while True:
        print("\nPilih kriteria:")
        print("1. Cari berdasarkan ID atau Nama siswa")
        print("2. Cari berdasarkan Program siswa")
        print("Ketik '-' untuk kembali ke input ID siswa.")
        
        pilihan = input("\nPilih opsi (1-3): ")

        if pilihan == '1':
            input_cari = input("\nMasukkan ID atau Nama lengkap siswa: ").strip().lower()
            
            # Cari berdasarkan ID atau Nama
            if input_cari.isdigit():
                siswa_ditemukan = {id_siswa: info_siswa for id_siswa, info_siswa in data_siswa.items()
                                   if id_siswa == input_cari}
            else:
                siswa_ditemukan = {id_siswa: info_siswa for id_siswa, info_siswa in data_siswa.items()
                                   if info_siswa['nama'].strip().lower() == input_cari}

            if siswa_ditemukan:
                # Tampilkan data siswa yang ditemukan (bisa berdasarkan ID atau Nama)
                print(Fore.GREEN + f"\nData siswa ditemukan:")
                print(generate_tabel_siswa(siswa_ditemukan))
            else:
                print(Fore.RED + f"Siswa dengan ID atau Nama '{input_cari}' tidak ditemukan.\n")

        elif pilihan == '2':
            program = input("\nMasukkan Program siswa: ").strip().lower()
            siswa_ditemukan = {
                id_siswa: info_siswa for id_siswa, info_siswa in data_siswa.items()
                if info_siswa['program'].strip().lower() == program
            }

            if siswa_ditemukan:
                # Tampilkan semua siswa dengan program yang sesuai
                print(Fore.GREEN + f"\nData siswa dengan Program '{program.title()}':")
                print(generate_tabel_siswa(siswa_ditemukan))
            else:
                print(Fore.RED + f"Tidak ada siswa yang terdaftar dalam program '{program.title()}'.\n")
        
        elif pilihan.lower() == '-':
            print()
            break

        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.\n")

# Fungsi untuk menampilkan menu dan mengarahkan ke fungsi yang sesuai
def menu():
    role, username = login()
    
    if role == 'Administrator':
        while True:
            print(Fore.BLUE + "\n=== MENU UTAMA ===\n")
            print("1. Tampilkan Data Keseluruhan Siswa")
            print("2. Tambah Data Siswa")
            print("3. Ubah Data Siswa")
            print("4. Ubah/Input Nilai Siswa")
            print("5. Hapus Data Siswa")
            print("6. Cari Data Siswa")
            print("7. Keluar")
            
            pilihan = input("\nPilih opsi (1-7): ")
            
            if pilihan == '1':
                tampilkan_data_siswa(role, username)
            elif pilihan == '2':
                tambah_data_siswa()
            elif pilihan == '3':
                ubah_data_siswa()
            elif pilihan == '4':
                input_nilai_siswa()
            elif pilihan == '5':
                hapus_data_siswa()
            elif pilihan == '6':
                cari_data_siswa()
            elif pilihan == '7':
                print(Fore.YELLOW + "Terima kasih! Program selesai.\n")
                break
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
    
    elif role == 'Lecture':
        while True:
            print(Fore.BLUE + "\n=== MENU UTAMA ===\n")
            print("1. Tampilkan Data Keseluruhan Siswa")
            print("2. Ubah/Input Nilai Siswa")
            print("3. Cari Data Siswa")
            print("4. Keluar")
            
            pilihan = input("\nPilih opsi (1-4): ")
            
            if pilihan == '1':
                tampilkan_data_siswa(role, username)
            elif pilihan == '2':
                input_nilai_siswa()
            elif pilihan == '3':
                cari_data_siswa()
            elif pilihan == '4':
                print(Fore.YELLOW + "Terima kasih! Program selesai.\n")
                break
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
    
    elif role == 'Student':
        while True:
            print(Fore.BLUE + "\n=== MENU UTAMA ===\n")
            print("1. Tampilkan Data Nilai Siswa")
            print("2. Keluar")
            
            pilihan = input("\nPilih opsi (1-2): ")
            
            if pilihan == '1':
                tampilkan_data_siswa(role, username)
            elif pilihan == '2':
                print(Fore.YELLOW + "Terima kasih! Program selesai.\n")
                break
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan menu utama
menu()