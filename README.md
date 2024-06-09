# Submission Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut.

### Permasalahan Bisnis

- Apa saja faktor faktor yang menyebabkan tingginya Attrition Rate
- Membuat dashboard yang memonitori faktor tersebut.

### Cakupan Proyek

- Membersihkan dan mengolah data awal
- Menganalisis faktor-faktor yang menyebabkan tingginya Attrition Rate dengan menjawab pertanyaan pada exploratory data analysis dan visualisasi data
- Membuat business dashboard dari faktor-faktor tersebut
- Membuat model machine learning untuk memprediksi status karyawan berdasarkan nilai dari faktor-faktor yang dimasukan

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment: 
conda create --name main-ds python=3.11

conda activate main-ds

pip install streamlit==1.28.1 pandas==2.1.1 numpy==1.24.3 seaborn==0.13.1 plotly==5.15.0 squarify==0.4.3 scikit-learn==1.5.0 joblib==1.4.2 category_encoders==1.3.0

```

```

## Business Dashboard

Business dashboard proyek ini dibuat menggunakan Google Looker Studio dengan menambah fitur filter berdasarkan status karyawan yaitu aktif dan inaktif. Pada dashboard ditampilkan jumlah seluruh karyawan, jumlah karyawan yang aktif dan yang keluar, attrition rate, nilai rata-rata gaji karyawan, nilai rata-rata tahun bekerja karyawan di perusahaan, grafik pie chart perbandingan jumlah berdasarkan status dengan gender, status dengan status pernikahan, status dengan kesedian melakukan perjalanan bisnis, dan status dengan bekerja overtime. Selain itu terdapat grafik yang menunjukkan sebaran karyawan berdasarkan usia, departement kerja, bidang pekerjaan, level pekerjaan, jenjang pendidikan, bidang pendidikan yang ditempuh, kategori gaji karyawan, dan persentase kenaikan gaji karyawan. Ada pula rating yang menampilkan rata-rata nilai performa kerja karyawan dan kepuasan karyawan dengan skala 1-5. 

Pada pojok atas terdapat tombol yang mengarahkan ke github repository tempat proyek ini disimpan, serta link menuju dashboard streamlit untuk mengakses dashboard prediksi berdasarkan model machine learning yang sudah dibuat. Model machine learning yang dibuat menerapkan teknik GradientBoostingClassifierakurasi training sebesar 98.4% dan akurasi validation sebesar 86.79% dengan nilai ROC training sebesar 95.6% dan nilai ROC validation sebesar 74.37%. Nilai ROC menunjukkan kemampuan model dalam memprediksi 2 jenis kategori. nilai ROC >70% sudah dapat diterima dalam penggunaan model. Pengguna dashboard prediksi hanya tinggal memasukan parameter yang diminta untuk mengetahui prediksi status karyawan aktif atau inaktif.

Link Looker Studio: https://lookerstudio.google.com/reporting/bfe26f76-2840-4202-bee9-2f7f7f5e6c9d

Link Streamlit: https://submission-pertama--menyelesaikan-permasalahan-human-resources.streamlit.app/

## Conclusion

Berdasarkan bussiness dashboard ini dapat dilihat bahwa
- Kecenderungan karyawan yang keluar memiliki gaji di bawah rata-rata gaji karyawan, nilai persentase kenaikan gaji yang rendah, dan level jabatan yang rendah juga.
- Karyawan yang bekerja overtime cenderung keluar.
- Umur karyawan yang keluar berada pada rentang umur produktif
- Nilai kepuasan karyawan berada pada rentang 3.3-3.9.

### Rekomendasi Action Items (Optional)

Untuk mengurangi tingkat attrition rate hal hal yang mungkin dapat dilakukan perusahaan adalah sebagai berikut
- Menaikan gaji karyawan dan persentase kenaikan gaji 
- Menambah beberapa kegiatan dan fasilitas lain yang dapat mingkatkan kepuasan karyawan.
- Menerapkan sistem kerja yang lebih efektif dan efisien sehingga jumlah karyawan yang harus bekerja overtime berkurang.
