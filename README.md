Nama : Mochammad Wahyu Suryansyah
NPM  : 2206083142
Kelas: PBP E

Tautan menuju aplikasi Adaptablle: https://bookshop.adaptable.app/

SOAL 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    CHECKLIST 1. Membuat sebuah proyek Django baru.
        Pertama-tama, kita perlu membuat repository baru terlebih dauhulu pada Github.
        Lalu kita juga membuat direktori baru pada direktori lokal dan melakukan inisiasi git dengan "git init"
        Dilanjutkan dengan konfigurasi nama dan surel dengan :  git config user.name "<NAME>" & it config user.    email "<EMAIL>"
        Begitu juga dengan konfigurasi global : git config --global user.name "<NAME>" & git config --global user email "<EMAIL>"
        Dilanjutkan verifikasi konfigurasi dengan : git config --list --local
        Setelah itu, kita perlu ,enghubungkan repositori lokal dengan repositori di GitHub dengan :git branch -M main & git remote add origin <URL_REPO>

        Selanjutnya, kita perlu melakukan instalasi Django yakni mengaktifkan vitrual environment pada direktori lokal yang sudha kita buat tadi dengan : python -m venv env
        Lalu kita katifkan virtual environment tadi dengan env\Scripts\activate.bat
        Lalu, kita juga perlu menyiapkan dependencies dengan membuat bverkas requirements.txt yang berisi:
            django
            gunicorn
            whitenoise
            psycopg2-binary
            requests
            urllib3
        dan kita pasang dengan : pip install -r requirements.txt
        Lalu kkta buat proyek Django dengan django-admin startproject shopping_list .

        Selanjutnya, kita mengkonfigutrasi proyek dengan menabhakan * pada ALLOWED_HOSTS di settings.py 
        Lalu untuk menjalanakan server kta dapat menjalankan perintah pada shell di direktori lokal denhan : python manage.py runserver
        Tidak lupa kita juga pelru membuat .gitignore
        Lalu kita push dengan : git add ., git commit -m "pesan", dan git push -u origin main

    CHECKLIST 2. Membuat aplikasi dengan nama main pada proyek tersebut.
        Pertama kita perlu  mengaktifkan virtual environment pada direktori lokal yang telah kita baut tadi dengan env\Scripts\activate.bat
        Lalu baru kita dapat membuat aplikasi  main dengan perintah :python manage.py startapp main

    CHECKLIST 3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        Kita perlu mengubah urls.py pada direktori proyek kita dengan menambah:
        from django.urls import path, include
        urlpatterns = [
            ...
            path('main/', include('main.urls')),
            ...
        ]

    CHECKLIST 4. Membuat model pada aplikasi main dengan nama Item 
                Kita perlu mengubah models.py pada direktori main dengan:
                from django.db import models

                class Product(models.Model):
                    name = models.CharField(max_length=255) #name sebagai nama item dengan tipe CharField.
                    amount = models.IntegerField()          #amount sebagai jumlah item dengan tipe IntegerField.
                    description = models.TextField()      #description sebagai deskripsi item dengan tipe TextField.
                Tidak lupa kita juga pelru melakukan migrasi model dnegan : python manage.py makemigrations dan python manage.py migrate

    CHECKLIST 5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        Pertama kita perlu mengubah berkas views.py pada drektori main dengan :
                def show_main(request):
            context = {
                
                'name': 'Nama',
                'class': 'Kelas'
            }
            return render(request, "main.html", context)

    CHECKLIST 6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        Pertama kita perlu membuat beerkas urls.py pada direktori main dengan kode berikut:
        from django.urls import path
        from main.views import show_main
        from django.urls import path, include

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
            path('main/', include('main.urls')),

        ]

    CHECKLIST 7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses 
        Pertama, kita perlu menghubungkan Adaptable.io dengan GitHub dan pilih All Repositories pada proses instalasi.
        Pilih repositori proyek yang telah kita buat sebagai basis aplikasi yang akan di-deploy. lalu pilih branch main
        Pada proyek ini kita pilih Python App Template sebagai template deployment dan PostgreSQL sebagai tipe basis data yang akan digunakan.
        Untuk versi Python perlu disesuaikan dengan spesifikasi aplikasi masing-masing
        Pada bagian Start Command kita pelru memasukkan perintah python manage.py migrate && gunicorn nama_proyek.wsgi.
        Lalu masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasi di mana saya menggunakan nama bookshop
        Centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi.
        Maka kita tinggal menunggu web selesai dideploy
    
    CHECKLIST 8. Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy
        Untuk membuat readme dapat kita lakuakn dengan visual studio code
        Lalu pada folder kita klik new dile dan memberi nama README.md dan kita isi sesuai yang diinginkan


SOAL 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

                Client Request     ----->          Django        
                    (HTTP Request)                Web Server    
                                                                
                                    |
                                    |
                                    v
                                                
                                Django View    
                                (views.py)     
                                                
                                    |
                                    |
                                    v
                                                
                                Model Data     
                                (models.py)   
                                                
                                    |
                                    |
                                    v
                                                
                                HTML Template  
                                (HTML File)    
                                                
                                    |
                                    |
                                    v
                                                
                                Server Response 
                                (HTTP Response) 
                                                
                                    |
                                    |
                                    v
                                                
                                Client Browser  

    Penjelasan:

    erkas models.py adalah tempat kita mendefinisikan model-data aplikasi kita. Model-data ini menggambarkan bagaimana data akan disimpan dan diorganisir dalam database. Setiap model dalam models.py mewakili tabel dalam database atau dokumen dalam basis data (pada kasus aplikasi web berbasis NoSQL). Model-data ini digunakan untuk mengelola data, termasuk menambah, mengubah, menghapus, dan mengambil data dari database.

    Sedangkan views.py adalah tempat kita mendefinisikan logika aplikasi kita. Views mengatur bagaimana permintaan HTTP dari pengguna akan diproses. Mereka berinteraksi dengan model-data (dari models.py) untuk mengambil atau mengubah data, dan mereka menentukan apa yang harus ditampilkan kepada pengguna. Dalam banyak kasus, views juga berfungsi sebagai penghubung antara model dan template.

    lalu urls.py berfungsi sebagai penghubung antara URL yang diterima oleh aplikasi kita dan views yang sesuai. Ini berisi daftar pola URL dan menentukan view yang harus dipanggil ketika URL tertentu diakses oleh pengguna. Oleh karena itu, urls.py mengatur navigasi di dalam aplikasi kita.

    Dan HTML digunakan untuk merender tampilan yang akan ditampilkan kepada pengguna. Template HTML dapat mengambil data dari views dan model untuk menghasilkan tampilan yang dinamis. Template ini digunakan untuk mengatur tampilan halaman web kita, termasuk bagaimana data ditampilkan kepada pengguna.

    Adapun aliran data umum dalam aplikasi web Django adalah sebagai berikut:

        USer mengakses URL yang ditentukan dalam urls.py.

        urls.py menghubungkan URL tersebut dengan view yang sesuai dalam views.py.

        View dalam views.py mungkin akan berinteraksi dengan model-data dalam models.py untuk mengambil atau mengubah data dalam database.

        Setelah data diperoleh, view akan menggunakan template HTML untuk merender tampilan yang akan dikirimkan kembali kepada pengguna.


SOAL 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    Dengan menggunakan virtual environment dapat memungkinkan kita untuk membuat development environment yang terisolasi. hal Ini memugnkinkan kita memiliki berbagai proyek dengan versi Python dan library yang berbeda. Tentunya,  pada etiap proyek memiliki environment sendiri-sendiri dan tidak memengaruhi satu satu sama lain. 
    Di sinilah virtual environment berfungsi sehingga tidak ada konflik antar proyek di mana tiap proyek bisa saja memilii versi python dan library berbeda.

    Lalu, mengenai pembuatan aplikasi web berbasis Django tanpa virtual envirronment sebenarnya masih memungkinkan. Kita dapat menginstall langsung Django secara global pada sistem lalu mengerjakan web tersebut langsung apda global envrionmentnya.

SOAL 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

    MVC (Model View Controller)
    Suatu model yang seringkali digunakan oleh para pengembang software. Terdapat beebrapa komponen di dalam arsiteuktur ini yaitu:

        Model
        Berisi tentang logika bisnis dan status data yang ada di dalam aplikasi. Komponen ini bertugas untuk mendapatkan dan memanipulasi data, berkomunikasi dengan controller, berinteraksi dengan database, terkadang memperbarui tampilan dari aplikasi yang dikembangkan.

        View
        Komponen ini berhubungan dengan antarmuka pengguna yang terdiri dari HTML/CSS.XML. Komponen ini berkomunikasi dengan pengontrol dan terkadang berinteraksi dengan model. View berkerja sama dengan controller untuk menciptakan tampilan dinamis pada aplikasi yang dikembangkan. Selain bertugas untuk menangani antarmuka dan interaksi pengguna, komponen view juga memiliki tugas untuk menyajikan data yang sesuai untuk pengguna.

        Controller
        Controller adalah suatu aktivitas/fragmen yang berfungsi sebagai komunikator antara view dan model. Komponen ini membutuhkan suatu input pengguna dari layanan view/REST. Lalu Permintaan “Get Data” diproses dari model dan diteruskan ke view untuk ditampilkan ke pengguna.
    
    MVT (Model-View-Template)
    Sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Konsep ini memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.

        Model
        Bertanggung jawab untuk mengatur dan mengelola data dari aplikasi. Model mewakili struktur data dan logika aplikasi yang berada di belakang tampilan. Model menghubungkan aplikasi dengan basis data dan mengatur interaksi dengan data tersebut.

        View
        Berisi menangani logika presentasi dalam konsep MVT. View mengontrol bagaimana data yang dikelola oleh model akan ditampilkan kepada pengguna. Dalam konteks MVT, view berperan sebagai pengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna.

        Template
        Berfungsi untuk mengatur tampilan atau antarmuka pengguna. Template memisahkan kode HTML dari logika aplikasi. Dalam MVT, template digunakan untuk merancang tampilan yang akhirnya akan diisi dengan data dari model melalui view.

    MVMM (Model View ViewModel )
    Gabungan dari MVC dan MVP. MVVM awalnya digunakan di dalam Windows Presentation Foundation (WPF) dan Silverlight. Pola yang digunakan berdasarkan gabungan dari MVC dan MVP mencoba untuk lebih jelas dalam memisahkan pengembangan UI dari logika bisnis dan perilaku dalam aplikasi.

        Model
        Model yang digunakan untuk MVVM mirip dengan model yang digunakan MVC, dimana model tersebut terdiri dari data dasar yang digunakan untuk menjalankan perangkat lunak.

        View
        View digunakan sebagai antarmuka grafis antara pengguna dan pola desain, serta menampilkan output dari data yang telah diproses. View yang digunakan MVVM mirip dengan View yang digunakan dalam MVC.

        ViewModel
        ViewModel di satu sisi adalah abstraksi dari View, lalu di sisi yang lain, sebagai penyedia pembungkus data model untuk ditautkan. ViewModel terdiri dair Model yang diubah menjadi View, dan berisi perintah yang dapat digunakan oleh View untuk mempengaruhi Model.
    
    Perbedaan ketiganya:

        MVC memiliki pengontrol yang menggerakkan Model dan Tampilan. MVT memiliki Tampilan untuk menerima permintaan HTTP dan mengembalikan respons HTTP. Pada MVVM user berinteraksi dengan tampilan secara langsung yang berfungsi dengan model tampilan. Jika ada perubahan, hal ini terjadi secara langsung antara model tampilan dan model itu sendiri. Selain itu, MVC Highly coupled, sedangkan MVT dan MVVM Loosely coupled.

