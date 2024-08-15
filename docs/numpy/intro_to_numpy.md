# Introduction to NumPy

## Apa itu NumPy?

NumPy adalah library fundamental untuk scientific computing di Python. NumPy digunakan untuk melakukan operasi matematika pada multi-dimensional array object, beserta objek turunannya seperti masked arrays dan matrix.

NumPy menyediakan fungsi-fungsi yang efisien untuk operasi matematika pada array, seperti operasi linear algebra, operasi statistik, shape manimpulation, sorting, selecting, I/O, dan lainnya.

Core dari Numpy adalah objek `ndarray` yang mengenkapsulasi array n-dimensi dengan elemen-elemen yang seragam, dimana operasi-operasinya dilakukan pada kode yang telah tekompilasi.

Referensi: https://numpy.org/doc/stable/user/whatisnumpy.html#what-is-numpy

## Mengapa menggunakan NumPy?

Python memiliki built-in `list` yang dapat digunakan untuk menyimpan data dalam bentuk array. Namun, `list` tidak efisien untuk melakukan operasi matematika pada data yang besar dan lambat untuk diproses.

Berikut beberapa perbedaan antara Numpy array dengan Python list:

1. Numpy array memiliki ukuran yang tetap, sedangkan Python list memiliki ukuran yang dinamis. Perubahan pada ukuran Numpy array akan menghasilkan array baru dan menghapus array lama.
2. Numpy array memiliki elemen-elemen yang seragam, sehingga ukuran mereka di dalam memori akan tetap sama.
3. Numpy array mendukung operasi matematika pada array ukuran besar secara efisien, sedangkan Python list tidak.
4. Bertambah banyaknya library scientific computing di Python yang menggunakan NumPy sebagai basisnya.

## NumPy Quickstart

Untuk mulai menggunakan NumPy dan mempelajari konsep dasar NumPy, kamu dapat membaca tutorial dari halaman resmi NumPy:

[NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)

Tutorial di atas akan membantu kamu memahami tentang:

1. Perbedaan antara one-, two-, dan n-dimensional arrays di NumPy
2. Bagaimana cara menggunakan operasi-operasi aljabar linear untuk n-dimensional arrays tanpa menggunakan for-loops
3. Memaham properti `axis` dan `shape` dari n-dimensional arrays

---

Selain itu, kamu juga bisa membaca tutorial NumPy di beberapa situs berikut:

1. [Scientific Computing in Python: Introduction to NumPy and Matplotlib](https://sebastianraschka.com/blog/2020/numpy-intro.html)

## NumPy Fundamentals

Dokumen-dokumen dari situs resmi NumPy di bawah ini akan membantu kamu untuk lebih memahami konsep, design decisions, dan technical constrains dari NumPy.

- [Array creation](https://numpy.org/doc/stable/user/basics.creation.html)
- [Indexing on ndarrays](https://numpy.org/doc/stable/user/basics.indexing.html)
- [I/O with NumPy](https://numpy.org/doc/stable/user/basics.io.html)
- [Data types](https://numpy.org/doc/stable/user/basics.types.html)
- [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [Copies and views](https://numpy.org/doc/stable/user/basics.copies.html)
- [Working with Arrays of Strings And Bytes](https://numpy.org/doc/stable/user/basics.strings.html)
- [Structured arrays](https://numpy.org/doc/stable/user/basics.rec.html)
- [Universal functions (ufunc) basics](https://numpy.org/doc/stable/user/basics.ufuncs.html)
