https://storehousepbp.adaptable.app/

1.

2.

3. Berikut adalah beberapa alasan mengapa kita menggunakan virtual environment:

--* Isolasi Proyek: Virtual environment memungkinkan kita untuk mengisolasi dependensi proyek tertentu dari lingkungan Python global. Ini berarti kita dapat memiliki versi yang berbeda dari paket Python di setiap proyek tanpa khawatir tentang konflik dependensi. Ini membantu mencegah masalah yang mungkin timbul ketika dua proyek menggunakan versi paket Python yang berbeda.<br>
Mengelola Dependensi: Dengan venv, kita dapat dengan mudah menginstal, menghapus, dan mengelola paket Python yang dibutuhkan oleh proyek kita. Ini membuat pengelolaan dependensi proyek menjadi lebih teratur.<br>
Memudahkan Deploy: Ketika kita ingin mengirimkan proyek ke server produksi, kita dapat dengan mudah meng-eksport daftar dependensi yang diperlukan dengan menggunakan requirements.txt, sehingga server produksi dapat menginstal paket-paket yang diperlukan.<br>
Isolasi Kesalahan: Jika ada masalah atau kesalahan dalam salah satu proyek, itu tidak akan mempengaruhi proyek lain yang ada di lingkungan yang sama.

Django Tanpa Virtual Environment

Meskipun kita dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, disarankan untuk selalu menggunakan virtual environment dalam pengembangan Django. Tanpa virtual environment, kita dapat mengalami masalah berikut:

--* Konflik Dependensi: Proyek Django satu dapat menggunakan versi paket tertentu, sementara proyek lain menggunakan versi yang berbeda. Ini dapat menyebabkan konflik dependensi dan masalah yang sulit dilacak.<br>
Kesulitan Manajemen Paket: Tanpa virtual environment, manajemen paket Python menjadi lebih sulit. kita harus berhati-hati dalam menginstal dan menghapus paket agar tidak mempengaruhi sistem Python global.<br>
Ketergantungan pada Lingkungan Global: Penggunaan paket Python dari sistem global dapat membuat proyek kita bergantung pada versi paket yang ada di lingkungan tersebut, yang mungkin tidak selalu sesuai dengan kebutuhan proyek kita.

4. MVC, MVT, dan MVVM

MVC (Model-View-Controller):

--* Model: Bertanggung jawab atas struktur data dan logika bisnis. Ini berinteraksi dengan database.<br>
View: Menampilkan data kepada pengguna dan menerima input dari pengguna. Ini mengirim permintaan ke Controller.<br>
Controller: Menerima permintaan dari View, memprosesnya, dan mengirimkan instruksi kepada Model untuk memperbarui data atau mengambil data baru.

MVT (Model-View-Template):

--* Model: Sama dengan dalam MVC, mengelola data dan logika bisnis.<br>
View: Mirip dengan View dalam MVC, bertanggung jawab untuk menampilkan data kepada pengguna dan menerima input.<br>
Template: Template dalam MVT mirip dengan bagian Controller dalam MVC tradisional, karena mengatur logika presentasi.

MVVM (Model-View-ViewModel):

--* Model: Sama dengan dalam MVC dan MVT, mengelola data dan logika bisnis.<br>
View: Mirip dengan View dalam MVC dan MVT, bertanggung jawab untuk menampilkan data kepada pengguna.<br>
ViewModel: Bertindak sebagai perantara antara Model dan View. Ini memungkinkan View untuk berinteraksi dengan Model tanpa perlu tahu tentang Model secara langsung.

Perbedaan utama antara ketiganya adalah bagaimana mereka mengatur logika aplikasi dan tampilan. Django menggunakan pendekatan MVT, di mana Template mirip dengan Controller dalam pendekatan MVC tradisional. Django secara otomatis mengelola aliran permintaan HTTP, sehingga developer lebih fokus pada logika aplikasi dan tampilan.
