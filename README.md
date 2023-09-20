Nama : Mochammad Wahyu Suryansyah
NPM  : 2206083142
Kelas: PBP E
Kode Asdos: LKS

1. Apa perbedaan antara form POST dan form GET dalam Django?

    POST
    - Metode POST digunakan untuk mengirim data ke server dengan tujuan membuat, mengubah, atau menghapus data di server. Biasanya juga digunakan untuk mengirim data yang akan dimasukkan ke dalam basis data atau sebagai tindakan yang akan mengubah status server.
    - Data yang dikirm biasanya data sensitif seperti kata sandi karena saat dikirim dalam badan permintaan HTTP, data tidak terlihat oleh pengguna.
    - Tidak ada batasan ukuran data yang dapat dikirim.

    GET
    - Metode GET digunakan untuk mengambil data dari server di mana kita hanya ingin mendapatkan data dari server tanpa mempengaruhi status atau data di server.
    - Data yang dikrim dapat dilihat oleh pengguna di mana data dikirim sebagai bagian dari URL. 
    - Ada batasan panjang URL yang dapat berbeda-beda tergantung pada server dan browser.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

    XML
    - XML merepresentasikan data dalam pola pohon
    - XML mendukung semua tipe data JSON dan tipe-tipe tambahan, seperti Boolean, tanggal, citra, dan namespace. 
    - Digunakan untuk mendefinisikan struktur data dengan tag-tag yang dapat disesuaikan di mana kitadapat membuat format data sendiri sesuai dengan kebutuhan.
    - Biasanya digunakan untuk pertukaran data antar sistem dan penyimpanan data terstruktur.
    - Kurang efisien untuk penggunaan data yang besar karena memiliki overhead dalam hal ukuran file yang disebabkan oleh tag-tagnya yang lengkap. 
    - Parsing XML memerlukan upaya lebih daripada format lain seperti JSON.

    JSON
    - JSON merepresentasikan data menggunakan pasangan kunci-nilai. 
    - JSON mendukung angka, objek, string, dan array Boolean.
    - struktur data yang lebih sederhana dibandingkan dengan XML di mana terdiri dari pasangan nama-nilai yang disusun dalam objek dan larik.
    - Biasanya digunakan secara luas dalam pengembangan web dan pertukaran data antara aplikasi web dan server. 

    HTML
    - digunakan untuk menggambarkan struktur dokumen web yang terdiri dari elemen-elemen seperti tag, atribut, dan teks.
    - Biasanya digunakan untuk membuat halaman web dan menampilkan data kepada pengguna melalui peramban web. 
    - Tidak digunakan untuk pertukaran data antar sistem atau penyimpanan data terstruktur seperti XML atau JSON.
    
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

    - Format data JSON ringkas dan mudah dibaca oleh manusia. Strukturnya berupa pasangan nama-nilai yang berfungsi seperti objek dan larik dalam JavaScript. Keterbacaan yang baik membuatnya ideal untuk debugging dan pengujian.
    - JSON memungkinkan untuk pengambilan data parsial dalam aplikasi web modern yang berbasis JavaScript. Hal ini berarti kitacdapat memuat hanya bagian-bagian data yang diperlukan dari server sehingga mengurangi beban lalu lintas dan waktu pengunduhan.
    - JSON dapat digunakan dengan mudah di berbagai bahasa pemrograman karena banyak bahasa memiliki dukungan untuk memparsing JSON. Hal ini memungkinkan aplikasi yang berjalan di berbagai platform dan bahasa berkomunikasi dengan mudah.
    - JSON adalah bagian dari JavaScript, hampir semua peramban web modern memiliki dukungan bawaan untuk memparsing JSON. Hal ini tentu memudahkan komunikasi antara peramban web dan server.
    - Format JSON yang ringan di mana format JSON biasanya memiliki ukuran yang lebih kecil dibandingkan dengan format lain seperti XML. Hal ini tentu mengurangi beban lalu lintas dan waktu yang diperlukan untuk mentransmisikan data.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Checklist 1. Membuat input form untuk menambahkan objek model pada app sebelumnya.
        - Mengatur Routing dari main/ ke /
          Sebelumnya, kita perlu mengaktifkan virtual environment terlebih dahulu dengan: env\Scripts\activate.bat
          Lalu, kita Bbuka urls.py yang ada pada folder wahyus_shop dan mengubah path main/ menjadi '' pada urlpatterns
        - Implementasi Skeleton sebagai Kerangka Views
          Kita buat folder templates pada root folder yang berisi sebuah berkas HTML baru bernama base.html dengan kode berikit:
                {% load static %}
                    <!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset="UTF-8" />
                            <meta
                                name="viewport"
                                content="width=device-width, initial-scale=1.0"
                            />
                            {% block meta %}
                        </head>

                        <body>
                            {% block content %}
                            {% endblock content %}
                        </body>
                    </html>

          Lalu kita tambahkan kode: 'DIRS': [BASE_DIR / 'templates'], pada settings.py di subdirektori wahyus_shop
            
        - Membuat Form Input Data dan Menampilkan Data Produk Pada HTML
            Pertama, kita buat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form yang dapat menerima data produk baru, yang berisi kode berikut:
                    from django.forms import ModelForm
                    from main.models import Product
                    class ProductForm(ModelForm):
                        class Meta:
                            model = Product
                            fields = ["name", "price", "description"]

            Lalu kita import: from django.http import HttpResponseRedirect, from main.forms import ProductForm, from django.urls import reverse pada views.py di main
            Selanjutnya, kita buat fungsi baru dengan nama create_product dengan kode berikut:
                def create_product(request):
                    form = ProductForm(request.POST or None)

                    if form.is_valid() and request.method == "POST":
                        form.save()
                        return HttpResponseRedirect(reverse('main:show_main'))

                    context = {'form': form}
                    return render(request, "create_product.html", context)

            Kita juga perlu mengubah fungsi show_main pada views.py menjadi:
                def show_main(request):
                    products = Product.objects.all()

                    context = {
                        'name': 'Pak Bepe', # Nama kamu
                        'class': 'PBP A', # Kelas PBP kamu
                        'products': products
                    }
                    return render(request, "main.html", context)

            Tidak lupa kita harus mengimport fungsi create_product yang sudah dibuat tadi dengan: from main.views import show_main, create_product pada urls.py pada main

            Tambahkan path url ke dalam urlpatterns pada urls.py di main path('create-product', create_product, name='create_product'),
            Buat berkas HTML baru dengan nama create_product.html pada direktori main/templates
                {% extends 'base.html' %} 

                {% block content %}
                <h1>Add New Product</h1>

                <form method="POST">
                    {% csrf_token %}
                    <table>
                        {{ form.as_table }}
                        <tr>
                            <td></td>
                            <td>
                                <input type="submit" value="Add Product"/>
                            </td>
                        </tr>
                    </table>
                </form>

                {% endblock %}

            Menambahkan kode berikut pada main.html 
                <table>
                    <tr>
                        <th>Name</th>
                        <th>Price</th>
                        <th>Description</th>
                        <th>Date Added</th>
                    </tr>

                    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

                    {% for product in products %}
                        <tr>
                            <td>{{product.name}}</td>
                            <td>{{product.price}}</td>
                            <td>{{product.description}}</td>
                            <td>{{product.date_added}}</td>
                        </tr>
                    {% endfor %}
                </table>

                <br />

                <a href="{% url 'main:create_product' %}">
                    <button>
                        Add New Product
                    </button>
                </a>

                {% endblock content %}

    Checklist 2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

        XML
        - Pertama, kita buka views.py yang ada pada folder main dan tambahkan import HttpResponse dan Serializer pada bagian paling atas.
            from django.http import HttpResponse
            from django.core import serializers
        - Lalu, kita buat sebuah fungsi yang menerima parameter request dengan nama show_xml dan buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada Product.
            def show_xml(request):
                data = Product.objects.all()
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        - Buka urls.py yang ada pada folder main dan import fungsi yang sudah kita buat tadi.
            from main.views import show_main, create_product, show_xml 

        JSON
        - Pertama, kita buat sebuah fungsi baru yang menerima parameter request dengan nama show_json pada views.py pada main
            def show_json(request):
                data = Product.objects.all()
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        -  Lalu kita import fungsi yang sudah kamu buat tadi pada urls/py di main
            from main.views import show_main, create_product, show_xml, show_json
        
        XML dan JSON by id
         - Pertama, kita buka views.py yang ada pada folder main dan buatlah sebuah fungsi baru yang menerima parameter request dan id dengan nama show_xml_by_id dan show_json_by_id.
        XML
        def show_xml_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        JSON
        def show_json_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
    Checklist 3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
        XML
        - Kita hanya perlu menambah path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
            ...
            path('xml/', show_xml, name='show_xml'), 
            ...
        JSON
        - Kita hanya perlu menambah path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
            ...
            path('json/', show_json, name='show_json'), 
            ...
        XML dan JSON by id
        - Kita hanya perlu menambah path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
            ...
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
            ...

    Checklist 4. Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
       - Cukup mengedit file README.md yang sudah dibuat sebelumnya (pada tugas 2)

5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

    https://drive.google.com/drive/folders/1OBfYmqePJFi1jWleWaUf_FM3UQxzxrLX?usp=sharing
