Link aplikasi: https://tugas2-katalog-han.herokuapp.com/todolist/

# Pertanyaan Tugas 6

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronus programming merupakan proses berjalannya program secara bersamaan tanpa harus menunggu antrian (non-sequential). Sementara itu, synchronus berjalan secara sekuensial. Hal tersebut menyebabkan kode yang asynchronus dapat membuat program untuk dieksekusi segera. Berkebalikan dengan asynchronus, synchronus akan memblokir eksekusi kode selanjutnya sampai kode yang saat ini dijalankan selesai terlebih dahulu.
### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming adalah pemrograman yang kode-kodenya merupakan event-triggered. Jadi, kode tersebut baru akan dieksekusi jika ada suatu event yang dilakukan. Salah satu contoh penerapannya dalam tugas ini yaitu pada button Save Change yang ada di form, yang terletak di dalam modal. 
```Javascript
document.getElementById("button").onclick = addTodolist
```
Pada kode tersebut, penambahan task baru akan dilakukan, jika user klik tombol Save Change.
### Jelaskan penerapan asynchronous programming pada AJAX.
Penerapannya yaitu dengan mengirimkan data yang didapat dari misal suatu form, ke server di background, request data, atau menerima data ketika page sudah di-load. Jadi dengan asynchronus programming tersebut, kita bisa load data tanpa reload seluruh page.
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Caranya yaitu saya menambahkan dua fungsi baru di views.py, yaitu fungsi add dan show_json. Fungsi add berfungsi untuk memproses penambahan task baru melalui form, sedangkan fungsi show_json berfungsi untuk mendapatkan data dalam bentuk json, yang nantinya akan dipakai di script. Pemakaiannya untuk menampilkan data-data task di web. Setelah itu, dilakukan routing di url.py.
Kemudian, saya membuat form di dalam modal, serta memberikan id agar bisa diakses dari script nanti. Saya juga membuat sebuah table setelahnya.
Lalu, saya membuat tag script yang isinya merupakan fungsi-fungsi untuk menampilkan dan menambahkan task. Di sinilah implementasi asynchronus programming dilakukan. Untuk menghubungkan dengan views-nya, digunakan fetch yang disertai url ke views masing-masing. Looping dilakukan untuk menampilkan data-data, serta fungsi addTodolist dengan method post untuk memproses form. Terakhir, digunakan kode yang merupakan event-triggered untuk menyimpan task baru yang diinput user.
