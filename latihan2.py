print("Rahayu wiiii")

x = 5
y = 6

hasil = x*y+2*x-2*y

print('ni hasilnya wii',hasil)

trueOrFalse = True
print(trueOrFalse)

ar = ['blue','green','red']
print(ar[0])

dic = {'nama buah':'durian',
        'nama ilmiah':'Durio Zibethinus',
        'asal': 'malaysia',
        'persebaran':'Asia Tenggara'}
print(dic['nama buah'])


if 5>2:
    print("lima lebih dari dua anjayyy")

x =4
y = (8-x)
if x == y :
    print("x dan y sama")
else:
    print("x dan y beda")

for isi in ar:
    print(isi)

def ini_fungsi(siapaNamanya):
    print(siapaNamanya + "belajar bahasa setan")

ini_fungsi("Wayan hihihi")

ini_fungsi("kak tri")

ini_fungsi("semua orang")

import cv2

import datetime as dt
x = dt.datetime.now()
print(x)

from datetime import date

hariini = date.today()

print("Hari ini tanggal", hariini) 

import numpy as np
a = np.array([1,2,3])

print(a.shape)
print(a.dtype)