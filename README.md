https://storehousepbp.adaptable.app/

1.
>Membuat sebuah proyek Django baru.<br>

Pertama buat direktori dengan nama aplikasi yang dibuat (storehousepbp) terus kalau sudah di inisiasi dengan menjalankan `git init` di cmd yang ada di direktori ini lalu buatlah virtual environment dengan menjalankan `py -m venv env` lalu aktifkan virtual environment tersebut dengan `env\Scripts\activate.bat` untuk di Windows.
Di direktori yang sama buatlah file dengan nama `requirements.txt` lalu tambahkan beberapa dependencies yang diperlukan untuk membuat projek django seperti django, gunicorn dan lain lain. lalu pasang dependencies tersebut dengan menjalankan perintah ini di virtual environment yang tadi sudah di aktifkan `pip install -r requirements.txt`.
Buatlah projek django dengan menjalankan `django-admin startproject storehousepbp .`. nama aplikasi nya sesuai yang ingin dibuat.<br><br>
>Membuat aplikasi dengan nama main pada proyek tersebut.<br>

Untuk membuat aplikasi dengan nama `main` jalankan perintah `py manage.py startapp main`.
Lalu masuk ke `settings.py` di direktori storehousepbp (aplikasi yang dibuat) lalu di bagian `INSTALLED_APPS` tambahkan 'main' ke dalam aplikasi.
>Melakukan routing pada proyek agar dapat menjalankan aplikasi main.<br>

Buatlah file bernama `urls.py` di direktori main lalu isi dengan kode :<br>
`from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]`<br>
Kemudian, masuk ke `urls.py` yang ada di direktori storehousepbp (aplikasi yang dibuat) kemudian tambahkan beberapa kode seperti :<br>
`from django.urls import path, include` hanya ditambahkan impor include dan <br>
`    path('main/', include('main.urls')),` ditambahkan di dalam urlspatterns <br>
>Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib.<br>



2.<br>![image](https://github.com/humama/storehousepbp/assets/20278539/bef151e5-9d7d-4fcd-ac9e-ab53b90ee6e5)<br>
Kaitan antara urls.py, views.py, models.py, dan berkas HTML adalah dasar dari kerangka kerja Django dalam mengembangkan aplikasi web. Setiap bagian memiliki peran dan tanggung jawabnya sendiri dalam proses pengembangan aplikasi. Berikut adalah penjelasan kaitan masing-masing komponen:

models.py: Berkas ini berisi definisi model-data yang digunakan oleh aplikasi Anda. Model adalah abstraksi dari entitas yang akan disimpan dalam database. Kaitan utama antara models.py dan komponen lainnya adalah:<br>
* Kaitan dengan views.py: Model digunakan oleh view untuk mengambil data dari database, memprosesnya, dan mengirimkannya ke template. View dapat menggunakan query database Django (ORM) untuk berinteraksi dengan model dan mendapatkan data yang diperlukan.<br>
views.py: Berkas ini berisi logika aplikasi web Anda, termasuk tindakan yang diambil saat pengguna mengunjungi URL tertentu. Kaitan antara views.py dan komponen lainnya adalah:<br>
* Kaitan dengan urls.py: View dihubungkan dengan URL melalui berkas urls.py. Anda mendefinisikan path URL yang mengarahkan ke view tertentu. Ketika pengguna mengakses URL tersebut, view yang sesuai akan dijalankan.<br>
* Kaitan dengan models.py: View sering digunakan untuk mengambil data dari model (database) menggunakan Django ORM. View dapat mengambil, memproses, dan mengirimkan data dari model ke template HTML.<br>
* Kaitan dengan berkas HTML: View juga bertanggung jawab untuk merender (mengisi) template HTML dengan data yang diperlukan. View menggunakan template tag Django untuk memasukkan data dari model ke dalam HTML sehingga data tersebut dapat ditampilkan kepada pengguna.

urls.py: Berkas ini berisi konfigurasi URL untuk aplikasi Anda. Ini menghubungkan URL dengan view yang sesuai. Kaitan antara urls.py dan komponen lainnya adalah:<br>
* Kaitan dengan views.py: Dalam urls.py, Anda mendefinisikan path URL yang mengarahkan ke view tertentu. Ini berarti URL tertentu akan mengeksekusi view yang sesuai saat diakses oleh pengguna.

Berkas HTML (Template): Template HTML digunakan untuk merender tampilan yang akan ditampilkan kepada pengguna. Kaitan antara berkas HTML dan komponen lainnya adalah:<br>
* Kaitan dengan views.py: View menggunakan template untuk merender tampilan. View mengirimkan data dari model ke template agar data tersebut dapat ditampilkan dalam HTML.

Dalam alur kerja tipikal Django, pengguna mengakses URL yang didefinisikan dalam urls.py. URL tersebut mengarahkan ke view yang sesuai dalam views.py. View menggunakan model-data dari models.py untuk mengambil atau memproses data. Kemudian, view merender template HTML yang menggabungkan data dari model dengan tampilan HTML yang sesuai. Hasil akhirnya adalah halaman web yang ditampilkan kepada pengguna.

Ini adalah inti dari pola desain Model-View-Controller (MVC) yang diadopsi oleh Django. Dalam pola ini, models.py berperan sebagai Model, views.py sebagai Controller, dan berkas HTML sebagai View. Django menggunakan pendekatan yang lebih dekat dengan Model-View-Template (MVT), di mana template berperan sebagai View, tetapi konsep dasarnya tetap sama.<br>

3. Berikut adalah beberapa alasan mengapa kita menggunakan virtual environment:

* Isolasi Proyek: Virtual environment memungkinkan kita untuk mengisolasi dependensi proyek tertentu dari lingkungan Python global. Ini berarti kita dapat memiliki versi yang berbeda dari paket Python di setiap proyek tanpa khawatir tentang konflik dependensi. Ini membantu mencegah masalah yang mungkin timbul ketika dua proyek menggunakan versi paket Python yang berbeda.<br>
* Mengelola Dependensi: Dengan venv, kita dapat dengan mudah menginstal, menghapus, dan mengelola paket Python yang dibutuhkan oleh proyek kita. Ini membuat pengelolaan dependensi proyek menjadi lebih teratur.<br>
* Memudahkan Deploy: Ketika kita ingin mengirimkan proyek ke server produksi, kita dapat dengan mudah meng-eksport daftar dependensi yang diperlukan dengan menggunakan requirements.txt, sehingga server produksi dapat menginstal paket-paket yang diperlukan.<br>
Isolasi Kesalahan: Jika ada masalah atau kesalahan dalam salah satu proyek, itu tidak akan mempengaruhi proyek lain yang ada di lingkungan yang sama.

Django Tanpa Virtual Environment

Meskipun kita dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, disarankan untuk selalu menggunakan virtual environment dalam pengembangan Django. Tanpa virtual environment, kita dapat mengalami masalah berikut:

* Konflik Dependensi: Proyek Django satu dapat menggunakan versi paket tertentu, sementara proyek lain menggunakan versi yang berbeda. Ini dapat menyebabkan konflik dependensi dan masalah yang sulit dilacak.<br>
* Kesulitan Manajemen Paket: Tanpa virtual environment, manajemen paket Python menjadi lebih sulit. kita harus berhati-hati dalam menginstal dan menghapus paket agar tidak mempengaruhi sistem Python global.<br>
* Ketergantungan pada Lingkungan Global: Penggunaan paket Python dari sistem global dapat membuat proyek kita bergantung pada versi paket yang ada di lingkungan tersebut, yang mungkin tidak selalu sesuai dengan kebutuhan proyek kita.<br>

4. MVC, MVT, dan MVVM

MVC (Model-View-Controller):

* Model: Bertanggung jawab atas struktur data dan logika bisnis. Ini berinteraksi dengan database.<br>
* View: Menampilkan data kepada pengguna dan menerima input dari pengguna. Ini mengirim permintaan ke Controller.<br>
* Controller: Menerima permintaan dari View, memprosesnya, dan mengirimkan instruksi kepada Model untuk memperbarui data atau mengambil data baru.

MVT (Model-View-Template):

* Model: Sama dengan dalam MVC, mengelola data dan logika bisnis.<br>
* View: Mirip dengan View dalam MVC, bertanggung jawab untuk menampilkan data kepada pengguna dan menerima input.<br>
* Template: Template dalam MVT mirip dengan bagian Controller dalam MVC tradisional, karena mengatur logika presentasi.

MVVM (Model-View-ViewModel):

* Model: Sama dengan dalam MVC dan MVT, mengelola data dan logika bisnis.<br>
* View: Mirip dengan View dalam MVC dan MVT, bertanggung jawab untuk menampilkan data kepada pengguna.<br>
* ViewModel: Bertindak sebagai perantara antara Model dan View. Ini memungkinkan View untuk berinteraksi dengan Model tanpa perlu tahu tentang Model secara langsung.

Perbedaan utama antara ketiganya adalah bagaimana mereka mengatur logika aplikasi dan tampilan. Django menggunakan pendekatan MVT, di mana Template mirip dengan Controller dalam pendekatan MVC tradisional. Django secara otomatis mengelola aliran permintaan HTTP, sehingga developer lebih fokus pada logika aplikasi dan tampilan.
