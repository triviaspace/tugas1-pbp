# Tugas 4
Pada tugas ini, kita mengimplementasikan Form dan Autentikasi Menggunakan Django <br/>
Berikut link aplikasi website, [HerokuApp Pages](https://tugas2-pbp-safa.herokuapp.com/).

## Kegunaan `{% csrf_token %}` Pada Elemen `<form>`
Tag `{% csrf_token %}` dapat diimplementasikan untuk menghindari *malicious attack* (serangan terhadap 
suatu sistem komputer atau jaringan dengan cara mengeksploitasi kelemahan pada sistem). Tag ini akan melakukan
*generate token* pada *server side* ketika page sedang di-*render* dan akan memastikan untuk *cross-check* token
setiap ada *request* yang masuk. Jika *request* yang masuk tidak berisi token, maka *request* tersebut tidak akan dieksekusi.
Form tidak akan dapat berjalan dengan baik apabila tidak ada `(% csrf_token %}` karena akan terjadi *Invalid or missing CSRF token*.

## Apakah Elemen `<form>` Dapat Dibuat Secara Manual Tanpa Generator?
Elemen `<form>` dapat dibuat menggunakan generator seperti `{{ form.as_table }}`. Namun, kita juga dapat membuatnya secara manual pada html
dengan `<form>` dan menyertakan `<input type="submit">` untuk melakukan *submit form*. Untuk dapat mengisi input, kita juga dapat menambahkan
elemen `<input>`. </br></br>
Kita dapat menggunakan cara lain, yaitu dengan menampilkan setiap parameter form menjadi suatu elemen.

## Alur Data
Ketika tombol submit telah di-*click* oleh *user*, data-data yang dimasukkan akan dicek oleh sistem. Apabila terdapat kesalahan *input*, *user* diarahkan untuk mengisi *form* kembali. Jika data yang diberikan benar, maka `models.py` akan memuat data-data tersebut lalu disimpan ke dalam *database*. Saat diperlukan, `models.py` akan mengambil data dari *database* dan dikirim untuk ditampilkan oleh *file* HTML.

## Proses Implementasi Form dan Autentikasi
1. Untuk membuat app baru, Menjalankan perintah `python manage.py startapp todolist` pada projek Django.
2. Menambahkan `path('todolist/', include('todolist.urls'))` pada `file project_django/urls.py`.
3. Membuat model `Task` berisi atribut-atribut `user`, `date`, `title`, dan `description` pada `models.py`.
4. Mengimplementasikan form registrasi, *login*, dan *logout* dengan membuat *function* `register`, `login_user`, dan `logout_user` pada `views.py`. Lalu, membuat folder `templates` berisi file-file HTML, seperti `login.html` dan `register.html`.
5. Membuat sebuah `todolist.html` sebagai halaman utama. Pada `views.py`, menambahkan *function* `show_todolist` untuk menampilkan data-data yang dibutuhkan.
6. Pada `views.py`, membuat *function* `create_task` untuk mengimplementasikan pembuatan *Task* baru. Lalu, Membuat template `create-task.html`.
7. Menambahkan file `urls.py` pada folder `todolist` dan mengisi url yang diperlukan dalam *app* todolist.
8. Melakukan *push code* ke *repository* GitHub, sekalian akan melakukan *deployment* secara otomatis.
9. Membuat dua akun pengguna dan tiga *dummy data* menggunakan model *Task* pada akun masing-masing di situs web Heroku.
