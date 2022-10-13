# Tugas 6
Pada tugas ini, kita mengimplementasikan Ajax pada Django <br/>
Berikut link aplikasi website, [HerokuApp Pages](https://tugas2-pbp-safa.herokuapp.com/).

## Perbedaan antara *Asynchronous Programming* dengan *Synchronous Programming*
Untuk proses *synchronous*, setiap fungsi dijalankan berurutan. Untuk dapat menjalankan fungsi berikutnya, harus menunggu fungsi sebelumnya selesai (*blocking*). 
Berbeda dengan proses *asynchronous*, kita tidak perlu menunggu suatu fungsi selesai dijalankan untuk menjalankan fungsi lainnya (*non-blocking*). 
Artinya, beberapa fungsi dapat dijalankan bersamaan dalam satu waktu.
 
Untuk eksekusi suatu program, proses *asynchronous* relatif lebih cepat dibandingkan dengan proses *synchronous*. 
Meskipun proses *asynchronous* terlihat lebih unggul, tetapi ada beberapa hal yang mempengaruhi kecepatan proses *asynchronous*. 
Berikut ini adalah faktor-faktor yang dapat mempengaruhi :
1. Keterkaitan antar fungsi </br>
Apabila hasil dari suatu fungsi akan digunakan pada fungsi berikutnya, maka prosesnya harus berjalan secara berurutan. Oleh karena itu, jika suatu fungsi saling berkaitan dengan fungsi lainnya, maka penggunaan proses asynchronous menjadi kurang tepat.

2. Lama waktu eksekusi </br>
Lama waktu yang dibutuhkan untuk menjalankan setiap fungsi harus diperhatikan sebelum menentukan tipe proses mana yang lebih baik dipilih. Jika rata-rata waktu yang dibutuhkan untuk setiap fungsi relatif cepat dan tidak membutuhkan proses yang kompleks, penggunaan proses asynchronous tidak akan berdampak besar pada jalannya sebuah program.
 
3. Kompleksitas </br>
Penerapan proses asynchronous pada suatu program cukuplah rumit. Apabila program yang akan dibuat masih tergolong sederhana dan tidak membutuhkan banyak proses, penggunaan asynchronous justru akan membuat program yang sederhana terlihat begitu kompleks

## Paradigma *Event-Driven Programming*
Event-driven programming adalah paradigma *computer programming* di mana *control flow* dari program ditentukan saat terjadinya *event*. 
*Events* ini dimonitor oleh *code* yang disebut *event listener*. Apabila terdeteksi ada event yang terjadi, maka akan dijalankan *event handler*
(*callback function* atau *method* yang di-*trigger* ketika suatu *event* terjadi).
Pada teori, semua bahasa pemrograman mendukung *event-driven style of programming*, meski ada beberapa bahasa yang memiliki fitur khusus untuk mempermudah implementasi paradigma ini. 

</br>

Pada *task* 6 ini, paradigma ini telah diimplementasikan. Contohnya, pada 
```
$(document).ready(function(){
    $("#getData").click(function(){
      
      createTableAjax();

    });
  });
 ```
 Di sini, function akan dijalankan apabila telah *button* telah di-*click*. *Handler* akan menjalankan fungsi tersebut.
 
 ## Penerapan *Asynchronous Programming* pada AJAX.
AJAX (*Asynchronous JavaScript And XML*) adalah penggunaan *object* `XMLHttpRequest` untuk berkomunikasi dengan server. 
AJAX dapat mengirim dan menerima informasi dalam berbagai format, termasuk *file* JSON, XML, HTML, dan teks. 
AJAX memiliki karakteristik "*asynchronous*". Artinya, AJAX dapat berkomunikasi dengan server, bertukar data, dan 
memperbarui halaman tanpa harus melakukan refresh halaman.

## Proses Implementasi
1. Membuat *file* html baru pada *folder* `templates` bernama `todolist_ajax.html`. Lalu, membuat konten dari *file* HTML.
2. Pada `views.py`, Membuat *function* `todolist_ajax` untuk mengembalikan data JSON. Setelah itu, membuat *function* `show_todolist_ajax` untuk melakukan
*render* pada halaman `todolist_ajax.html` yang telah berisi data-data JSON.
3. Menambahkan *path* pada `urls.py` berupa `path('json/', todolist_ajax, name='todolist_ajax')`,
    `path('show/json/', show_todolist_ajax, name='show_todolist_ajax')`,
    `path('add/', add_task_ajax, name='add_task_ajax')`.
4. Membuat function `createTableAjax()` pada `todolist_ajax.html` untuk menampilkan data-data *tasks* berupa tabel. Menambahkan modal button untuk
membuat *form* di dalamnya. Lalu, Membuat *event handler* untuk *button* getData dan *button* POST! apabila di-*click*.
5. Pada `views.py`, Membuat *function* `add_task_ajax` untuk mengembalikan halaman `todolist_ajax.html` apabila *form* telah diisi dan
task telah ditambahkan.
