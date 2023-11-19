pegawai = [{'Kode Pegawai': 'A001', 'Nama': 'Marheike Bawolye, M.Pd', 'Pendidikan Terakhir': 'Magister', 'Jabatan': 'Kepala Sekolah', 'Status Pegawai': 'PNS'},
        {'Kode Pegawai': 'B001', 'Nama': 'Anna Alamri, M.Pd', 'Pendidikan Terakhir': 'Magister', 'Jabatan': 'Guru', 'Status Pegawai': 'PNS'},
        {'Kode Pegawai': 'B002', 'Nama': 'Sukma Gubali, S.Pd', 'Pendidikan Terakhir': 'Sarjana', 'Jabatan': 'Guru', 'Status Pegawai': 'HONORER'},
        {'Kode Pegawai': 'C001', 'Nama': 'Sri Gita Djafar, S.E', 'Pendidikan Terakhir': 'Sarjana', 'Jabatan': 'Tata Usaha', 'Status Pegawai': 'HONORER'}]


#Membuat Menu Read Data
def ReadData(pegawai):
    while True:
        print('\n======Data Pegawai SMP Negeri 1 Mananggu======\n')
        print('1. Data Seluruh Pegawai')
        print('2. Data Pegawai Tertentu')
        print('3. Kembali Ke Menu Utama')
        read = input('Masukkan pilihan menu anda (1-3):')

        if read == '1':
            if len(pegawai) != 0: #memeriksa apakah data ada atau tidak
                print('Daftar Data Pegawai')
                # Header tabel
                print(f"| {'Kode Pegawai':^15} | {'Nama':^30} | {'Pendidikan Terakhir':^20} | {'Jabatan':^20} | {'Status Pegawai':^15} |")
                
                # Isi tabel
                for i in pegawai: #iterasi elemen dalam list pegawai
                    kode_pegawai = i['Kode Pegawai']
                    nama = i['Nama']
                    pendidikan = i['Pendidikan Terakhir']
                    jabatan = i['Jabatan']
                    status_pegawai = i['Status Pegawai']
                    print(f"| {kode_pegawai:^15} | {nama:^30} | {pendidikan:^20} | {jabatan:^20} | {status_pegawai:^15}|")
            else:
                print('\n---Data Pegawai Tidak Ditemukan---')

                    
        elif read == '2':
            if len(pegawai) != 0:
                id = input('Masukkan Kode Pegawai:').upper() 
                hasil = False #melacak data ada atau tidak
                #iterasi elemen menggunakan enumerasi
                for j, i in enumerate(pegawai): 
                    if i['Kode Pegawai'] == id:
                        # Header tabel
                        print(f"\n| {'Kode Pegawai':^15} | {'Nama':^30} | {'Pendidikan Terakhir':^20} | {'Jabatan':^20} | {'Status Pegawai':^15} |")

                        # Isi tabel untuk pegawai tertentu
                        kode_pegawai = i['Kode Pegawai']
                        nama = i['Nama']
                        pendidikan = i['Pendidikan Terakhir']
                        jabatan = i['Jabatan']
                        status_pegawai = i['Status Pegawai']

                        print(f"| {kode_pegawai:^15} | {nama:^30} | {pendidikan:^20} | {jabatan:^20} | {status_pegawai:^15}|")
                
            
            else:
                print('\n----Data Pegawai Tidak Ditemukan----')
        
        elif read == '3':
            break
        else:
            print('\n-----Pilihan Menu Tidak Valid-----')
            continue


# Menambahkan Data Pegawai
def CreatData (pegawai) :
    while True :
        print ('\n======Data Pegawai SMP Negeri 1 Mananggu======\n')
        print ('1. Menambah Data Pegawai')
        print ('2. Kembali Ke Menu Utama')
        creat = input ('Masukkan pilihan menu anda (1-2) :') 
        
        #menambah data pegawai
        if creat == '1' :
            kode_pegawai=input('Masukan Kode Pegawai : ').upper ()

            #mengecek apakah kode pegawai sudah ada dalam data awal
            for i in pegawai :
                if i ['Kode Pegawai'] == kode_pegawai :
                    print ('\n----Data Sudah Ada----\n')
                    break

            else :
                nama=input('Masukkan Nama Lengkap : ').title()
                pendidikan=input('Masukkan Pendidikan Terakhir :').title()
                jabatan =input ('Masukkan Jabatan :').title()
                status=input('Masukkan Status Pegawai (PNS/HONORER) :').upper()

                data_pegawai = {
                    'Kode Pegawai' : kode_pegawai,
                    'Nama' : nama, 
                    'Pendidikan Terakhir' : pendidikan,
                    'Jabatan' : jabatan,
                    'Status Pegawai' : status}
                
                cek = input ('\nApakah Data Ini akan disimpan? (Yes/No) : ').upper()
                if cek == 'YES' :
                    pegawai.append(data_pegawai)
                    print ('\n------Data Berhasil Disimpan-----')
                else :
                    break
        elif creat == '2' :
            return
        else :
             print ('Pilihan tidak valid. Silahkan pilih 1 atau 2')
            

#Update data pegawai
def updateData(pegawai):
    while True:
        print('\n======Data Pegawai SMP Negeri 1 Mananggu======\n')
        print('1. Mengubah Data Pegawai')
        print('2. Kembali Ke Menu Utama')
        update = input('Masukkan pilihan menu anda (1-2): ')

        if update == '1':
            kode_pegawai = input('Masukkan Kode Pegawai yang akan diupdate: ').upper()
            data_ditemukan = False
            for i, data in enumerate(pegawai):
                if data['Kode Pegawai'] == kode_pegawai:
                    data_ditemukan = True

                    print('\nData Pegawai Sebelum Update:')
                    # Header tabel
                    print(f"| {'Kode Pegawai':^15} | {'Nama':^30} | {'Pendidikan Terakhir':^20} | {'Jabatan':^20} | {'Status Pegawai':^15} |")

                    # Isi tabel sebelum update
                    kode_pegawai = data['Kode Pegawai']
                    nama = data['Nama']
                    pendidikan = data['Pendidikan Terakhir']
                    jabatan = data['Jabatan']
                    status_pegawai = data['Status Pegawai']

                    print(f"| {kode_pegawai:^15} | {nama:^30} | {pendidikan:^20} | {jabatan:^20} | {status_pegawai:^15} |")

                    cek = input('\nApakah anda ingin melakukan update data? (Yes/No): ').upper()
                    if cek == 'YES':
                        edit_kolom = input('Masukkan Kolom yang Ingin diubah (Nama / Pendidikan Terakhir / Jabatan / Status Pegawai): ').title()
                        if edit_kolom in data:
                            new_value = input(f'Masukkan {edit_kolom} baru: ').title()
                            pegawai[i][edit_kolom] = new_value

                            # Menampilkan data setelah update
                            print('\nData Pegawai Setelah Update:')
                            # Header tabel
                            print(f"| {'Kode Pegawai':^15} | {'Nama':^30} | {'Pendidikan Terakhir':^20} | {'Jabatan':^20} | {'Status Pegawai':^15} |")

                            # Isi tabel setelah update
                            kode_pegawai = pegawai[i]['Kode Pegawai']
                            nama = pegawai[i]['Nama']
                            pendidikan = pegawai[i]['Pendidikan Terakhir']
                            jabatan = pegawai[i]['Jabatan']
                            status_pegawai = pegawai[i]['Status Pegawai']

                            print(f"| {kode_pegawai:^15} | {nama:^30} | {pendidikan:^20} | {jabatan:^20} | {status_pegawai:^15} |")

                            print('\n-----Data Telah Berhasil di Update-----')

                        else:
                            print('\n*****Kolom Data Salah atau Tidak Ditemukan*****')
                    break

            if not data_ditemukan:
                print('\n---Data Tidak Ditemukan---')

        elif update == '2':
            return
        else:
            print('\nPilihan tidak valid. Silahkan pilih 1 atau 2')



# menghapus data pegawai
def deleteData(pegawai):
    while True:
        print('\n======Data Pegawai SMP Negeri 1 Mananggu======\n')
        print('1. Hapus Data Pegawai')
        print('2. Kembali Ke Menu Utama')
        delete = input('Masukkan pilihan menu anda (1-2): ')

        if delete == '1':
            kode_pegawai = input('Masukkan Kode Pegawai yang akan dihapus: ').upper()
            data_ditemukan = False

            for i, data in enumerate(pegawai):
                if data['Kode Pegawai'] == kode_pegawai:
                    data_ditemukan = True
                    print('\nData Pegawai Sebelum Dihapus:')
                    print(f"| {'Kode Pegawai':^15} | {'Nama':^30} | {'Pendidikan Terakhir':^20} | {'Jabatan':^20} | {'Status Pegawai':^15} |")
                    print(f"| {data['Kode Pegawai']:^15} | {data['Nama']:^30} | {data['Pendidikan Terakhir']:^20} | {data['Jabatan']:^20} | {data['Status Pegawai']:^15} |")

                    cek = input('\nApakah anda yakin ingin menghapus data ini? (Yes/No): ').upper()
                    if cek == 'YES':
                        del pegawai[i]
                        print('\n-----Data Telah Berhasil dihapus-----')
                        break
                    else:
                        print('\n-----Penghapusan Data Dibatalkan-----')
                        break

            if not data_ditemukan:
                print('\n---Data Tidak Ditemukan---')

        elif delete == '2':
            return

        else:
            print('Pilihan tidak valid. Silahkan pilih 1 atau 2')


# Filter Data
def filterData(pegawai):
    while True:
        print('\n======Data Pegawai SMP Negeri 1 Mananggu======\n')
        print('1. Filter Data Pegawai')
        print('2. Kembali Ke Menu Utama')
        filter_menu = input('Masukkan pilihan menu anda (1-2): ')

        if filter_menu == '1':
            print('\n======Filter Data Pegawai SMP Negeri 1 Mananggu======\n')
            print('1. Filter Data Berdasarkan Huruf Awalan Nama')
            print('2. Filter Data Berdasarkan Pendidikan Terakhir')
            print('3. Filter Data Berdasarkan Jabatan')
            print('4. Filter Data Berdasarkan Status Pegawai')
            print('5. Kembali Ke Menu Utama')
            pilihan_filter = input('Masukkan pilihan menu anda (1-5): ')

            # Filter nama berdasarkan awalan huruf
            if pilihan_filter == '1':
                huruf_awalan = input('Masukkan Huruf Awalan Nama: ').upper()
                filtered_data = filter(lambda data: data['Nama'].startswith(huruf_awalan), pegawai)
                print_filtered_data(filtered_data)
                

            # Filter berdasarkan pendidikan terakhir
            elif pilihan_filter == '2':
                pendidikan = input('Masukkan Pendidikan Terakhir: ').title()
                filtered_data = filter(lambda data: data['Pendidikan Terakhir'] == pendidikan, pegawai)
                print_filtered_data(filtered_data)

            # Filter berdasarkan jabatan
            elif pilihan_filter == '3':
                jabatan = input('Masukkan Jenis Jabatan: ').title()
                filtered_data = filter(lambda data: data['Jabatan'] == jabatan, pegawai)
                print_filtered_data(filtered_data)

            # Filter berdasarkan status pegawai
            elif pilihan_filter == '4':
                status = input('Masukkan Status Pegawai: ').capitalize()
                filtered_data = filter(lambda data: data['Status Pegawai'].capitalize() == status.capitalize() or data['Status Pegawai'].upper() == status.upper(), pegawai)
                print_filtered_data(filtered_data)


            elif pilihan_filter == '5':
                break
            else:
                print('Pilihan tidak valid. Silahkan pilih 1-5.')

        elif filter_menu == '2':
            break
        else:
            print('Pilihan tidak valid. Silahkan pilih 1 atau 2.')


def print_filtered_data(filtered_data):
    filtered_list = list(filtered_data)
    
    if not filtered_list:
        print('\n---Data tidak ditemukan---')
    else:
        # Header tabel
        print(f"| {'Kode Pegawai':^15} | {'Nama':^30} | {'Pendidikan Terakhir':^20} | {'Jabatan':^20} | {'Status Pegawai':^15} |")

        # Isi tabel
        for data in filtered_list:
            kode_pegawai = data['Kode Pegawai']
            nama = data['Nama']
            pendidikan = data['Pendidikan Terakhir']
            jabatan = data['Jabatan']
            status_pegawai = data['Status Pegawai']
            print(f"| {kode_pegawai:^15} | {nama:^30} | {pendidikan:^20} | {jabatan:^20} | {status_pegawai:^15}|")


while True :
    Menu=input('''
    \n======Menu Data Pegawai SMP Negeri 1 Mananggu======\n
    1. Data Pegawai
    2. Menambahkan Data Pegawai
    3. Mengubah Data Pegawai
    4. Menghapus Data Pegawai
    5. Menyaring Data Pegawai
    6. Keluar
    
    Masukkan angka menu yang Anda pilih (1/6): ''')
    if(Menu =='1'):
       ReadData(
           pegawai)
    elif (Menu == '2'):
        CreatData (pegawai)
    elif (Menu == '3') :
        updateData (pegawai)
    elif (Menu == '4') :
        deleteData (pegawai)        
    elif (Menu == '5') :
        filterData (pegawai)   
    elif (Menu == '6') :
        print ('\n***Terimakasih Sudah Membuka Program Ini***')
        break 
    else :
        print ('\nPilihan tidak valid. Silahkan pilih 1, 2, 3, 4, 5, atau 6')
