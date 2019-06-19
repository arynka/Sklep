class Koszyk():
 
	def __init__( self):
		 self.koszyk= []
 
	def dodaj_Towar( self, towar, ilosc):
		 self.koszyk.append([towar, ilosc])
		 
	def lacznyKoszt( self):
		
		for b in self.koszyk:
			 self.koszt = zwroc_Koszt() * b   #nie dziala
		
 
 
	def wyswietl_Koszyk( self):
		for a in  self.koszyk:
			print(" w sumie " +str(a[1])+ " KOSZ "+str(a[0].wyswietlOpis()) )
			
	def usun_Towar( self, numer):
		del  self.koszyk[numer]
 
 
class Towar(object):
 
	def __init__( self, cena_Jednostk, ilosc):
		 self.ilosc= ilosc
		 self.cena_Jednostk= cena_Jednostk
 
 
	def zwroc_Koszt( self):
		return(self.cena_Jednostk*self.ilosc) 
 
	def ustaw_Ilosc( self,ilosc ):
		 self.ilosc= ilosc
 
	def ustaw_Cene_Jednostk( self, cena_Jednostk):
		 self.cena_Jednostk= cena_Jednostk
 
 
class  TOWAR1(Towar):
 
	def __init__( self, cena_Jednostk, ilosc):
		Towar.__init__( self, cena_Jednostk, ilosc)
 
	def wyswietlOpis( self):
		return("Towar1, fghij567, 589k")
 
class  LatopToshibaC11(Towar):
 
	def __init__( self, cena_Jednostk, ilosc):
		Towar.__init__( self, cena_Jednostk, ilosc)
 
	def wyswietlOpis( self):
		return("Towar1, 356, 78")
 
class  TOWAR2(Towar):
 
	def __init__( self, cena_Jednostk, ilosc):
		Towar.__init__( self, cena_Jednostk, ilosc)
 
	def wyswietlOpis( self):
		return("Towar2, 123, 45")
 
class  Towar3(Towar):
 
	def __init__( self, cena_Jednostk, ilosc):
		Towar.__init__( self, cena_Jednostk, ilosc)
 
	def wyswietlOpis( self):
		return("Towar3, 12345")
 
class  Towar4(Towar):
 
	def __init__( self, cena_Jednostk, ilosc):
		Towar.__init__( self, cena_Jednostk, ilosc)
 
	def wyswietlOpis( self):
		return("Towar4, 475, 890")
 
class  Towar5(Towar):
 
	def __init__( self, cena_Jednostk, ilosc):
		Towar.__init__( self, cena_Jednostk, ilosc)
 
	def wyswietlOpis( self):
		return("Towar5, 207l, 6493k")
 
class  Towar6(Towar):
 
	def __init__( self, cena_Jednostk, ilosc):
		Towar.__init__( self, cena_Jednostk, ilosc)
 
	def wyswietlOpis( self):
		return("Towar6, 205lks, 493k")
 
class  Towar7(Towar):
 
	def __init__( self,cena_Jednostk, ilosc):
		Towar.__init__( self, cena_Jednostk, ilosc)
 
	def wyswietlOpis( self):
		return("Towar7, 683hjk, 793920k")
 

 
 
 
a1= Towar1(ilosc= 1, cena_JednostkJedn= 191)
a2= Towar2(ilosc= 2, cena_JednostkJedn= 292)
a3= Towar3(ilosc= 3, cena_JednostkJedn= 393)
a4= Towar4(ilosc= 4, cena_JednostkJedn= 495)
a5= Towar5(ilosc= 5, cena_JednostkJedn= 595)
a6= Towar6(ilosc= 6, cena_JednostkJedn= 696)
a7= Towar7(ilosc= 7,cena_JednostkJedn= 797)
a8= Towar1(ilosc= 1, cena_JednostkJedn= 198)
a9= Towar2(ilosc= 2, cena_JednostkJedn= 299)
a10= Towar3(ilosc= 3, cena_JednostkJedn= 310)
a11= Towar4(ilosc= 4, cena_JednostkJedn= 411)
a12= Towar5(ilosc= 5, cena_JednostkJedn= 512)
a13= Towar6(ilosc= 6, cena_JednostkJedn= 613)
a14= Towar7(ilosc= 7,cena_JednostkJedn= 714)


 
 
koszyk1=Koszyk()
koszyk2=Koszyk()
 
koszyk1.dodajTowar(a, 1)
koszyk1.dodajTowar(a2, 2)
koszyk1.dodajTowar(a3, 4)
koszyk1.dodajTowar(a4, 6)
koszyk1.dodajTowar(a5, 3)
koszyk1.dodajTowar(a6, 2)

koszyk2.dodajTowar(a7, 3)
koszyk2.dodajTowar(a8, 1)
koszyk2.dodajTowar(a9, 1)
koszyk2.dodajTowar(a10, 2)
koszyk2.dodajTowar(a11, 4)
koszyk2.dodajTowar(a12, 3)
 print("koszyk numer jeden ")
koszyk2.wyswietlKoszyk()
print("koszyk numer dwa ")
koszyk1.wyswietlKoszyk()
