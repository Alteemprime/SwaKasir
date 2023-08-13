import cashier_module as cm

def splash_screen():
    '''
    Fungsi splash screen tanpa argumen bertujuan memperkenalkan program bahkan pada new user
    sehingga pengguna mudah memahami tujuan program dan cara pengoperasian program secara umum

    arguments : None

    returns None
    '''
    print('Selamat datang di program SwaKasir')
    print('')
    print('Program ini akan meminta anda memasukkan barang-barang yang anda beli dari swalayan kami')
    print('Permintaan data yang anda masukkan meliputi nama barang, jumlah barang, dan harga satuan per barang dari belanjaan anda')
    print('itu semua perlu dilakukan untuk menghitung rupiah yang perlu anda bayar')
    print('Jangan khawatir bila anda memasukkan data, ketika anda selesai memasukkan semua belanjaan,')
    print('anda bisa review ulang data yang anda masukkan, baik nama barang, jumlah barang, maupun harga satuan')
    print('')
    print('anda mendapatkan diskon 5% untuk total belanja lebih dari Rp. 200.000')
    print('diskon 8% untuk total belanja lebih dari Rp. 300.000')
    print('dan diskon 10% untuk total belanja lebih dari Rp. 500.000')
    print('pastikan barang di kantong belanja anda mencapai total belanja untuk mendapatkan diskon!')
    print('')
    print('Pencet tombol sembarang untuk memulai program')

def display_transaction_summary():
    '''
    Fungsi display_transaction_summary memberi gambaran visual data belanja untuk diperiksa oleh user
    kesesuaiannya dengan fakta

    arguments : None

    returns None
    '''
    global new_transaction
    num = 1
    print('')
    print('Anda masuk ke mode edit, di bawah ditampilkan rangkuman belanja anda')
    print('1. Masukkan nomor rekaman barang yang ingin anda edit')
    print('2. Jika anda ingin menghapus nomer rekaman yang anda pilih, masukkan nama "delete" sebagai nama barang')
    print('3. Jika tidak ingin menghapus, masukkan nama barang yang baru atau masukkan "s" untuk skip (memakai nilai lama)')
    print('4. Masukkan nilai jumlah yang baru atau masukkan "0"(nol) untuk skip (memakai nilai lama)')
    print('5. Masukkan nilai harga satuan yang baru atau masukkan "0"(nol) untuk skip (memakai nilai lama)')
    print('6. Masukkan "y" untuk mengedit nomor rekaman yang lain, "n" untuk melihat data terbaru belanja anda,')
    print('')
    print(f'DAFTAR BELANJA PELANGGAN ATAS NAMA {new_transaction.customer.upper()}')
    print('')
    print('| No |     Nama Item     | Jumlah Item | Harga Satuan |     Total Harga     |')
    for key in new_transaction.keys :
        print(f'|{num:^4}|{key:^19}|{new_transaction.dict[key][0]:^13}|{new_transaction.dict[key][1]:^14}|{new_transaction.dict[key][0]*new_transaction.dict[key][1]:>21}|')
        num += 1
    print('')    

def edit_transaction():
    '''
    Fungsi edit_transaction membantu user mengedit data transaksi secara abstrak, sehingga fungsi ini
    ditampilkan bersama display_transaction_summary sebagai panduan data lama yang disimpan di komputer

    arguments : None

    returns None
    '''
    global add_data_reset
    global new_transaction
    global still_editing
    still_editing = True
    edit_mode = True
    while edit_mode :
        checkout = input('Masukkan kata "reset" untuk menghapus semua transaksi \n' +
                   'Masukkan "ok" jika anda setuju dengan daftar belanja di atas \n' +
                   'atau masukkan nomor barang yang ingin anda edit : ')
        if  checkout.lower() == 'reset':            
            new_transaction.reset_transaction()
            still_editing = False
            edit_mode = False
            add_data_reset = True
            break
        elif checkout.lower() == 'ok':
            still_editing = False
            edit_mode = False
            add_data_reset = False
            break
        else :
            try :
                num_pressed = int(checkout)
                key_selected = new_transaction.keys[num_pressed-1]
                new_barang = str(input(f'Masukkan nama barang baru untuk input barang nomor {num_pressed} (s untuk skip)(delete untuk menghapus):'))
                if new_barang.lower() == 'delete':
                    if str(input(f'Hapus seluruh data untuk pembelian barang {key_selected} (y/n) : ')).lower() == 'y' :
                        new_transaction.delete_data(key_selected)                                                
                        display_transaction_summary()                        
                    else :
                        pass
                elif new_barang.lower() == 's' :
                    new_transaction.dict[key_selected] = new_transaction.dict[key_selected]
                else :
                    new_transaction.update_item_name(key_selected, new_barang)
                    key_selected = new_barang                    
                    new_jumlah = int(input(f'Masukkan jumlah barang baru untuk input barang {key_selected} (0 untuk skip):'))
                    if new_jumlah == 0 :
                        new_transaction.dict[key_selected][0] = new_transaction.dict[key_selected][0]
                    else :
                        new_transaction.update_item_qty(key_selected,new_jumlah)
                    print(new_transaction.dict)
                    new_hargasatuan = int(input(f'Masukkan harga baru untuk input barang {key_selected} (0 untuk skip):'))
                    if new_hargasatuan == 0 :
                        new_transaction.dict[key_selected][1] = new_transaction.dict[key_selected][1]
                    else :
                        new_transaction.update_item_price(key_selected,new_hargasatuan)
                    print(new_transaction.dict)
            except ValueError :
                pass
        em = str(input('Edit nomor rekaman belanja yang lain (y/n): '))
        if new_transaction.dict == {}:
            reset_add_data = input('Anda sudah menghapus semua daftar belanja anda, pencet tombol [Enter] untuk mengulang ke menu penambahan data')
            edit_mode = False
            still_editing = False
            add_data_reset = True
        elif em.lower() == 'y' :
            edit_mode = True
        elif em.lower() == 'n' :
            edit_mode = False
            still_editing = True
    
def add_new_transaction():
    '''
    fungsi add_new_transaction berfungsi untuk inisiasi data transaksi baru untuk user. Seluruh
    item unik belanja diharapkan sudah dimasukkan user disini
    '''
    global add_data_reset
    global new_transaction
    global still_editing
    print('')
    new_transaction.customer = str(input('Dengan customer bernama siapa saya berinteraksi ? '))
    still_editing = True
    print(f'Salam {new_transaction.customer}, anda bisa mulai memasukkan daftar belanjaan anda')
    customer_input = True
    num = 0
    print('')
    while customer_input:
        barang_name = str(input(f'Masukkan barang ke- {num+1} yang anda beli : '))
        num += 1
        barang_qty = int(input(f'Ada berapa {barang_name} yang dibeli : '))
        barang_price = int(input(f'Berapa harga satuan barang {barang_name} : '))
        new_transaction.add_data(barang_name,barang_qty,barang_price)
        more_input = str(input('Masih ada barang lagi yang hendak dimasukkan (y/n):'))
        if more_input.lower() == 'y':
            customer_input = True
            print('')
        elif more_input.lower() == 'n':
            customer_input = False
            add_data_reset = False
    
splash_screen()
new_transaction = cm.Transaction()
add_data_reset = True
still_editing = True

print('')
while add_data_reset :
    add_new_transaction()
    while still_editing :
        display_transaction_summary()
        edit_transaction()
display_transaction_summary()
pay = new_transaction.total_price()
print(pay)

