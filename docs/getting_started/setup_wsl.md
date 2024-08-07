# Setup WSL (Optional)

Windows Subsystem for Linux (WSL) adalah fitur Windows yang memungkinkan kamu menjalankan lingkungan Linux di komputer Windows kamu, tanpa perlu virtual machine terpisah atau dual-boot. WSL dirancang untuk memberikan pengalaman yang mulus dan produktif bagi pengembang yang ingin menggunakan Windows dan Linux secara bersamaan.

Untuk menginstall WSL, kamu bisa membaca [dokumentasi resmi](https://learn.microsoft.com/en-us/windows/wsl/install).

**Mengapa kamu perlu WSL untuk pemrograman Python?**

Beberapa alasan mengapa kamu perlu WSL:

1. Environment yang konsisten: WSL memungkinkan kamu untuk menjalankan aplikasi Python di lingkungan Linux yang konsisten. Hal ini memungkinkan kamu untuk menghindari masalah dependensi yang mungkin terjadi di Windows. WSL juga memungkinkan kamu untuk mengembangkan dalam environment yang sama persis dengan yang digunakan di production server, yang biasanya berbasis Linux. Hal ini dapat mengurangi masalah yang disebabkan oleh perbedaan environment antara development dan production.
2. Command Line Interface (CLI): WSL memungkinkan kamu untuk menggunakan CLI Linux di Windows. CLI Linux lebih familiar bagi programmer Python karena banyak tools Python yang lebih mudah dijalankan di Linux.
3. Dukungan Package Manager: Package management di Linux seperti `apt` membuatnya lebih mudah untuk menginstal dan mengelola dependensi serta tools dibandingkan dengan beberapa alat manajemen paket di Windows.
