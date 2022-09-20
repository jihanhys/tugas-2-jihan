**Link aplikasi Heroku:** https://tugas2-katalog-han.herokuapp.com/katalog/

**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html**
![Tugas 2 PBP - Han](https://user-images.githubusercontent.com/90143852/189931993-4b3c2fc0-0871-477c-aa6a-e9fb7e2ca088.png)

Client melakukan request dan request tersebut akan melalui urls.py. Kemudian, request diteruskan ke file views.py untuk diproses. Jika proses tersebut membutuhkan data dari database, akan dipanggil fungsi query ke file models.py dan database akan mengembalikan query, serta diteruskan ke views.py. Pada file tersebut,hasil query disimpan ke suatu variabel. Setelah data di-render di views.py, akan dilakukan mapping pada file html. Terakhir, data akan ditampilkan di web page.

**Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
Virtual environment dibutuhkan agar perubahan yang terjadi pada satu proyek Django tidak mempengaruhi proyek lainnya. Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi masalahnya adalah bisa terjadi conflict antara dependencies, dan virtual environment dapat mengatasi masalah tersebut. Sehingga disarankan untuk menggunakan virtual environment. Selain itu, misal terdapat PC dan laptop yang menggunakan versi Django yang berbeda, kita tetap bisa mengerjakan proyek yang sama pada PC dan Laptop tersebut karena sudah satu environment.

**Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4.**
**1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.**
**2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.**
**3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.**
**4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
Dalam melakukan step 1, saya membuat fungsi bernama show_catalog yang menerima parameter request dari user. Fungsi tersebut berisi statement yang akan ditampilkan melalui file katalog.html. Data tersebut berada di dalam dictionary bernama context yang di dalamnya terdapat nama, npm, dan item_catalog. item_catalog berisi data-data yang akan ditampilkan pada tabel di web.

Untuk pemetaan data yang sudah di-render di views.py, dilakukan pada file katalog.html. Untuk data tabel, dilakukan looping untuk mendapatkan data-data yang perlu ditampilkan pada tabel di web. Selanjutnya dilakukan routing pada file urls.py yang tersedia di folder katalog dengan menambahkan path untuk aplikasi katalog pada list urlpatterns. Hal ini berfungsi agar halaman html di templates bisa ditampilkan melalui browser. Tak lupa, untuk menambahkan aplikasi katalog ke dalam urlpatterns yang ada di file urls.py di folder project_django.

Setelah itu dilakukan add, commit, dan push. Kemudian, saya membuat secret repository untuk api key dan app name. Lalu, dilakukan re-run all jobs pada proyek terakhir yang failed.
