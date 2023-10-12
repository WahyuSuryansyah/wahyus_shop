Nama : Mochammad Wahyu Suryansyah
NPM  : 2206083142
Kelas: PBP E
Kode Asdos: LKS

Link: 

Tugas 6

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

    - Synchronous Programming
    Setiap tugas dieksekusi satu per satu secara berurutan. Saat satu tugas sedang menunggu operasi yang memerlukan waktu maka seluruh program akan terhenti sampai operasi itu selesai. Hal ini dapat menyebabkan program terasa lambat dan tidak responsif, terutama dalam aplikasi yang melakukan banyak operasi I/O.

    - Asynchronous Programming
    Berbeda dengan synchronus programming, tugas-tugas yang memerlukan waktu dapat berlanjut ke tugas berikutnya tanpa harus menunggu tugas sebelumnya selesai. Ketika tugas asinkron menunggu operasi yang memerlukan waktu, seperti I/O atau jaringan, ia tidak akan menghentikan seluruh program. Sebaliknya, ia akan melepaskan CPU dan mengizinkan tugas-tugas lain untuk berjalan. Hal ini lah yang membuat program menjadi lebih responsif dan dapat meningkatkan kinerja dalam situasi di mana ada banyak tugas yang memerlukan waktu.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

    Sebuah pendekatan dalam pemrograman di mana program merespons events yang terjadi secara asinkron. Biasanya, berupa interaksi pengguna seperti mengklik tombol, mengisi formulir, atau merespons data eksternal seperti respons dari server atau data sensor. Program yang dibangun dengan paradigma event-driven akan mengeksekusi fungsi atau tindakan tertentu ketika peristiwa-peristiwa ini terjadi.

    Contoh:
    Penggunaan tombol "Delete" untuk menghapus produk adalah salah satu contoh penerapan paradigma event-driven programming. Saat pengguna mengklik tombol "Delete" pada suatu produk, sebuah event (klik) terjadi. Hal ini memicu fungsi JavaScript deleteProduct(productId) yang telah ditetapkan sebagai respons terhadap event tersebut. Fungsi ini kemudian mengirim permintaan AJAX DELETE ke server untuk menghapus produk yang dipilih.

3. Jelaskan penerapan asynchronous programming pada AJAX.

    Penerapan asynchrinus pada AJAX berupa data transfer (HTTP request) yang dilakukan di belakang  tanpa perlu refresh halaman atau postback antara browser dan web server sehingga halaman web dapat memanggil bit yang keicl atau seluruh data/informasi dari server tersebut. Dengan demikian, aplikasi web dapat menjadi lebih cepat dan user friendly.

4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

    - JQuery
        ~ Tidak perlu membuat instance objek dari XMLHTTPRequest. 
        ~ Kita perlu menambahkan library JQuery pada project. 
        ~ Response handling dapat dilakukan secara langsung dengan memanggil fungsi done dan fail.
        ~ Perlu menulis lebih banyak baris kode sehingga memperlambat kecepatan waktu muat karena terjadi pemuatan file yang tidak perlu.

    - Fetch API
        ~ Menggunakan Promises yang memungkinkan API lebih sederhana sehingga menghindari callback hell dan harus mengingat API kompleks XMLHttpRequest.
        ~ Response handling dengan memnggunakan fungsi then (jika Promise tersebut mengembalikan resolve) dan catch (jika Promise tersebut mengembalikan reject).
        ~ Dapat digunkan untuk mealkukan fetch berbagai tipe data, hal ini dikarenakan Fetch API tidak mengasumsikan tipe data respon yang akan diperloeh.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

    Checklist 1. Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX. 

     - AJAX GET

        Ubahlah kode cards data item agar dapat mendukung AJAX GET.

        Lakukan pengambilan task menggunakan AJAX GET.

     - AJAX POST

        1. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.

        Pertama, kita perlu membuat fungsi baru pada block 
        <Script> dengan nama addProduct()

        <script>
            function addProduct() {
                fetch("{% url 'main:add_product_ajax' %}", {
                    method: "POST",
                    body: new FormData(document.querySelector('#form'))
                }).then(refreshProducts)

                document.getElementById("form").reset()
                return false
            }
        </script>
        
        Kode tersebut digunakan untuk membuat sebuah FormData baru yang datanya diambil dari form pada modal sehingga data dapat dikirimkan dari form tersebut ke server. Lalu, document.getElementById("form").reset() digunakan untuk mengosongkan isi field form modal setelah di-submit. Agar dapat menambahkan product, kita juga perplu menambahkan tombol sebagai berikut:
        
        <script>
        ...
        document.getElementById("button_add").onclick = addProduct
        </script>

        2. Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.

        3. Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.

        4. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.

        5. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.

    Checklist 2. Melakukan perintah collectstatic.


Referensi:
https://www.dicoding.com/blog/mengenal-fungsi-asynchronous-request-pada-javascript/
https://medium.com/@reemshakes/is-ajax-getting-replaced-by-fetch-api-55207234793f
https://wesbos.com/javascript/13-ajax-and-fetching-data/74-ajax-and-apis