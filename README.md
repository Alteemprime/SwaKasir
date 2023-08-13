# SwaKasir
Program yang digunakan pelanggan Supermarket untuk memasukkan barang belanjaan mereka sendiri
## Requirements / Objective
<img width="475" alt="expected output" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/dce04cda-2860-4d77-be71-a9c16116c68c"> 

- Screenshot di atas adalah output yang diharapkan dari kelas transaksi
  
- Program menyediakan operasi CRUD (Create, Read, Update, Delete) di data yang dimasukkan
  
- User dapat mereset data yang telah dimasukkan
  
- User yang setuju dengan data yang ia masukkan mendapat diskon berdasar total harga barang. 10% untuk total harga di atas 500k, 8% untuk total harga di atas 300k dan 5% untuk total harga di atas 200k

## Flowchart
<img width="329" alt="Swakasir Flowchart" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/e6a2757e-cd8f-4ba3-8369-514eff36685a">

- Pada awal program, variabel kelas Transaksi dibuat serta flag variable add_data dan display+edit. flag add_data bernama add_data_reset. digunakan untuk kontrol loop ketika user reset data atau user menghapus semua data. flag display_edit bernama still_editing digunakan untuk kontrol loop ketika user sudah selesai mengedit datanya dan ingin melihat visual data yang ditampilkan.

- Di versi ini, user diharapkan mengedit secara urut dari dari atas ke bawah, memilih nomor rekaman yang di edit. memilih proses pengeditan. baru kemudian mendapat update visual data yang telah dimasukkan. Ini terjadi dalam box edit data. flag still_editing mengontrol loop dimana user masih meminta update visual.

- Flag edit_mode digunakan untuk kontrol looping user memasukkan tiap pembelian (data tiap barang, jumlah dan harga satuan)

- Jika user memasukkan 'ok' ketika proses edit, total harga dihitung beserta kondisi diskonnya

## Transaction Class
<img width="184" alt="Transaction" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/481a34b3-863e-4c34-98b1-602f2153518d">

Kelas transaksi merupakan dictionary. list digunakan untuk mengakses data dictionary berdasar urutan dimasukkan oleh user.

<img width="230" alt="Transaction_AddData" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/457b3f1b-1cfa-4797-a9dd-5768c1763e27">

Untuk tiap data yang dimasukkan, format data dictionary diformat sesuai required output di atas.

<img width="284" alt="Transaction_Update" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/d53c122b-0c67-47c2-9fcf-24eb60823d06">

Karena nama barang merupakan key dictionary yang immutable, penggantian nama membuat data dict nama barang baru dan menghapus data nama barang lama. Transaction list bisa langsung diupdate. Untuk jumlah dan harga satuan barang, bisa langsung re-assign dengan nilai baru

<img width="173" alt="Transaction_Delete" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/46994819-996c-4d81-b61c-a4b0660a5517">

Hapus data berdasar key dictionary yang dimasukkan (nama barang). begitu juga di transaction list

<img width="165" alt="Transaction_Reset" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/cea2c1d6-1d4b-488c-8b3f-c3fd1c24bad4">

Reset berarti mengosongkan Transaction dictionary dan list

<img width="460" alt="Transaction__str__" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/02dd4c19-4459-4cb9-8e59-469499d1e3dc">

__str__ untuk merepresentasikan secara string, dictionary dari kelas transaksi. Digunakan agar representasi string kelas sesuai dengan required output. ini dipakai ketika debug program selama development.

<img width="509" alt="Transaction_TotalPrice" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/2ea7fdc8-cc2f-484b-87cd-c8e0ab774c79">

Total menampung jumlah total harga. total_pay menampung jumlah total harga dengan memperhitungkan kondisi diskon. output yang diterima user dicabangkan antara yang mendapat diskon dan yang tidak berdasar threshold harga 200k.

## Program SwaKasir
- Splash_Screen menyambut user, memberi info cara penggunaan program, dan info diskon sehingga user yang memperkirakan harganya belum mencapai threshold harga diskon dapat mengambil barang lagi sebelum input data

<img width="443" alt="SwaKasir_DisplayTransactionSummary" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/e0b9d3c0-bc5e-4f1d-900c-bd3771794a40">

- Display_Transaction_Summary memberi visual data yang dimasukkan user dalam bentuk tabel dengan format rata tengah dan rata kanan

<img width="391" alt="SwaKasir_AddNewTransaction" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/1e1849be-78ec-46ac-b01a-079563d66884">

- Customer_input flag untuk mengontrol user masih mau menambah data baru atau tidak.

<img width="329" alt="SwaKasir_Edit_CheckOut1" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/6ca95a7e-43c2-4b34-8501-9e7909761bc3">

- Variabel checkout digunakan untuk menampung string pilihan reset --> reset transaksi, ok --> perhitungan total harga yang harus dibayar user

<img width="539" alt="SwaKasir_Edit_CheckOut2" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/dd6937ec-a504-4104-ba52-1bb4f0b59247">

- Blok try except digunakan karena dibutuhkan integer nomor barang yang akan digunakan untuk mengakses data transaksi melalui indeks list kelas Transaksi. sementara checkout dapat menampung string. Diberikan fitur skip sehingga user bisa lebih cepat mengedit datanya (tidak perlu memasukkan lagi data lama)

<img width="547" alt="SwaKasir_EditMode" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/d1db461a-3729-4bb0-9e02-e1b736f68cf8">

- Variabel em digunakan untuk set flag edit_mode yang mengontrol apakah user akan mengedit nomor data belanja yang lain.

## Test Case
1. User memasukkan 1 pembelian, memilih reset, memasukkan 1 pembelian, menghapus pembelian tersebut
<img width="788" alt="Output_TestCase1_1" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/bda56a30-2fda-461f-b455-378b8054b183">
<img width="428" alt="Output_TestCase1_2" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/d699a261-f33e-4154-b30f-f5a46eb6663a">
<img width="789" alt="Output_TestCase1_3" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/e98cb080-8d63-4a01-87a7-ef1633ea04d8">

2. User memasukkan 1 pembelian, memilih ok untuk membayar
<img width="806" alt="Output_TestCase2_1" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/57be2650-5e31-468a-8931-14b9d59a74ca">

3. User memasukkan 3 pembelian, menghapus pembelian ke 2, mengedit pembelian ke 3 di nama barang dan harga satuan, dengan total harga antara 300k - 500k
<img width="551" alt="Output_TestCase3_1" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/659b903b-e552-4d9f-a445-3a093bbdfbad">
<img width="797" alt="Output_TestCase3_2" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/16719bc7-1558-4f6b-a520-865b47a51980">
<img width="810" alt="Output_TestCase3_3" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/1c9154ed-4735-4a6e-9146-4e3afa99c1c6">
Pada versi ini masih ada sisa code debug yang perlu dibersihkan di eksekusi print data dictionary transaksi ketika proses edit
<img width="797" alt="Output_TestCase3_4" src="https://github.com/Alteemprime/SwaKasir/assets/137682124/350b57f4-4ff8-4ec3-99f1-07e811ccda10">
