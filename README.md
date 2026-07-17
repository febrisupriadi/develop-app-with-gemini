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


## Task 3: Sign In to Cloud Code and Enable Gemini

Langkah-langkah ini digunakan untuk menghubungkan IDE Cloud Workstations dengan akun Google Cloud Anda dan mengaktifkan panel interaksi AI Gemini Code Assist.

### 1. Masuk (Sign In) ke Google Cloud via IDE
1. Setelah IDE Cloud Workstations terbuka, perhatikan bilah status (*status bar*) di pojok kiri bawah jendela editor.
2. Klik tombol bertuliskan **Cloud Code - Sign In**.
3. Ikuti instruksi popup yang muncul untuk membuka halaman otorisasi browser Anda.
4. Salin kode otorisasi yang diberikan, masukkan kembali ke dalam kotak input di IDE, lalu tekan **Enter**.

### 2. Membuka Panel Chat Gemini
1. Di bilah aktivitas (*activity bar*) sebelah kiri editor, klik ikon **Cloud Code** (logo berbentuk susunan kotak biru).
2. Di dalam panel Cloud Code yang terbuka, cari dan klik menu **Gemini Code Assist Chat**.
3. Sesi chat siap digunakan untuk membantu pembuatan kode aplikasi Python Flask Anda.

---

## Task 4: Chat with Gemini

Langkah ini digunakan untuk menguji fungsionalitas asisten AI Gemini Code Assist dengan memberikan pertanyaan kontekstual mengenai layanan Google Cloud sebelum mulai membuat aplikasi.

### Langkah-langkah Pengujian:
1. Buka panel **Gemini Code Assist Chat** di sisi kiri IDE Anda.
2. Di kolom teks input chat, ajukan pertanyaan mengenai opsi deployment aplikasi:
   ```text
   What are the Google Cloud services available to deploy a web application?
   ```
3. Ajukan pertanyaan lanjutan yang lebih spesifik untuk menentukan layanan terbaik untuk aplikasi kontainer sederhana:
   ```text
   What is the best Google Cloud service to deploy a simple containerized application?
   ```
   *Gemini akan merekomendasikan **Cloud Run** karena sifatnya yang serverless dan berbasis kontainer.*

---

## Task 5 & 6: Develop and Enhance the Python Flask App

Langkah ini menggunakan Gemini Code Assist untuk membuat kerangka dasar aplikasi web berbasis Python Flask yang mengelola data inventaris, serta melakukan pengujian emulator secara lokal.

### 1. Membuat Database Inventaris (`inventory.py`)
Buat file baru di ruang kerja (*workspace*) IDE Anda dengan nama `inventory.py`, lalu masukkan data contoh berikut:
```python
inventory = [
    {"productid": "12345", "onhandqty": "100"},
    {"productid": "67890", "onhandqty": "50"},
    {"productid": "11122", "onhandqty": "25"}
]
```

### 2. Membangun Logika Utama Server (`app.py`)
Buka file `app.py`, hapus seluruh kode bawaan, dan ganti dengan kode final Flask yang telah mengekspos endpoint API `/inventory` dan `/inventory/<productid>` berikut:
```python
import os
from flask import Flask, render_template, jsonify
from inventory import inventory

app = Flask(__name__)

# Endpoint untuk menampilkan seluruh daftar inventaris
@app.route('/inventory', methods=['GET'])
def inventory_list():
    return jsonify(inventory)

# Endpoint untuk menampilkan data inventaris berdasarkan Product ID
@app.route('/inventory/<productid>', methods=['GET'])
def inventory_item(productid):
    for item in inventory:
        if item['productid'] == productid:
            return jsonify(item)
    return jsonify({'error': 'Product not found'}), 404

# Endpoint utama aplikasi web
@app.route('/')
def hello():
    message = "It's running!"
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')
    return render_template('index.html', message=message, Service=service, Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
```

### 3. Menjalankan Aplikasi di Emulator Lokal
1. Di bilah aktivitas sebelah kiri IDE, klik ikon **Cloud Code** > **Cloud Run**.
2. Klik tombol **Run App on Local Cloud Run Emulator**, lalu klik **Run**.
3. Jika muncul perintah popup di bagian atas layar untuk mengaktifkan komponen tambahan, pilih **Yes** pada opsi *Enable minikube gcp-auth addon*.
4. Uji endpoint lokal di browser Anda dengan mengakses:
   * `http://localhost:8080/inventory`
   * `http://localhost:8080/inventory/12345`

---

## Task 7: Deploy the App to Google Cloud Run (Production)

Langkah akhir untuk mempublikasikan aplikasi Flask dari lingkungan pengembangan lokal ke infrastruktur serverless Google Cloud Run.

### ⚠️ Catatan Troubleshoot (Penting):
Jika deployment via GUI Cloud Code gagal karena error `authentication failed` ke `gcr.io`, hal ini disebabkan oleh masalah izin token Docker di Workstation lokal. Masalah ini diselesaikan dengan menggunakan metode **Remote Cloud Build** langsung dari terminal workstation ke server Google.

### Langkah Deployment Jarak Jauh via Terminal Workstation:
1. Jalankan perintah ini di Terminal IDE untuk mengirimkan source code dan mengompilasinya langsung di Google Cloud Build (Ganti nomor proyek sesuai akun Anda):
   ```bash
   gcloud builds submit --tag gcr.io/qwiklabs-gcp-03-b4059ddc671e/hello-world-1:latest --project=qwiklabs-gcp-03-b4059ddc671e
   ```
2. Setelah berstatus `SUCCESS`, jalankan perintah berikut untuk merilis kontainer tersebut ke internet melalui Cloud Run:
   ```bash
   gcloud run deploy hello-world-1 \
     --image gcr.io/qwiklabs-gcp-03-b4059ddc671e/hello-world-1:latest \
     --region us-east4 \
     --allow-unauthenticated \
     --platform managed \
     --project=qwiklabs-gcp-03-b4059ddc671e
   ```

### 4. Validasi Live URL Publik
Setelah proses deploy memunculkan alamat web `.run.app` resmi, lakukan pemicuan traffic masuk (*HTTP GET Request*) dengan membuka URL publik berikut di browser:
* `https://<URL-Cloud-Run-Anda>/inventory`
* `https://<URL-Cloud-Run-Anda>/inventory/12345`

Pemicuan traffic pada live URL ini akan mengaktifkan sistem penilaian otomatis Qwiklabs untuk memberikan centang hijau.

---
**Status Akhir Lab:** Selesai 100% (100/100 Points) 🚀

