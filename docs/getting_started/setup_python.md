# Setup Python

Pada bagian ini, kamu akan belajar bagaimana cara menginstall Python di komputer kamu.

Klik salah satu tab di bawah ini sesuai dengan sistem operasi yang kamu gunakan untuk melihat langkah-langkahnya.

`````{tab-set}
````{tab-item} Windows
## Instalasi Python di Windows

### 1. Download Installer Python

[Buka situs resmi Python](https://www.python.org/downloads/). Di halaman download, cari bagian Windows installers dan pilih versi Python terbaru.

### 2. Jalankan File Installer

Setelah proses download selesai, double-click pada file installer Python yang sudah kamu unduh.

### 3. Ikuti Proses Instalasi

Jendela instalasi Python akan muncul. Pada tahap ini, pastikan kamu memilih opsi Install Now. Opsi ini akan menginstall Python dengan pengaturan default yang direkomendasikan.

PENTING: Selama proses instalasi, pastikan kamu mencentang pilihan "Add Python 3.x to PATH". Ini akan menambahkan direktori instalasi Python ke environment variable sehingga kamu bisa menjalankan perintah Python dari Command Prompt dengan mudah.

Klik tombol "Install Now" dan tunggu hingga proses instalasi selesai.

## Verifikasi Instalasi Python di Windows

Setelah proses instalasi selesai, saatnya untuk memastikan Python sudah terinstall dengan benar. Buka aplikasi Command Prompt (bisa kamu cari melalui menu Start).

Pada jendela Command Prompt, jalankan perintah berikut:

```{code-block} bash
python --version
```

Jika instalasi Python berjalan lancar, Command Prompt akan menampilkan informasi versi Python yang terinstall.
````

````{tab-item} Linux
## Instalasi Python di Linux

Cara install Python di Linux sedikit berbeda jika di bandingkan dengan Windows dan MacOS. Karena biasanya dilakukan melalui package manager bawaan dari distro Linux yang digunakan.

Perintah dan langkah-langkah instalasi bisa berbeda-beda tergantung pada distro Linux yang kamu gunakan. Sebagai contoh, panduan berikut ini akan menggunakan perintah untuk Debian-based distro.

### 1. Update Package List
Buka aplikasi Terminal lalu pada jendela Terminal, masukkan perintah berikut untuk update package list:

```{code-block} bash
sudo apt update
```

Masukkan password administrator kamu jika diminta.

### 2. Instalasi Python Menggunakan Package Manager

Untuk meng-install Python 3, kamu bisa menggunakan perintah berikut ini:

```{code-block} bash
sudo apt install python3
```

Perintah ini akan menginstall Python 3 beserta beberapa paket bawaan yang di perlukan.

## Verifikasi Instalasi Python di Linux
Pada jendela Terminal, lalu ketikkan perintah berikut ini:

```{code-block} bash
python --version
```

Jika sudah maka kamu bisa Tekan Enter. Apabila instalasi Python berjalan lancar, maka Terminal akan menampilkan informasi versi Python yang terinstall tersebut.
````

````{tab-item} macOS
## Instalasi Python di macOS

### 1. Download Installer Python

[Buka situs resmi Python](https://www.python.org/downloads/). Di halaman download, cari bagian macOS installers dan pilih versi Python terbaru.

### 2. Install Python Menggunakan Package Installer

Setelah file installer Python ter-download, double-click pada file tersebut. Ikuti perintah instalasi yang muncul pada layar. Umumnya, proses instalasi di macOS cukup mudah dan intuitif.

## Verifikasi Instalasi Python di macOS

Buka aplikasi Terminal (bisa kamu cari melalui Spotlight). Pada jendela Terminal, lalu ketikkan perintah berikut, yaitu:

```{code-block} bash
python --version
```

Jika instalasi Python berjalan lancar, Terminal akan menampilkan informasi versi Python yang terinstall.
````
`````
