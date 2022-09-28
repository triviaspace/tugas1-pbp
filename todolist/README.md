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
Elemen `<form>` biasanya dapat dibuat menggunakan generator seperti `{{ form.as_table }}`.

