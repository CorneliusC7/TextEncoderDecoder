huruf = "a^b^c^d^e^f^g^h^i^j^k^l^m^n^o^p^q^r^s^t^u^v^w^x^y^z^ ^.^-^=".lower().split("^")
angka = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28".split()
def decode(s):
    lalah = ""
    s = s.split()
    for i in s:
        lalah = lalah + huruf[int(i)-1]
    print(lalah)
def encode(s):
    alig = []
    ha = ""
    for f in s:
        alig.append(f)
    for i in alig:
        ha = ha + str(huruf.index(i)+1) + " "
    print(ha)

while True:
    if input("Mode : ") == "e":
        encode(input().lower())
    else:
        decode(input())
