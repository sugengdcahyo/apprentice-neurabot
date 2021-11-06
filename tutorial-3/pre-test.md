# 1. Case

## 1.1. make a pattern like the one below with the programming language you are good at.

```
input: 5
*
**
***
****
*****

    *
   **
  ***
 ****
*****

*****
****
***
**
*

*****
 ****
  ***
   **
    *

    *
   ***
  *****
 ******* 
*********

    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
```

## 1.2. Palindrom case

```
words: Kasur ini rusak
>>True

words: Aku adalah manusia
>>False

words: Kasur Koh Ahok rusak
>>True

words: Ria Irawan nawari air
>>True

words: kucing berlari
>>False
```

## 1.3. Encrypt/Decrypt


pra-syarat untuk bisa mengerjakan:
* list dan string method

### 1.3.1. a. Enkripsi dengan metode Caesar:
Metode merupakan metode yang paling sederhana dalam melakukan enkripsi. Teknik ini hanya melakukan pemetaan suatu karakter huruf (angka dan karakter spesial tidak termasuk) dengan metode pergeseran karakter. contoh

| huruf | shift 2 | shift 3 | shift 4 | shift -2 |
|-------|---------|---------|---------|----------|
| a     | c       | d       | e       | y        |
| A     | C       | D       | E       | Y        |
| c     | e       | f       | g       | a        |
| z     | b       | c       | d       | x        |
| %     | %       | %       | %       | %        |
| _     | _       | _       | _       | _        |
| 5     | 5       | 5       | 5       | 5        |

ketentuan:
* pergeseran satu huruf setelah `z` adalah `a`.
* Jika input karakter merupakan huruf kapital maka output juga kapital, begitu juga dengan huruf kecil/non-kapital.
* semua yang bukan huruf tidak berubah, jadi kalau ada suatu angka maka karakter enkripsinya tetap angka tersebut, begitu juga dengan semua karater spesial termasuk spasi.

Maka, untuk mendeskripsikan (decript) sama dengan menggeser ke arah sebaliknya.

Buatlah fungsi `caesar_encript`, dengan argumen `txt` (string) dan `shift` (intiger) seperti dibawah ini. Yang melakukan peng-ekripsian menggunakan metode Caesar terhadap string `txt`. Keluaran dari fungsi ini berupa string terenkripsi / chiper text.
 
**hint**: method yang mungkin berguna:
* `ord()`, `chr()`
* string method: `.isalpha()`, `.islower()`, dll
* jumlah karakter abjad 26
* nilai ord dari abjad/huruf berurutan
"""

Graded

```
def caesar_encript(txt,shift):
  pass
  # Mulai Kode anda di sini
```

Fungsi Decript caesar

```
def caesar_decript(chiper,shift):
  return caesar_encript(chiper,-shift)
```

Sanity check!!!

```
msg = 'Haloz DTS mania, MANTAPSZZZ!'
cpr = caesar_encript(msg,4)
txt = caesar_decript(cpr,4)

print('plain text:',txt)
print('chiper text:',cpr)
```

Expected output:
```
plain text: Haloz DTS mania, MANTAPSZZZ!
chiper text: Lepsd HXW qerme, QERXETWDDD!
```

Intro 2:

Fungsi shuffle_order akan mengurutkan string `txt` sesuai dengan list `order` parameter. Dimana `len(txt)==len(order)` dan elemen atau item di dalam order memenuhi $x \in \{0,..,\rm{len(txt)-1}\}$.

contoh: 
`(str) abcde: (list) [0,4,3,2,1]` maka keluarannya adalah `aedcb`. 
Fungsi ini akan digunakan di soal nomor 3 saat kita bermaksud mengirimkan text terenkripsi secara berkala dengan urutan acak dalam bentuk text-text yang lebih kecil.


b. Buatlah fungsi `deshuffle_order`, dengan argument `sftxt` (string) dan `order` (list). Yang akan mengembalikan urutan string kembali seperti semula sebelum di-shuffle. Sedemikian hingga: 
`deshuffle_order(shuffle_order(txt,order),order) == txt`
 
**hint: list method `.index()`**
"""

Graded
 
Fungsi mengacak urutan

```
def shuffle_order(txt,order):
  return ''.join([txt[i] for i in order])
```

Fungsi untuk mengurutkan kembali sesuai order

```
def deshuffle_order(sftxt,order):
  pass
  # Mulai Kode anda di sini
```
Sanity check!!!
 
```
print(shuffle_order('abcd',[2,1,3,0]))
print(deshuffle_order('cbda',[2,1,3,0]))
```

Expected output:

```
cbda
abcd
```
