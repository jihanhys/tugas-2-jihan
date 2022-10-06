Link aplikasi: https://tugas2-katalog-han.herokuapp.com/todolist/
## Pertanyaan tugas 5
### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Inline style: inline tag dari html <p style=”….”>
Keuntungan: Bisa memasukkan kode css ke html dengan cepat, berguna untuk testing atau melihat preview perubahan
Kekurangan: Menambahkan kode css ke setiap elemen di html itu memakan banyak waktu dan membuat struktur file html menjadi tidak rapih.
2. Internal style sheet: menambahkan <style> pada section head di html
Keuntungan: kita bisa menggunakan class dan id selector di style sheet jenis ini.
Kekurangan:Menambahkan kode css tersebut ke dokumen html dapat meningkatkan ukuran page dan waktu laoding.
3. External style sheet: file yang terpisah dari html
Keuntungan: file html memiliki struktur yang lebih "clean" dan kita bisa menggunakan file .css yang sama untuk halaman yang berbeda.
Kekurangan: Page web kita bisa tidak di-render dengan benar sampai external css sudah loaded sepenuhnya
Untuk proyek skala besar, lebih baik menggunakan external style sheet.
### Jelaskan tag HTML5 yang kamu ketahui.
1. div: bisa dibilang sebagai mark-up yang tidak terlalu meaningful karena dapat terlalu general.
2. nav: menspesifikasikan sebuah section dari dokumen sebagai navigasi.
3. section:merepresentasikan sebuah section untuk dokumen atau aplikasi yang general.
4. form: menspesifikasikan sebuah form
5. button: membuat sebuah button
6. hr: membuat sebuah garis horiontal
7. img: menspesifikasikan sebuah foto
8. input: untuk field yang mengambil input
9. table: menspesifikasikan sebuah table
10. td: cell dari table
11. tr: row dari table
12. th: header dari table
  
### Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Tipe-tipe CSS selector ada tiga, yaitu element selector, class selector, dan ID selector.
- Element selector tidak pakai tanda pagar (tidak ada tanda apa-apa sebelum deklarasi di css-nya)
- Class selector mengunakan tanda titik di depannya
Digunakan untuk deskripsikan style tag dengan class tertentu
- ID selector menggunakan tanda pagar di depannya
Deklarasinya mendeskripsikan untuk halaman html yang id-nya ada p1

### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.
Cara saya mengimplementasikan checklist di atas yaitu dengan mendesain html yang sudah dibuat dengan internal css. Saya menambahkan link css untuk menerapkan css pada file .html tersebut. Kemudian menambahkan tag <style> pada section <head> di file .html. Untuk cards, saya menambahkan tag <div> dengan class bernama card pada section body. Kemudian, mendesain-nya dengan pada bagian internal css seperti margin, border-radius agar ujung dari card menjadi tumpul, serta menggunakan hover untuk memberikan efek shadow bagi card.

## Pertanyaan tugas 4
### Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?
csrf_token digunakan untuk menangani threats berupa CSRF. CSRF merupakan sebuah serangan anggap saja dari hacker, yang akan mengirimkan form buatan dia sendiri. Dengan csrf_token, token akan dicek oleh fungsi views yang menangani action. Jika valid akan dikirim ke server. Jika tidak valid seperti tidak ada tokennya, maka tidak akan diproses. Jika potongan kode ini tidak ada, maka form buatan kita yang ada di database menjadi tidak terproteksi, sehingga bila ada hacker bisa saja mengirimkan form buatan dia sendiri, bukannya form yang seharusnya. Saat kita run aplikasi, akan muncul verification failed dan request tidak bisa diproses.
  
### Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.
Kita bisa membuat form secara manual tanpa menggunakan built-in methods seperti form.as_table, form.as_p, atau form.as_ul.Caranya yaitu dengan mengedit konten html menggunakan CSS. Jadi, bukannya dengan form.as_table, tetapi dengan mengakses atribut di models satu-satu dengan form pada section masing-masing. Misal untuk atribut di todolist, maka akan diakses form.title, form.description, dst.
### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
User melakukan request pada browser. Lalu, akan di-generate http request yang diminta user. Server akan menerima request dari user, dan akan mencari views yang menangani path yang di-request. Kemudian akan di-generate halaman form. Halaman form dikirimkan sebagai response ke user, ditampilkan di browser. User isi form, lalu click submit. Form yang sudah diisi, dikirim ke alamat yang ada di bagian action pada file HTML. Lalu dikirim ke server. Kemudian server akan cek dan cari views yang menangani form. Terakhir, page HTML akan di-display ke user.
  
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama, untuk membuat suatu aplikasi baru bernama todolist, saya menjalankan perintah python manage.py startapp todolist. Kemudian, secara otomatis, Django akan menyediakan beberapa file yang kita butuhkan kecuali urls.py, forms.py, serta folder templates untuk menyimpan file html. Saya juga mendaftarkan aplikasi todolist di settings.py pada folder project_django.
Kedua, untuk menambahkan path todolist, akan ditambahkan pada urls.py di folder project_django.
Ketiga, pembuatan model Task dilakukan pada file models.py dengan atribut user, date, title, dan description. Atribut user menggunakan Foreign Key dengan parameter User karena merepresentasikan relationship many-to-one.
Keempat, implementasi form, registrasi, login, dan logout dilakukan dengan membuat fungsi-fungsi di views.py(add_task, register, login_user, dan logout_user) serta file html(create-task.html, register.html, login.html) untuk menampilkannya di web browser. Untuk form saya membuat file baru bernama forms.py. Jadi, form-nya tidak pada file html.
Kelima, halaman utama todolist dibuat dengan membuat fungsi show_task dan file todolist.html. Data di database, yang diakses melalui models di-loop untuk menampilkan data-data sesuai user. Penyesuaian data dengan user masing-masing dilakukan dengan melakukan filter. Tombol "Tambah Task Baru" diimplementasikan dengan menambahkan button dengan url yang mengarah ke halaman yang memproses penambahan task tersebut.
Keenam, pembuatan halaman form dilakukan dengan membuat file forms.py. Fields-nya berisi atribut yang datanya akan dimodifikasi/ditambah oleh user.
Ketujuh, routing dilakukan dengan penambahan path di urls.py di folder todolist.
Kedelapan, untuk deploy ke heroku cukup dilakukan dengan add, commit, dan push ke github. Lalu, akan secara otomatis di-deploy sampai ada tanda centang hijau.
Kesembilan, pembuatan akun pengguna dan dummy data dengan register 2 akun baru. Kemudian, login pada masing-masing akun, serta menambahkan data berupa task baru sesuai masing-masing user.
