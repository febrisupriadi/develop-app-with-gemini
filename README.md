# Lab: Develop an App with Gemini

Repositori ini berisi panduan dan dokumentasi untuk menyelesaikan lab "Develop an App with Gemini" di Google Cloud Skills Boost / Qwiklabs.

## Task 1: Configure Environment, Account, and Gemini API

Langkah-langkah berikut digunakan untuk melakukan konfigurasi awal lingkungan Cloud Shell, mengaktifkan API Gemini (Cloud AI Companion), serta memberikan izin akses (IAM Roles) yang diperlukan oleh akun pengguna.

### 1. Inisialisasi Variabel Lingkungan
Jalankan perintah berikut di Cloud Shell untuk menyimpan Project ID, Region, dan Akun Pengguna yang aktif ke dalam variabel:

```bash
PROJECT_ID=\$(gcloud config get-value project)
REGION=us-east4
USER=\$(gcloud config get-value account 2> /dev/null)

echo "PROJECT_ID=\${PROJECT_ID}"
echo "REGION=\${REGION}"
echo "USER=\${USER}"
```

### 2. Mengaktifkan Cloud AI Companion API
Aktifkan API untuk layanan Gemini dengan perintah berikut:

```bash
gcloud services enable cloudaicompanion.googleapis.com --project ${PROJECT_ID}
```

### 3. Konfigurasi IAM Roles (Izin Akses Gemini)
Berikan peran `cloudaicompanion.user` dan `serviceusage.serviceUsageViewer` kepada akun pengguna agar fitur Gemini Code Assist dapat digunakan:

```bash
gcloud projects add-iam-policy-binding \({PROJECT_ID} --member user:\){USER} --role=roles/cloudaicompanion.user
gcloud projects add-iam-policy-binding \({PROJECT_ID} --member user:\){USER} --role=roles/serviceusage.serviceUsageViewer
```

> **Catatan Troubleshoot:** Jika muncul pesan peringatan terkait *Regional Access Boundary* (`Gaia id not found`), pesan tersebut dapat diabaikan karena merupakan perilaku bawaan akun instan Qwiklabs. Izin IAM akan tetap sukses terpasang pada daftar kebijakan proyek.

## Task 2: Create a Cloud Workstations Configuration and Instance

Langkah-langkah ini digunakan untuk membuat klaster workstation, konfigurasi mesin, dan meluncurkan instans Cloud Workstation yang akan terintegrasi dengan Gemini Code Assist.

### 1. Membuat Workstation Cluster
Jalankan perintah berikut di Cloud Shell untuk membuat klaster workstation baru di wilayah yang telah ditentukan:

```bash
gcloud workstations clusters create my-cluster \
    --region=\$REGION \
    --project=\$PROJECT_ID
```
*(Proses pembuatan klaster ini biasanya memakan waktu beberapa menit. Tunggu hingga terminal selesai memproses).*

### 2. Membuat Workstation Configuration
Buat konfigurasi workstation yang menyertakan ekstensi Cloud Code secara bawaan agar fitur Gemini Code Assist langsung siap digunakan:

```bash
gcloud workstations configs create my-config \
    --cluster=my-cluster \
    --region=\$REGION \
    --project=\$PROJECT_ID
```

### 3. Membuat Instans Cloud Workstation
Setelah konfigurasi siap, buat instans workstation utama tempat Anda akan menulis kode aplikasi:

```bash
gcloud workstations create my-workstation \
    --cluster=my-cluster \
    --config=my-config \
    --region=\$REGION \
    --project=\$PROJECT_ID
```

### 4. Meluncurkan Workstation via Google Cloud Console
1. Buka halaman **Cloud Workstations** di Google Cloud Console.
2. Masuk ke menu **Workstations**.
3. Klik nama workstation Anda (`my-workstation`), lalu klik **Start**.
4. Setelah statusnya berubah menjadi *Running*, klik **Launch** untuk membuka IDE berbasis Code OSS (VS Code versi open-source) di tab browser baru.

### 4. Membuat dan Menjalankan Workstation (via Cloud Console)

Jika tidak menggunakan terminal, pembuatan instans workstation dapat dilakukan secara visual melalui antarmuka Google Cloud Console dengan langkah berikut:

1. Pada panel Navigasi kiri di Cloud Console, cari dan klik menu **Workstations**.
2. Klik tombol **Create Workstation** di bagian atas halaman.
3. Isikan nilai properti berikut pada formulir yang tersedia:
   * **ID:** `my-workstation`
   * **Configuration:** Pilih `my-config` (konfigurasi yang telah dibuat sebelumnya)
4. Klik tombol **Create** di bagian bawah.
5. Setelah berhasil dibuat, instans akan muncul di bawah daftar *My workstations* dengan status **Stopped**.
6. Untuk menyalakannya, klik tombol **Start**. Status akan berubah menjadi *Starting*.
7. Tunggu beberapa menit hingga status berubah menjadi **Running**, yang menandakan bahwa lingkungan kerja IDE Anda telah siap digunakan.



