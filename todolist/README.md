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

# Tugas 5
Pada tugas ini, kita mengimplementasikan Web Design <br/>
Berikut link aplikasi website, [HerokuApp Pages](https://tugas2-pbp-safa.herokuapp.com/todolist).

## Implementasi CSS
Terdapat 3 cara mengimplementasi CSS dalam HTML, yaitu :
1. Inline CSS
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. 
Setiap elemen HTML memiliki atribut style dan di situ lah inline CSS ditulis.
Cara ini cukup bermanfaat apabila kita ingin menguji dan melihat perubahan pada satu elemen.
Namun, cara ini kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. 

2. Internal CSS
Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. 
Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.
Cara ini berguna apabila kita ingin melakukan perubahan style pada satu halaman saja, namun penulisan CSS harus diulang apabila kita
ingin mengimplementasikannya di halaman lain.
  
3. External CSS
Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. 
File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.
Cara ini lebih sederhana dan mudah dibandingkan menambahkan kode CSS di setiap elemen HTML yang ingin kita atur tampilannya.
Kekurangannya adalah halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. 
Hal ini biasanya terjadi disebabkan karena koneksi internet yang lambat.
  
## Macam-macam tag HTML5 beserta fungsinya
(bisa cek di https://www.w3schools.com/TAGS/default.asp)
  
## CSS Selector
Terdapat beberapa cara implementasi CSS berdasarkan selector-nya, yaitu :
- Untuk Elemen, bisa menggunakan nama elemen html, seperti p{}, h1{}, dst.
- Untuk ID, bisa menggunakan nama id dan menyertakan # di awalannya, seperti #contohID{}.
- Untuk Class, bisa menggunakan nama class dan menyertakan . di awalannya, seperti .contohClass{}.

## Proses Implementasi Web Design
Dengan melakukan penambahan style CSS secara inline dan eksternal CSS. Lalu, setiap task baru, membuat penambahan card di laman html yang dapat mengimplementasi belum selesai/selesai dan fitur hapus. 
