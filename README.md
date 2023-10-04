Nama : Mochammad Wahyu Suryansyah
NPM  : 2206083142
Kelas: PBP E
Kode Asdos: LKS

Tugas 5

1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

    1. p {} Mengubah gaya semua teks pada elemen <p> menjadi warna merah
        p {
            ...
        }

    2. div {} Mengatur margin dan padding untuk semua elemen <div>
    div {
        ...
    }

    3. h2 {} Mengubah ukuran font untuk semua elemen <h2> menjadi lebih besar
    h2 {
        ...
    }

    4. a{} Mengubah gaya semua elemen <a> (link) untuk membuat teks menjadi tebal (bold) dan memberikan warna biru:
    a {
        ..
    }

    5. img {} Mengatur batas tepi (border) untuk semua elemen <img>
    img {
        ...
    }

    6. ul {} Mengubah gaya semua elemen <ul> (daftar tak terurut) untuk menghilangkan tanda bulatan (bullet) dan memberikan margin kiri
    ul {
        ...
    }

    7. strong {} Mengubah font tebal (bold) untuk semua elemen <strong> (teks tebal)
    strong {
        ...
    }

2. Jelaskan HTML5 Tag yang kamu ketahui.

    1. <header> Digunakan untuk mendefinisikan bagian atas atau kepala dari sebuah halaman atau bagian.

    2. <nav> Menandakan bagian yang berisi navigasi atau menu utama situs web.

    3. <main> Menunjukkan konten utama dari halaman web, yang biasanya berada di antara <header> dan <footer>.

    4. <article> Mengelompokkan konten independen yang dapat berdiri sendiri, seperti berita atau postingan blog.

    5. <section> Membagi konten menjadi bagian-bagian yang lebih kecil dan memiliki arti atau makna tertentu.

    6. <aside> Digunakan untuk konten tambahan yang berhubungan dengan konten utama, seperti sidebar atau iklan.

    7. <footer> Menunjukkan bagian bawah dari halaman atau bagian, biasanya berisi informasi tambahan seperti hak cipta atau tautan ke halaman terkait.

    8. <figure> dan <figcaption> <figure> digunakan untuk mengelompokkan konten multimedia, seperti gambar atau video

    9. <figcaption> digunakan untuk memberikan keterangan atau deskripsi tentang konten multimedia tersebut.

    10. <video> dan <audio> Digunakan untuk menyisipkan dan mengontrol video dan audio di halaman web.

    11. <canvas> Memungkinkan pembuatan gambar dan grafik menggunakan JavaScript.

    12. <form> Digunakan untuk membuat formulir interaktif yang memungkinkan pengguna untuk mengirim data ke server.

    13. <input> Membuat elemen input seperti teks, kata sandi, checkbox, radio button, dan lainnya dalam formulir.

    14. <textarea>  Membuat area teks yang lebih besar yang memungkinkan pengguna untuk memasukkan teks panjang.

    15. <button>  Membuat tombol yang dapat digunakan untuk tindakan interaktif, seperti mengirimkan formulir atau menjalankan fungsi JavaScript.

    16. <datalist>  Digunakan bersamaan dengan elemen input untuk menyajikan pilihan atau daftar autentikasi kepada pengguna.

    17. <progress>  Menunjukkan kemajuan atau status dalam operasi jangka panjang, seperti pengunggahan file atau pemrosesan data.

    18. <details> dan <summary> Digunakan untuk membuat elemen yang dapat diperluas atau disusutkan oleh pengguna dengan mengeklik <summary>.

    19. <mark> Digunakan untuk menyorot atau menandai teks dalam konten.

    20. <time>  Menandakan waktu atau tanggal dalam teks.

    21. <meter> Digunakan untuk menunjukkan skala atau rentang nilai numerik, seperti rating atau suhu.

   22.  <abbr> dan <acronym> Digunakan untuk menggambarkan singkatan atau akronim dan memberikan informasi tambahan saat pengguna mengarahkan kursor ke atasnya.

    23. <iframe> Digunakan untuk menyisipkan halaman web atau konten dari situs web lain ke dalam halaman web saat ini.

3. Jelaskan perbedaan antara margin dan padding.
    1. Margin
    Margin adalah ruang di sekitar elemen, di luar batas elemen tersebut. Biasanya, margin digunakan untuk memberikan jarak antara elemen dengan elemen lainnya di sekitarnya. Selain itu, margin tidak memiliki latar belakang atau warna. Lalu, margin tidak mempengaruhi ukuran atau bentuk elemen itu sendiri, tetapi mempengaruhi jarak antara elemen dan elemen-elemen lain di sekitarnya.
    
    2. Padding
    Sementara padding adalah ruang di dalam elemen, di antara konten elemen dan batas elemen. Biasanya, padding digunakan untuk memberikan ruang di sekitar konten elemen, terpisah dari batas elemen. Selain itu, padding dapat memiliki latar belakang atau warna, sehingga dapat mengubah tampilan latar belakang elemen di dalam padding. Lalu, padding juga mempengaruhi ukuran dan bentuk elemen, karena itu memengaruhi ruang di sekitar konten elemen.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

    Perbedaan utama antara Tailwind dan Bootstrap adalah pendekatannya terhadap CSS. Bootstrap adalah framework CSS berbasis komponen, yang berarti menyediakan kumpulan komponen siap pakai yang dapat Anda gunakan untuk membangun situs web dan aplikasi web. Tailwind, di sisi lain, adalah framework CSS berbasis utilitas, yang berarti menyediakan kumpulan kelas utilitas yang dapat Anda gunakan untuk menyesuaikan tampilan dan nuansa situs web Anda.

    Bootstrap
    Waktu yang tepat untuk menggunakan bootstrap adalah saat ingin mengembangkan proyek dengan cepat dan tidak memiliki banyak waktu untuk merancang tampilan dari awal, karena komponen UI yang telah ditentukan sebelumnya dan desainnya yang konsisten. Sehingga, tidak perlu lagi memakan banyak waktu mengotak atik CSS kustom.

    Tailwind
    Waktu yang tepat untuk menggunakan tailwind  adalah saat kita ingin memiliki fleksibilitas tinggi dalam merancang tampilan sesuai dengan kebutuhan proyek, karena Tailwind memungkinkan kita untuk merancang tampilan dengan menggunakan kelas-kelas utilitas. Sehingga,ukuran file CSS kita juga akan berkurang untuk meningkatkan kecepatan muat halaman.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Halaman Login
        Pertama, saya mengubah latar belakang header card menjadi warna biru (.bg-primary) dan teks menjadi putih (.text-white). Tombol "Login" juga menjadi warna biru (btn-primary). Negitu juga pada teks register now.
    2. Halaman register
        Pertama, saya menggunakan container dan row Bootstrap untuk mengatur tata letak keseluruhan. Lalu, agar lebih rapi saya ,menggunakan card Bootstrap untuk mengelilingi formulir pendaftaran. Agar lebih berwarna, saya memberikan header card dengan latar belakang biru (bg-primary) dan teks putih (text-white). Dan memberi warna tombol "Daftar" dengan kelas btn btn-primary.
    3. halaman Utama
        Pertama saya membuat navbar dengan lataer belakang biru dan tomobol logout merah dan tulisan Judul Wahyus Shop Page Putih denga kode berikut.
          <a class="navbar-brand" href="#" style="color: white;">Wahyus Shop Page</a>
        Lalu untuk tombol logoutnya saya tambahkan class="btn btn-danger" untuk memberi warna merah 
            <button class="btn btn-danger">
                      Logout
                  </button>
        Dan untuk table agar memiliki bordr dan isi lebih berwarna saya menambahkan kode berikut
            <table class="table table-bordered table-striped bg-light">

    4. Halaman Add New Product    
        Agar halaman lebih berwarna, saya memberi warna header card biru dengan kode berikut
         <div class="card-header bg-primary text-white">
            <h1 class="card-title">Add New Product</h1>
        </div> 
        Lalu saya menaruh formulir di card agar lebih rapi
             <div class="card-body"></div>
        dan memberi margin agar lebih tertata
            <table style="margin: 20px;">

