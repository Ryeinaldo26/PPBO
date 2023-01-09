# Task 1
##Pada sebuah kelas di Kampus Mikroskil terdapat mahasiswa dan dosen pada kelas tersebut. Mahasiswa
##tersebut tentunya memiliki data berupa (bagian ini kalian cari tahu sendiri). Sedangkan dosen
##memiliki data berupa NIP, Nama, jabatan, jenis kelamin, dan no HP. Pada suatu acara, seorang
##mahasiswa ditujukan untuk melakukan rekap absensi dari acara tersebut. Absensi tersebut nantinya
##harus bisa dicetak serta bisa dihitung kira-kira berapa banyak jumlah pengunjung pada acara
##tersebut. Bisakah kalian membantu mahasiswa tersebut?

class mahasiswa:
    jumlah = 0
    acara = []
    def __init__ (self,nim,nama,kelas,jeniskelamin,nohp):
        self.nim = nim
        self.nama = nama
        self.kelas = kelas
        self.jenis = jeniskelamin
        self.no = nohp
        tmp = {"NIM": self.nim,"Nama": self.nama,"Kelas": self.kelas,"Jenis Kelamin": self.jenis,"No. HP": self.no}
        self.acara.append(tmp)
    def cetakData (self):
        for i in range(len(self.acara)):
            print(f'NIM             : {self.acara[i]["NIM"]}')
            print(f'Nama            : {self.acara[i]["Nama"]}')
            print(f'Kelas           : {self.acara[i]["Kelas"]}')
            print(f'Jenis Kelamin   : {self.acara[i]["Jenis Kelamin"]}')
            print(f'No. HP          : {self.acara[i]["No. HP"]}')
            print()
        print()
        print(f'Jumlah Peserta Mahasiswa : {len(self.acara)}')

class dosen:
    jumlah = 0
    acara = []
    def __init__ (self,nip,nama,jabatan,jeniskelamin,nohp):
        self.nip = nip
        self.nama = nama
        self.jabatan = jabatan
        self.jenis = jeniskelamin
        self.no = nohp
        tmp = {"NIP": self.nip,"Nama": self.nama,"Jabatan": self.jabatan,"Jenis Kelamin": self.jenis,"No. HP": self.no}
        self.acara.append(tmp)
    def cetakData (self):
        for i in range(len(self.acara)):
            print(f'NIP             : {self.acara[i]["NIP"]}')
            print(f'Nama            : {self.acara[i]["Nama"]}')
            print(f'Jabatan         : {self.acara[i]["Jabatan"]}')
            print(f'Jenis Kelamin   : {self.acara[i]["Jenis Kelamin"]}')
            print(f'No. HP          : {self.acara[i]["No. HP"]}')
            print()
        print()
        print(f'Jumlah Peserta Dosen : {len(self.acara)}')
###########################################################################################################################
#### a = dosen('121221333','Kagamine Rin','Dosen Tetap','Perempuan','082166996208')
#### b = mahasiswa('211110558','Alvin Nonitehe Syas Putra Laia','IF C Pagi','Laki-laki','081375269852')
#### c = mahasiswa('211111677','Ryeinaldo','IF C Pagi','Laki-laki','085761683128')
#### d = dosen('123321123','Kagamine Luka','Dosen Tetap','Laki-laki','085157996128')
#### a.cetakData()
#### b.cetakData()
#### c.cetakData
#### d.cetakData()
