# Operators

Operator digunakan untuk melakukan operasi pada variabel dan nilai.

```{contents}
:local:
```

## Assignment Operators

Assignment operator digunakan untuk memberikan nilai pada variabel.

| Operator | Contoh         | Sama Dengan       |
| -------- | -------------- | ----------------- |
| `=`      | `x = 5`        | `x = 5`           |
| `+=`     | `x += 3`       | `x = x + 3`       |
| `-=`     | `x -= 3`       | `x = x - 3`       |
| `*=`     | `x *= 3`       | `x = x * 3`       |
| `/=`     | `x /= 3`       | `x = x / 3`       |
| `%=`     | `x %= 3`       | `x = x % 3`       |
| `//=`    | `x //= 3`      | `x = x // 3`      |
| `**=`    | `x **= 3`      | `x = x ** 3`      |
| `&=`     | `x &= 3`       | `x = x & 3`       |
| `\|=`    | `x \|= 3`      | `x = x \| 3`      |
| `^=`     | `x ^= 3`       | `x = x ^ 3`       |
| `>>=`    | `x >>= 3`      | `x = x >> 3`      |
| `<<=`    | `x <<= 3`      | `x = x << 3`      |
| `:=`     | `print(x := 3` | `x = 3; print(x)` |

## Arithmetic Operators

Arithmetic operator digunakan untuk melakukan operasi matematika pada variabel.

| Operator | Nama                            | Contoh   |
| -------- | ------------------------------- | -------- |
| `+`      | Penjumlahan                     | `x + y`  |
| `-`      | Pengurangan                     | `x - y`  |
| `*`      | Perkalian                       | `x * y`  |
| `/`      | Pembagian                       | `x / y`  |
| `%`      | Modulus                         | `x % y`  |
| `//`     | Pembagian (pembulatan ke bawah) | `x // y` |
| `**`     | Eksponensial (pangkat)          | `x ** y` |

## Comparison Operators

Comparison operator digunakan untuk membandingkan dua nilai.

| Operator | Nama                    | Contoh   |
| -------- | ----------------------- | -------- |
| `==`     | Sama dengan             | `x == y` |
| `!=`     | Tidak sama dengan       | `x != y` |
| `>`      | Lebih besar dari        | `x > y`  |
| `<`      | Lebih kecil dari        | `x < y`  |
| `>=`     | Lebih besar sama dengan | `x >= y` |
| `<=`     | Lebih kecil sama dengan | `x <= y` |

## Logical Operators

Logical operator digunakan untuk menggabungkan pernyataan bersyarat.

| Operator | Deskripsi                                             | Contoh                  |
| -------- | ----------------------------------------------------- | ----------------------- |
| `and`    | Mengembalikan `True` jika kedua pernyataan benar      | `x < 5 and  x < 10`     |
| `or`     | Mengembalikan `True` jika salah satu pernyataan benar | `x < 5 or x < 4`        |
| `not`    | Mengembalikan `True` jika pernyataan tidak benar      | `not(x < 5 and x < 10)` |

## Identity Operators

Identity operator digunakan untuk membandingkan objek, bukan nilai.

| Operator | Deskripsi                                                       | Contoh       |
| -------- | --------------------------------------------------------------- | ------------ |
| `is`     | Mengembalikan `True` jika kedua variabel adalah objek yang sama | `x is y`     |
| `is not` | Mengembalikan `True` jika kedua variabel bukan objek yang sama  | `x is not y` |

## Membership Operators

Membership operator digunakan untuk memeriksa apakah elemen berada dalam objek.

| Operator | Deskripsi                                                         | Contoh       |
| -------- | ----------------------------------------------------------------- | ------------ |
| `in`     | Mengembalikan `True` jika nilai tertentu berada dalam objek       | `x in y`     |
| `not in` | Mengembalikan `True` jika nilai tertentu tidak berada dalam objek | `x not in y` |

## Bitwise Operators

Bitwise operator digunakan untuk melakukan operasi pada bit.

| Operator | Nama        | Deskripsi                                        | Contoh   |
| -------- | ----------- | ------------------------------------------------ | -------- |
| `&`      | AND         | Set bit ke 1 jika kedua bit adalah 1             | `x & y`  |
| `\|`     | OR          | Set bit ke 1 jika salah satu bit adalah 1        | `x \| y` |
| `^`      | XOR         | Set bit ke 1 jika hanya satu bit yang bernilai 1 | `x ^ y`  |
| `~`      | NOT         | Invert semua bit                                 | `~x`     |
| `<<`     | Left Shift  | Geser bit ke kiri sebanyak n posisi              | `x << y` |
| `>>`     | Right Shift | Geser bit ke kanan sebanyak n posisi             | `x >> y` |

## Operator Precedence

Operator precedence menentukan urutan operasi yang dieksekusi dalam ekspresi.

| Operator                            | Description                                           |
| ----------------------------------- | ----------------------------------------------------- |
| ()                                  | Parentheses                                           |
| \*\*                                | Exponentiation                                        |
| +x -x ~x                            | Unary plus, unary minus, and bitwise NOT              |
| \* / // %                           | Multiplication, division, floor division, and modulus |
| + -                                 | Addition and subtraction                              |
| << >>                               | Bitwise left and right shifts                         |
| &                                   | Bitwise AND                                           |
| ^                                   | Bitwise XOR                                           |
| \|                                  | Bitwise OR                                            |
| == != > >= < <= is is not in not in | Comparisons, identity, and membership operators       |
| not                                 | Logical NOT                                           |
| and                                 | AND                                                   |
| or                                  | O                                                     |
