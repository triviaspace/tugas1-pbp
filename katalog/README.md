# Tugas 2
Pada tugas ini, kita mengimplementasikan konsep Model-View-Template (MVT) pada django. <br />
Berikut link aplikasi website, [HerokuApp Pages](https://tugas2-pbp-safa.herokuapp.com/).

## Penjelasan Alur dari Bagan
![URLConf](https://user-images.githubusercontent.com/96807409/190288213-36f2b57b-14c6-45bc-93a0-d3c076f25fb6.png)

Alur sebuah permintaan diproses di Django :
1. *Request* dari *User* yang masuk ke server Django akan diproses melalui `urls.py` menuju ke `views.py`. 
2. Dalam `urls.py`, Django yang bekerja sebagai *controller* akan mengecek keberadaan *resources*.
3. Apabila terdapat proses yang membutuhkan keterlibatan *database*, maka `views.py` akan memanggil *query* ke `models.py`, lalu *database* 
akan mengembalikan hasil dari *query* tersebut ke `views.py`. 
4. Setelah *request* telah selesai diproses, hasil prosesnya akan dipetakan ke dalam berkas HTML yang sudah didefinisikan 
sebelumnya. 
5. Berkas HTML berbentuk template tersebut dikembalikan ke pengguna sebagai respons.

## Virtual Environment
### Kenapa Virtual Environment dibutuhkan?
*Virtual environment* adalah *tool* yang dapat menjaga *dependences* yang diperlukan oleh berbagai proyek terpisah dengan 
membuat *isolated python virtual environments*. *Python Developer* biasanya membutuhkan *virtual environment* agar 
mereka tidak perlu memedulikan perbedaan versi django, *library*, maupun *framework* yang berbeda-beda disebabkan oleh :
- Versi dependensi masing-masing *developer* berbeda
- Masing-masing proyek punya versi yang beda
- Adanya *update version*

Bayangkan jika seorang *developer* bekerja pada dua proyek python berbasis web, yang satu proyek personal dengan django versi 2.1 
serta proyek *open source* menggunakan django versi 1.9. Akan sangat susah bagi developer untuk ikut berkontribusi dalam proyek *open source* 
karena akan terjadi banyak *error* akibat perbedaan versi django. Apabila developer ingin melakukan *downgrade* versi django, 
maka *developer* tidak bisa mengerjakan proyek personalnya kembali. *Virtual environment* dapat menangani masalah ini dengan 
memungkinkan developer membuat *virtual environment* terpisah (tidak terikat satu sama lain) yang dapat diaktifkan dan dinonaktifkan dengan mudah 
setelah selesai digunakan.

### Apakah Aplikasi Web Berbasis Django Dapat Tetap Dibuat Tanpa Menggunakan Virtual Environment?
Kita tetap dapat membuat web berbasis django tanpa *virtual environment*, namun ketika terjadi perbedaan versi, 
seperti yang telah dijelaskan sebelumnya, akan timbul banyak *error*. Maka dari itu, peran *virtual environment* cukup penting.

## Proses Implementasi Konsep MVT
1. Membuat fungsi pada `katalog/views.py` yang dapat mengambil data dari `CatalogItem` pada `katalog/models.py`.
Membuat fungsi `katalog_view(request)` dengan parameter mengambil *request* dari user. Dalam fungsi, juga memuat variabel `context` berisi 
`list_katalog`, `name`, serta `id`. Fungsi akan memanggil *query* ke dalam *database* dan menyimpan hasil dalam variabel `CatalogItem` 
kemudian `katalog.html` akan di-*render* agar dapat muncul dalam HTML.

2. Membuat sebuah *routing* untuk memetakan fungsi yang telah dibuat pada `views.py`.
*Routing* dilakukan dengan menambahkan `path('katalog/', include('katalog.urls'))` pada `urls.py`. 
*Routing* dilakukan pada `urls.py` di `katalog`. Kemudian, `urls.py` akan menjalankan fungsi view `katalog_view(request)` yang berada di `views.py`.

3. Memetakan data `{{nama}}` dan `{{id}}` untuk menampilkan data nama dan npm yang didapatkan dari proses *render* fungsi pada `views.py` 
ke dalam `katalog.html`. Terdapat juga loop `catalog_item` untuk menampilkan isi dari `catalog_item` dalam bentuk tabel.

4. Terakhir, melakukan tahap *deployment* dengan menghubungkan *repository* github dengan heroku. Pada tahap ini,
menambahkan variable `APP_NAME` dan `API_KEY` dari aplikasi yang dibuat di Heroku ke dalam Github *repository secrets*.
