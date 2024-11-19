Data_Pasien = [
    {
        'Nama Depan': 'JON',
        'Nama Belakang': 'DOE',
        'Umur': 54, 
        'Jenis Kelamin': 'Pria',
        'Keterangan': 'Inap',
        'Email': 'JODO@kingstone.com'
        
    },
    {
        'Nama Depan': 'JANE',
        'Nama Belakang': 'DOE',
        'Umur': 32, 
        'Jenis Kelamin': 'Wanita',
        'Keterangan': 'Clear',
        'Email': 'JEDO@kingstone.com'
    }
]

def Tampil_Daftar_Pasien() :
    print('''
                                ||||||||||||||||||||||||||||||||||||||||| 
                                || DAFTAR PASIEN RUMAH SAKIT KING STONE||
                                ||||||||||||||||||||||||||||||||||||||||| 
          ''')
    print('------------------------------------ 2023 - 2024 Data -------------------------------------------------')
    print("Index\t|Nama Depan\t|Nama Belakang\t|Umur\t|Jenis Kelamin\t|Keterangan\t|Email\t\n------------------------------------------------------------------------------------------------------")
    for i in range(len(Data_Pasien)) :
        print('{}\t|{}\t\t|{}\t\t|{}\t|{}\t\t| {}\t\t|{}'.format(i,Data_Pasien[i]['Nama Depan'],
        Data_Pasien[i]['Nama Belakang'],Data_Pasien[i]['Umur'],Data_Pasien[i]['Jenis Kelamin'],Data_Pasien[i]['Keterangan'],Data_Pasien[i]['Email']))
    print('------------------------------------------------------------------------------------------------------')
def Enter_Data_Pasien() :
    print('\n>>>>>>>> Mohon diisi 6 PROMT yang akan muncul setelah ini sesuai dengan prosedur dan value yang di minta program <<<<<<<<<\n \t\t Note: BAGI INPUTAN BERUPA NOMINAL MOHON ISI DENGAN VALUE NOMINAL JUGA!!\n')

    while True: 
        Nama_Depan = input('Nama Depan Pasien : ').upper()
        if(Nama_Depan == " " or Nama_Depan.isalpha() == False) : 
            print('\n\n\t         !!!!!!Perhatian!!!!!!             \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')
        else : 
            break

    while True: 
        Nama_Belakang = input('\nKOSONGKAN APABILA TIDAK ADA\nNama Belakang Pasien : ').upper()
        if(Nama_Belakang == " "): 
            Nama_Belakang = 'N/A'
            break
        elif Nama_Belakang.isalpha() == False : 
            print('\n\t         !!!!!!Perhatian!!!!!!             \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')
        else : 
            break
    
    while True: 
        Umur_Pasien = int(input('Umur Pasien : '))
        if(Umur_Pasien < 0 or Umur_Pasien >= 110) : 
            print('\t         !!!!!!Perhatian!!!!!!             \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')
        else : 
            break

    while True:
        Jenis_Kelamin_Pasien = int(input('''
        -- Input angka 0 = Pria
        -- Input angka 1 = Wanita
        
        Jenis Kelamin Pasien : '''))
        if Jenis_Kelamin_Pasien == 0 : 
            Jenis_Kelamin_Pasien = 'Pria'
            break
        elif Jenis_Kelamin_Pasien == 1 : 
            Jenis_Kelamin_Pasien = 'Wanita'
            break
        else : 
            print('\t         !!!!!!Perhatian!!!!!!             \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')

    while True: 
        Status_Pasien = int(input('''
        \n\tPanduan EWS: 0 - 4 = 'Clear' | 5 - 7 = 'Inap'

        Masukkan 'Early Warning Score' pasien : '''))
        ews = (0,1,2,3,4,5,6,7)
        if Status_Pasien in ews: 
            break
        else : 
            print('\t         !!!!!!Perhatian!!!!!!             \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')

    while True:
        if Status_Pasien < 5 :
            Status_Pasien = 'Clear'
            break
        elif Status_Pasien >= 5 : 
            Status_Pasien = 'Inap'
            break
        else :
            print('\t         !!!!!!Perhatian!!!!!!             \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')
            break
    
    while True: 
        Email_Pasien = input('E-mail pasien : ')
        if Email_Pasien == " " : 
            print('\n\n\t!!PERHATIAN!!\n\t!!Tolong diisi!!\n')
        else : 
            break
    List_Pasien = {"Nama Depan" : Nama_Depan, "Nama Belakang" : Nama_Belakang, "Umur" : Umur_Pasien, "Jenis Kelamin" : Jenis_Kelamin_Pasien, "Keterangan" : Status_Pasien, "Email" : Email_Pasien}
    Data_Pasien.append(List_Pasien)
    
    Tampil_Daftar_Pasien()
    print('\n===================== TERIMA KASIH ! DATA TELAH BERHASIL DI INPUT KE DATABASE RSKS =====================\n')

def Update_Data_Pasien() : 
    Tampil_Daftar_Pasien()
    print('''\n===================== Berikut database pasien RSKS yang ter-Update =====================\n\nBerdasarkan Database Pasien yang terbaru di atas, silahkan masukkan Nomer Index yang bersangkut yang ingin anda UPDATE\n''')

    while True:
        while True: 
            Update_Data = input('\n\nNomer Index: ')
            if Update_Data.isnumeric() == True: 
                No_Index_Updatedata = int(Update_Data)
                if No_Index_Updatedata >= len(Data_Pasien): 
                    print('\n\n>>>>>MOHON MAAF input index TIDAK VALID<<<<<\n\tSilahkan INPUT kembali')
                else : 
                    break
            else : 
                print('\n\n>>>>>MOHON MAAF input index TIDAK VALID<<<<<\nSilahkan INPUT kembali') 
                
        print('\n\nInput Berhasil, berikut data yang terunduh\n\n-------------------------------------------------------------------------------------------')
        print("Index\t|Nama Depan\t|Nama Belakang\t|Umur\t|Jenis Kelamin\t|Keterangan\t|Email\t\n-------------------------------------------------------------------------------------------")
        for i in range(len(Data_Pasien)) :
            if i == No_Index_Updatedata: 
                print('{}\t|{}\t\t|{}\t\t|{}\t|{}\t\t| {}\t\t|{}'.format(i,Data_Pasien[i]['Nama Depan'],
                Data_Pasien[i]['Nama Belakang'],Data_Pasien[i]['Umur'],Data_Pasien[i]['Jenis Kelamin'],Data_Pasien[i]['Keterangan'],Data_Pasien[i]['Email']))
        else : 
            i+=1 

        print('''\n\n>>>>>> Key Elemen yang dapat di pilih untuk menjalani UPDATE DATA: <<<<<<
            
        ''')
        while True : 
            Update = input('''1 = Nama Depan | 2 = Nama Belakang | 3 = Umur | 4 = Jenis Kelamin
                    5 = Keterangan | 6 = Email   
                           
    Masukkan angka yang merepresantikan key elemen yang ingin di ubah : ''')
            if Update == '1': 
                Update_Elemen = input('\t Update Nama Depan: ')
                if(Update_Elemen == " " or Update_Elemen.isalpha() == False) : 
                    print('\n\n\t\t!!!!!!Perhatian!!!!!! \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')
                else : 
                    Data_Pasien[No_Index_Updatedata]['Nama Depan'] = Update_Elemen.upper()
                    break
            elif Update == '2' : 
                Update_Elemen = input('\t Update Nama Belakang: ')
                if(Update_Elemen == " "): 
                    Update_Elemen = 'N/A'
                    Data_Pasien[No_Index_Updatedata]['Nama Belakang'] = Update_Elemen.upper()
                    break
                elif Update_Elemen.isalpha() == False : 
                    print('\n\n\t\t!!!!!!Perhatian!!!!!! \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')
                else : 
                    Data_Pasien[No_Index_Updatedata]['Nama Belakang'] = Update_Elemen.upper()
                    break
            elif Update == '3' : 
                Update_Elemen = int(input('\t Update Umur: '))
                if(Update_Elemen < 0 or Update_Elemen >= 110) : 
                    print('\n\n\t\t!!!!!!Perhatian!!!!!! \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')
                else : 
                    Data_Pasien[No_Index_Updatedata]['Umur'] = Update_Elemen
                    break
            elif Update == '4' : 
                Update_Elemen = int(input('''
                -- Input angka 0 = Pria
                -- Input angka 1 = Wanita
        
                    Update Jenis Kelamin : '''))
                if Update_Elemen == 0: 
                    Data_Pasien[No_Index_Updatedata]['Jenis Kelamin'] = 'Pria'
                    break
                elif Update_Elemen == 1: 
                    Data_Pasien[No_Index_Updatedata]['Jenis Kelamin'] = 'Wanita'
                    break
                else : 
                    print('\n\n\t\t!!!!!!Perhatian!!!!!! \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')
            elif Update == '5' : 
                Update_Elemen = int(input('''
                Panduan EWS: 0 - 4 = 'Clear' | 5 - 7 = 'Inap'

                Update Keterangan dengan 'Early Warning Score': '''))
                if Update_Elemen >= 0 and Update_Elemen < 5 : 
                    Data_Pasien[No_Index_Updatedata]['Keterangan'] = 'Clear'
                    break
                elif Update_Elemen >= 5 and Update_Elemen < 8 : 
                    Data_Pasien[No_Index_Updatedata]['Keterangan'] = 'Inap'
                    break
                else : 
                    print('\n\n\t\t!!!!!!Perhatian!!!!!! \n  ERROR : Di karenakan INPUT tidak sesuai dengan program\n \t        MOHON DI INPUT KEMBALI\n')
            elif Update == '6' : 
                Update_Elemen = input('Update Email: ')
                if Update_Elemen == " " : 
                    print('\n\n\t\t\t\t!!Perhatian!! \n\t\tTolong diisi Email atau contact yang bisa di hubungi\n\n')
                else : 
                    Data_Pasien[No_Index_Updatedata]['Email'] = Update_Elemen
                    break
            else : 
                print('\t\t\n\n         \t!!!!!!Perhatian!!!!!!             \n  \tERROR : Pilih HANYA dari Value 1 - 6\n')
        Tampil_Daftar_Pasien()
        print('\n===================== TERIMA KASIH ! DATA TELAH BERHASIL TER-UPDATE KE DATABASE RSKS =====================\n')
        break

def Remove_Data_Pasien() : 
    Tampil_Daftar_Pasien()
    print('''\n===================== Berikut database pasien RSKS yang ter-Update =====================\n\n\nBerdasarkan Database Pasien yang terbaru ini, mohon pilih data yang ingin di unduh dengan menggunakan nomer index\n''')

    while True : 
        while True : 
            Remove_Data = input('\n\nNomer Index: ')
            if Remove_Data.isnumeric() == True: 
                Remove_Index_Int = int(Remove_Data)
                if Remove_Index_Int >= len(Data_Pasien): 
                    print('\n\n>>>>>MOHON MAAF input index TIDAK VALID<<<<<\nSilahkan INPUT kembali')
                else : 
                    break
            else : 
                print('\n\n>>>>>MOHON MAAF input index TIDAK VALID<<<<<\nSilahkan INPUT kembali')

        print('\n\nInput Berhasil, berikut data yang terunduh\n\n-------------------------------------------------------------------------------------------')
        print("Index\t|Nama Depan\t|Nama Belakang\t|Umur\t|Jenis Kelamin\t|Keterangan\t|Email\t\n-------------------------------------------------------------------------------------------")
        for i in range(len(Data_Pasien)) :
            if i == Remove_Index_Int: 
                print('{}\t|{}\t\t|{}\t\t|{}\t|{}\t\t| {}\t\t|{}'.format(i,Data_Pasien[i]['Nama Depan'],
                Data_Pasien[i]['Nama Belakang'],Data_Pasien[i]['Umur'],Data_Pasien[i]['Jenis Kelamin'],Data_Pasien[i]['Keterangan'],Data_Pasien[i]['Email']))
        else : 
            i+=1 

        while True: 
            Yakin_Hapus = input('\n\nPERINGATAN ! Apakah and yakin untuk menghapus data di atas tersebut? (Y/N)').upper()
            if Yakin_Hapus == 'Y' : 
                del Data_Pasien[Remove_Index_Int]
                Tampil_Daftar_Pasien()
                print("\n\n\t>>>>>> Tindakan 'Remove' telah berhasil di eksekusi <<<<<<")
                break
            elif Yakin_Hapus == 'N' : 
                Tampil_Daftar_Pasien()
                print("\n\n\t>>>>>> Tindakan 'Remove' tidak berhasil di eksekusi <<<<<<")
                break
            else : 
                Yakin_Hapus != 'Y' or Yakin_Hapus != 'N'
                print('\n\n\t>>>>>> Mohon diisi sesuai spesifikasi (Y/N) <<<<<<\n')
        break

# Karena while true ini akan ttp looping walawpun tidak ada inputan di menu database
while True: 
    Menu_Database = input('''
        
                        
        SELAMAT DATANG DI DATABASE RSKS
                          
        MENU YANG TERSEDIA:
        1. DATABASE Pasien RSKS
        2. ENTER Data Pasien Baru
        3. UPDATE Data Pasien
        4. REMOVE Data Pasien
        5. EXIT Program
        
        Sesuai keperluan, silahkan input angka 1 - 5 : ''' )
    if(Menu_Database == '1') :
        Tampil_Daftar_Pasien()
    elif(Menu_Database == '2') :
        Enter_Data_Pasien()
    elif(Menu_Database == '3') : 
        Update_Data_Pasien()
    elif(Menu_Database == '4') : 
        Remove_Data_Pasien()
    elif(Menu_Database == '5') : 
        print('''
TERIMA KASIH kepada staff RSKS yang telah mengakses program early access kami. 
Jika ada kesulitan untuk mengakses atau menggunakan program in mohon hubungi Team IT kami.
Dan kami harap dapan mengikuti survey feedback yang akan kami selenggarakan bulan depan.
Untuk info lebih lanjut mengenai survey tersebut, tim kami akan hubungi seluruh staff RSKS via E-mail. 

Best Regard,
              

              
Garm Raid
Team Leader IT & Data Science

Team IT and Data Science contact: 078452775311                
''')
        break
