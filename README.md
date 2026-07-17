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

