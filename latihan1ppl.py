# membuat class jadwal

print("-->Rachel Setyawan Hanapi<--")

# senin

class senin():
    def PPL():
        pengajar = "Pak Qibar"
    def PWPB():
        pengajar = "Pak Sudrajat"
    def PBO():
        pengajar = "Pak Rendi"

obj = senin()
obj.PPL = "Pemodelan Perangkat Lunak"
obj.PWPB = "Pemograman Web Perangkat Bergerak"
obj.PBO = "Pemograman Berbasis Web"
print('------>Senin<------')
print (obj.PPL)
print (obj.PWPB)
print (obj.PBO)

# Selasa

class selasa():
    def PWPB():
        pengajar = "Pak Sudrajat"
    def B_Ing():
        pengajar = "Ms. Vera Diana"
    def Mtk():
        pengajar = "Bu Dwi Kurniati"

obj = selasa()
obj.PWPB = "Pemograman Web Perangkat Bergerak"
obj.B_Ing = "B.Inggris"
obj.Mtk = "Matematika"
print('------>Selasa<------')
print (obj.PWPB)
print (obj.B_Ing)
print (obj.Mtk)

# Rabu

class rabu():
    def PKK():
        pengajar = "Pak Rendi"
    def Penjas():
        pengajar = "Pak Yayang"
    def B_Ind():
        pengajar = "Pak Saipul"

obj = rabu()
obj.PKK = "Prakarya dan Kewirausahaan"
obj.Penjas = "Pejaskes"
obj.B_Ind = "B.Indonesia"
print('------>Rabu<------')
print (obj.PKK)
print (obj.Penjas)
print (obj.B_Ind)

# Kamis

class kamis():
    def PWPB():
        pengajar = "Pak Sudrajat"
    def PKK():
        pengajar = "Pak Rendi"
    def PKN():
        pengajar = "Pak Suar"
    def PAI():
        pengajar = "Pak Zaenal"

obj = kamis()
obj.PWPB = "Pemograman Web Perangkat Bergerak"
obj.PKK = "Prakarya dan Kewirausahaan"
obj.PKN = "Pendidikan Kewarga Negaraan"
obj.PAI = "Pendidikan Agama Islam"
print('------>Kamis<------')
print (obj.PWPB)
print (obj.PKK)
print (obj.PKN)
print (obj.PAI)

#Jumat

class jumat():
    def PWPB():
        pengajar = "Pak Sudrajat"
    def PKK():
        pengajar = "Pak Rendi"

obj = jumat()
obj.PWPB = "Pemograman Web Perangkat Bergerak"
obj.PBO = "Pemograman Berbasis Web"
print('------>Jumat<------')
print (obj.PWPB)
print (obj.PBO)