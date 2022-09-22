# Tugas 2
Pada tugas ini, kita mengimplementasikan *Data Delivery* pada django.
Berikut link aplikasi website, [HerokuApp Pages](https://tugas2-pbp-safa.herokuapp.com/).

## Perbedaan antara JSON, XML, dan HTML
JSON merupakan suatu format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari *web server* sehingga dapat dibaca oleh para *user*. 
Ekstensi file JSON adalah .json.

XML sebuah bahasa *markup* yang didesain untuk menyimpan dan mengantarkan data. Ekstensi file XML adalah .xml.

HTML bahasa *markup* standar untuk membuat dan menyusun halaman dan aplikasi web. Ekstensi file HTML adalah .html.

<img width="734" alt="Screen Shot 2022-09-22 at 10 21 59" src="https://user-images.githubusercontent.com/96807409/191651520-57660f05-4328-4c17-9f4c-be6b4d524cf4.png">


## Mengapa *data delivery* diperlukan dalam pengimplementasian sebuah platform?
Dalam membangun suatu platform, pasti dibutuhkan transaksi data, antara data milik *user* dengan *database* platform maupun pertukaran data pada sesama *user*. 
*Data delivery* diperlukan untuk memudahkan dan mempercepat proses pertukaran data sehingga *developer* tidak perlu melakukan pertukaran data secara manual.


## Proses Implementasi Data Delivery
1. Untuk membuat *app* baru, Menjalankan perintah `python manage.py startapp mywatchlist` pada projek Django.
2. Membuat folder baru bernama `mywatchlist` ke dalam `urls.py`.
3. Melakukan routing untuk mengakses `mywatchlist` dalam format HTML, XML, dan JSON pada `urls.py` di dalam aplikasi mywatchlist.
4. Menambahkan model pada `models.py` bernama `WatchlistItem` dengan attribut `watched`, `title`, `rating`, `release_date`, dan `review`.
5. Membuat `initial data` pada folder `fixtures` bernama `initial_mywatchlist_data.json` berisi data-data yang akan ditampilkan. 
6. Menambahkan method untuk menampilkan data dengan format HTML, XML, dan JSON pada file `views.py`.
7. Melakukan migrasi data dengan perintah `python manage.py makemigrations` dan `python manage.py migrate`. 
8. Melakukan *load initial data* dengan `python manage.py loaddata initial_mywatchlist_data.json`.
