Link aplikasi: https://tugas2-katalog-han.herokuapp.com/mywatchlist/

### Jelaskan perbedaan antara JSON, XML, dan HTML!
HTML dan XML merupakan markup language, tetapi  fungsi dari kedua hal tersebut cukup berbeda. HTML akan men-display data dan mendeskripsikan struktur dari sebuah webpage, sementara XML menyimpan dan men-transfer data. Funsi JSON juga mirip dengan XML, tetapi penyimpanan informasinya berbeda. XML merupakan informasi yang dibungkus di dalam tag, sedangkan format JSON berbentuk text sehingga lebih mudah untuk dibaca.

Dalam implementasinya, JSON mengirimkan data dengan menguraikannya terlebih dahulu, lalu dikirimkan melalui internet. Sementara itu, XML mempunyai data yang jauh lebih terstruktur. JSON menyimpan elemen secara efisien, tetapi tidak rapi. Penyimpanan elemen pada XML lebih terstruktur dan mudah dibaca oleh manusia dan mesin, tetapi kurang efisien.

Fokus dari bentuk data pada data delivery juga berbeda-beda, seperti XML yang lebih berfokus pada pertukaran informasi, sedangkan HTML lebih interaktif karena appearace webpage dapat diedit dengan HTML.

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena dalam mengembangkan sebuah platfom, kita bisa saja butuh untuk mengirim data dari satu stack ke stack lainnya. Bentuk data yang dikirimkan bisa bermacam-macam seperti JSON, XML, dan HTML. Selain itu, data delivery juga penting karena dengan data delivery, data-data yang kita punya bisa ditampilkan pada web.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama, untuk membuat suatu aplikasi baru bernama mywatchlist, saya menjalankan command python [manage.py](http://manage.py/) startapp mywatchlist. Nah, dari sini, Django secara otomatis generate file-file yang dibutuhkan seperti admin.py, apps.py, models.py, dan views.py.

Selanjutnya, saya mendaftarkan aplikasi mywatchlist di [settings.py](http://settings.py) dan juga menambahkan path-nya di [urls.py](http://urls.py) pada folder project_django. Dalam pembuatan model MyWatchList di models.py, saya membuat 5 atribut yang data dari ke-5 atribut tersebut saya buat pada file initial_watchlist_data.json. Ketika data-data yang diperlukan sudah ditambahkan pada file tersebut, maka dilakukan migrasi dan loaddata.

Untuk implementasi fitur untuk menyajikan data yang telah dibuat sebelumnya dalam format HTML, XML, dan JSON, saya membuat beberapa fungsi di [views.py](http://views.py), untuk menampilkan data dalam format-format yang diminta.

Kemudian, membuat routing pada [urls.py](http://urls.py) dengan menambahkan beberapa path sesuai dengan kebutuhan dari HTML, JSON, dan XML. Saya juga menyediakan data dalam format JSON berdasarkan ID dari masing-masing data yang di-assign di initial_watchlist_data.json dengan nama pk. Ketika semua pekerjaan sudah selesai, dilakukan add, commit, dan push ke github, serta deploy aplikasi mywatchlist ke heroku. Setelah itu, agar data yang ada pada templates juga ditampilkan di heroku, saya menjalankan python manage.py loaddata initial_watchlist_data.json di console heroku.

Screeshot pengaksesan localhost via postman:
![2022-09-21 (2)](https://user-images.githubusercontent.com/90143852/191447495-aa49172e-0fc8-4f0a-8760-2da2ebbccc42.png)
![2022-09-21 (3)](https://user-images.githubusercontent.com/90143852/191447517-423f6eba-dbba-4bc3-b326-445578d34feb.png)
![2022-09-21 (4)](https://user-images.githubusercontent.com/90143852/191447541-1dd84eaa-0a53-4b59-b8b4-8bfb4f0acf98.png)
