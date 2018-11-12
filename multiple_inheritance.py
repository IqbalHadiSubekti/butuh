#contoh multiple inheritance kantor
class Sawah():
	def p(self):
		print("Tempat untuk menanam padi")
		
class Petani(Sawah):
	def p(self):
		print("Mengolah sawah")

class Pupuk(Sawah):
	def p(self):
		print("Diberikan untuk tanaman padi")


class Irigasi(Sawah):
	def p(self):
		print("Memberikan pengairan bagi sawah")		

class Lahan(Petani,Pupuk):
	pass

class Air(Irigasi,Pupuk):
	pass
	
class Padi(Sawah):
	harga = 400000
	if harga > 500000:
		print("Harga padi naik")
	elif harga < 500000:
		print("Harga padi turun")
	else:
		print("Harga padi stabil")
		
l = Lahan()
l.p()
a = Air()
a.p()