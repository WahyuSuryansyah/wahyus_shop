Nama : Mochammad Wahyu Suryansyah
NPM  : 2206083142
Kelas: PBP E
Kode Asdos: LKS

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

    Django UserCreationForm adalah sebuah form bawaan (built-in form) yang disediakan oleh Django, sebuah kerangka kerja pengembangan web Python yang populer. Form ini digunakan untuk membuat formulir pendaftaran user dalam aplikasi web yang memungkinkan user untuk membuat akun baru. UserCreationForm menyederhanakan proses pembuatan akun user dengan mengelola validasi data input dan proses penyimpanan data pengguna ke dalam database.

    Kelebihan:

        - UserCreationForm sangat mudah penggunaannya, kita dapat mengintegrasikannya dengan cepat dalam aplikasi kita tanpa perlu menulis kode validasi atau manipulasi data yang rumit.
        - Form ini memiliki validasi bawaan yang kuat untuk memastikan bahwa data yang dimasukkan oleh user adalah valid dan aman. Hal ini membantu menghindari serangan siber. 
        - UserCreationForm secara otomatis berinteraksi dengan model User yang sudah ada di Django, sehingga data pengguna baru akan disimpan di basis data dengan benar.

    Kekurangan:

        - Tidak memiliki field email sehingga tidak dapat melakukan verifikasi akun melalui email

        - Jika kita memerlukan fitur otentikasi lanjutan seperti otentikasi dua faktor (2FA) atau integrasi dengan layanan pihak ketiga, kita perlu menambahkan fungsionalitas tersebut sendiri.

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

    Autentikasi adalah proses memverifikasi identitas pengguna. Di dalam Django, autentikasi biasanya dilakukan saat pengguna mencoba untuk masuk ke dalam sistem dengan menyediakan kredensial seperti nama pengguna (username) dan kata sandi (password). Proses autentikasi tentu sangat penting dalam aplikasi web agar dapat memastikan bahwa hanya pengguna yang memiliki izin yang benar yang dapat mengakses sumber daya atau fitur tertentu dalam aplikasi kita. Hal ini membantu melindungi data dan mengidentifikasi pengguna secara sah.

    Otorisasi adalah proses mengendalikan akses pengguna ke sumber daya atau fitur tertentu setelah mereka berhasil diautentikasi.  Di dalam Django, otorisasi sering kali diimplementasikan menggunakan sistem perizinan (permission system). Hal ini memungkinkan kita untuk mengatur izin atau hak akses yang spesifik untuk pengguna atau grup pengguna tertentu. Otorisasi cukup penting untuk memastikan bahwa pengguna hanya dapat melakukan tindakan yang sesuai dengan peran atau izin mereka dalam aplikasi. Hal ini membantu melindungi data sensitif dan mencegah pengguna yang tidak berwenang mengakses atau mengubah sumber daya.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

    Cookies adalah sepotong data kecil yang disimpan di sisi klien (browser) saat user mengunjungi sebuah situs web. Cookies digunakan dalam konteks aplikasi web untuk menyimpan informasi di sisi klien yang dapat digunakan oleh server web untuk mengenali user yang kembali ke situs tersebut. 

    Django memiliki dukungan bawaan untuk mengelola cookies dan sesi user melalui modul django.contrib.sessions. Berikut adalah cara Django menggunakan cookies untuk mengelola data sesi user:

    1.  Memulai Sesi user
        Ketika seorang user pertama kali mengunjungi situs web Django, sesi user baru akan dimulai secara otomatis. Sebuah cookie khusus dengan ID sesi akan dibuat dan dikirimkan ke peramban user.
        
    2.  Menyimpan Data Sesi
        Saat user melakukan interaksi dengan situs web (misalnya, masuk, menambahkan barang ke keranjang belanja, atau mengisi formulir), Django dapat digunakan untuk menyimpan data sesi user dalam bentuk dictionary Python. Data ini akan dikaitkan dengan ID sesi yang sesuai.
    
    3.  Mengirimkan Cookie Kembali
        Setiap kali user membuat permintaan berikutnya ke situs web, web akan mengirimkan cookie sesi (berisi ID sesi) kembali ke server Django. Ini memungkinkan Django untuk mengidentifikasi sesi user yang sesuai.
    
    4.  Mengambil Data Sesi
        Django akan mengambil ID sesi dari cookie, mencocokkannya dengan sesi yang sesuai di server, dan mengembalikan data sesi user ke dalam aplikasi.
    
    5.  Mengambil Data Sesi
        Dapat menghapus atau mengubah data sesi user sesuai kebutuhan. Setelah user keluar atau sesi berakhir, data sesi dapat dihapus.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

    Penggunaan cookies dalam pengembangan web dapat menjadi alat yang berguna untuk menyimpan informasi pada sisi klien (browser) dan menjaga keadaan (state) aplikasi di seluruh sesi user. Namun, ada beberapa risiko potensial yang perlu diwaspadai terkait dengan penggunaan cookies.

    - Cookies dapat digunakan untuk menyimpan data sensitif, seperti token otentikasi atau informasi pengguna lainnya. Jika tidak diimplementasikan dengan benar, data ini dapat terpapar jika cookies diretas oleh pihak yang tidak berwenang.

    - Cookie Theft di mana Cookies yang tidak dienkripsi atau yang rentan terhadap serangan peretasan dapat dicuri oleh pihak yang tidak berwenang. Serangan pencurian cookies dapat memberikan akses kepada penyerang untuk mengakses akun pengguna yang terkait dengan cookies tersebut.

    - Cross-Site Scripting (XSS)Serangan yaitu XSS dapat memungkinkan penyerang menyisipkan skrip berbahaya ke dalam halaman web yang akan dieksekusi oleh browser pengguna. Dalam konteks cookies, penyerang dapat mencuri cookies pengguna melalui serangan XSS dan menggunakannya untuk mengakses akun pengguna.

    - Tracking Pengguna di mana Cookies juga digunakan oleh banyak situs web untuk melacak perilaku pengguna secara online. Beberapa pengguna mungkin menganggap ini sebagai pelanggaran privasi, terutama jika data yang dikumpulkan digunakan tanpa izin atau dengan cara yang tidak etis.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    Checklist 1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

        Registrasi
        Pertama, kita perlu menjalankan virtual environement terlebih dauhulu. Lalu kita import redirect, UserCreationForm, dan messages pada bagian paling atas kode views.py. Berikutnya kita perlu membuat fungsi regostrasi unutk membuat formulir otomatis dan aku baru. Lalu kita membuat templates register.html untuk mengatur bagaimana tampilan halaman web registrasi kita. Tidak lupa kita juga perlu impor fungsi registrasi tadi pada urls.py dan menambahkan path nyab ke dalam urlpatterns.

        Login dan Logout
        Langkahnya sama sebagaimana dalam pembuatan reistrasi hanya saja kita meingpor from django.contrib.auth import authenticate, login dan from django.contrib.auth import logout pada views.py

    Checklist 2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

        [![1.png](https://i.postimg.cc/Bvt61N3R/1.png)](https://postimg.cc/5Hd1hB6m)
        [![2.png](https://i.postimg.cc/pd7dQ8Xr/2.png)](https://postimg.cc/gwVdmxhb)

    Checklist 3. Menghubungkan model Item dengan User.
        Pertama, kita perlu mengimpor from django.contrib.auth.models import User pada models.py dan menambahkan potongan kode berikut:

        class Product(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)

    Checklist 4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

        Pertama, kita tambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas pada views.py dengan kode berikut:
        import datetime
        from django.http import HttpResponseRedirect
        from django.urls import reverse

        Selanjutnya kita mengganti kode yang ada pada blok if user is not None menjadi potongan kode berikut.
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        Pada fungsi show_main, kita tambahkan potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context
        context = {
            'name': 'Pak Bepe',
            'class': 'PBP A',
            'products': products,
            'last_login': request.COOKIES['last_login'],
        }


        Ubah fungsi logout_user menjadi seperti potongan kode berikut.
        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response

        Lalu agar last login dapat ditampilkan pada web kita, kita tambahkan potongan kode berikut di antara tabel dan tombol logout pada main.html.

        <h5>Sesi terakhir login: {{ last_login }}</h5>
      