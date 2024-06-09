# Submission Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut.

### Permasalahan Bisnis

Permasalahan bisnis yang dihadapi adalah tingginya nilai attrition rate perusahaan Jaya Jaya Maju yang mencapai lebih dari 10%. Nilai Attrition Rate ini menunjukkan banyaknya karyawan yang memutuskan resign dibanding karyawan yang memutuskan untuk terus bekerja diperusahaan tersebut. Banyaknya karyawan yang keluar akan menyebabkan alur kerja yang sudah berjalan menjadi tertunda, pekerjaan yang harusnya dikerjakan oleh seseorang malah harus tertunda atau dilimpahkan ke pekerja lain agar pekerjaan tersebut bisa selesai. Pekerja yang mendapat beban kerja tambahan akan menyelesaikan pekerjaannya menjadi sedikit lebih lama sehingga alur kerja dalam perusahaan menjadi melambat.

Untuk mengetahui hal-hal yang menyebabkan tingginya attrition rate, kita perlu mencari tahu terlebih dahulu faktor faktor yang menyebabkan tingginya attrition rate. Faktor faktor ini bisa berasal baik dari dalam perusahaan seperti fasilitas dan bebam kerja yang diberikan kepada karyawan maupun dari karyawan itu sendiri seperti dari mana dia berasal. Faktor-faktor inilah yang kemudian dipantau dan dijaga nilainya agar nilai attrition rate dapat terus ditekan.

### Cakupan Proyek

- Membersihkan dan mengolah data awal
- Menganalisis faktor-faktor yang menyebabkan tingginya Attrition Rate dengan menjawab pertanyaan pada exploratory data analysis dan visualisasi data
- Membuat business dashboard dari faktor-faktor tersebut
- Membuat model machine learning untuk memprediksi status karyawan berdasarkan nilai dari faktor-faktor yang dimasukan

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee (https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv)

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_human_resources
cd proyek_human_resources
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run model_dashboard.py
```

## Business Dashboard

Business dashboard proyek ini dibuat menggunakan Google Looker Studio dengan menambah fitur filter berdasarkan status karyawan yaitu aktif dan inaktif. Pada dashboard ditampilkan jumlah seluruh karyawan, jumlah karyawan yang aktif dan yang keluar, attrition rate, nilai rata-rata gaji karyawan, nilai rata-rata tahun bekerja karyawan di perusahaan, grafik pie chart perbandingan jumlah berdasarkan status dengan gender, status dengan status pernikahan, status dengan kesedian melakukan perjalanan bisnis, dan status dengan bekerja overtime. Selain itu terdapat grafik yang menunjukkan sebaran karyawan berdasarkan usia, departement kerja, bidang pekerjaan, level pekerjaan, jenjang pendidikan, bidang pendidikan yang ditempuh, kategori gaji karyawan, dan persentase kenaikan gaji karyawan. Ada pula rating yang menampilkan rata-rata nilai performa kerja karyawan dan kepuasan karyawan dengan skala 1-5. 

Pada pojok atas terdapat tombol yang mengarahkan ke github repository tempat proyek ini disimpan, serta link menuju dashboard streamlit untuk mengakses dashboard prediksi berdasarkan model machine learning yang sudah dibuat. Model machine learning yang dibuat menerapkan teknik GradientBoostingClassifierakurasi training sebesar 98.4% dan akurasi validation sebesar 86.79% dengan nilai ROC training sebesar 95.6% dan nilai ROC validation sebesar 74.37%. Nilai ROC menunjukkan kemampuan model dalam memprediksi 2 jenis kategori. nilai ROC >70% sudah dapat diterima dalam penggunaan model. Pengguna dashboard prediksi hanya tinggal memasukan parameter yang diminta untuk mengetahui prediksi status karyawan aktif atau inaktif.

Link Looker Studio: https://lookerstudio.google.com/reporting/bfe26f76-2840-4202-bee9-2f7f7f5e6c9d

Link Streamlit: https://submission-pertama--menyelesaikan-permasalahan-human-resources.streamlit.app/

## Conclusion

Berdasarkan bussiness dashboard ini dapat dilihat bahwa
- Kecenderungan karyawan yang keluar memiliki gaji di bawah rata-rata gaji karyawan, nilai persentase kenaikan gaji yang rendah, dan level jabatan yang rendah juga. Rata rata gaji karyawan bernilai 6650 USD sedangkan sebagian besar karyawan memiliki gaji di bawah 5000 USD, sebagian besar karyawan yang cenderung keluar juga berada pada rentang gaji di bawah 5000 USD. Pada grafik status karyawan berbanding persentase karyawan yang rendah dapat dilihat bahwa semakin rendah persentase kenaikan gaji semakin banyak karyawan yang keluar. Rendahnya gaji dan persentase kenaikan gaji jelas dipengaruhi dari level jabatan mereka, sebagian besar karyawan memiliki level jabatan terendah sehingga memiliki gaji dan persentase kenaikan gaji yang rendah juga. 
- Karyawan yang bekerja overtime cenderung keluar. Meskipun sebagian besar karyawan tidak bekerja overtime, karyawan yang keluar paling banyak berasal dari golongan yang bekerja overtime.
- Kebanyakan karyawan yang keluar berada pada rentang umur 25-35 tahun yang merupakan umur produktif dan suka mengeksplorasi hal baru.
- Kualitas kerja dan tingkat kepuasan karyawan berada pada rentang 3,3-3,9. Penilaian terhadap kepuasan lingkungan kerja berada pada nilai terendah yaitu 3.3 sehingga perlu ditingkatkan.

### Rekomendasi Action Items (Optional)

Untuk mengurangi tingkat attrition rate hal hal yang mungkin dapat dilakukan perusahaan adalah sebagai berikut
- Menaikan gaji karyawan dan persentase kenaikan gaji. Peningkatan gaji dan persentase karyawan dalam batas wajar harus dilakukan. Karyawan dengan dapat mendapat kenaikan gaji sebesar 10-20% agar bisa keluar dari nilai rata-rata gaji saat ini. 
- Menambah beberapa kegiatan dan fasilitas lain yang dapat mingkatkan kepuasan karyawan terhadap lingkungan kerja.
- Menerapkan sistem kerja yang lebih efektif dan efisien sehingga jumlah karyawan yang harus bekerja overtime berkurang.Proses penerapan ini dapat dilakukan perlahan melalui sebuah pelatihan masal, pemanfaatan aplikasi seperti kanban board dan lain-lain.
- Dengan adanya business dashboard HRD diharap selalu melakukan update data karyawan secara rutin setiap bulan agar aktivitas-aktivitas yang diadakan tepat sasaran sesuai faktor-faktor yang mempengaruhi attrition rate.
