from django.db import models

class Kiado(models.Model):

    azon = models.IntegerField()
    nev = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("Kiado")
        verbose_name_plural = ("Kiadok")

    def __str__(self):
        return self.nev

    def feltolt(sorok:list[str]):
        Kiado.objects.all().delete()
        for sor in sorok:

            s = sor.split('\t')
            if len(s)!=2:
                return "Nem megfelelő db tabulátor!"
            try:
                azon = int(s[0])
            except:
                return  f"Hiba az egyik rekordban. Az 1. mezőben egész számot kell megadni!"
            Kiado.objects.create(azon=azon,nev=s[1])
        return None
        

   
class Film(models.Model):

    azon = models.IntegerField()
    cim = models.CharField(max_length=100)
    kiadasiev  = models.IntegerField(null=True)
    kocka = models.IntegerField(null=True)
    szinese = models.BooleanField()
    kiado = models.ForeignKey(Kiado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Film")
        verbose_name_plural = ("Filmek")

    def __str__(self):
        return self.cim

    def feltolt(sorok):
        Film.objects.all().delete()
        
        for sor in sorok:
            
            s = sor.split('\t')
            if len(s)!=6:
                return "Nem megfelelő db tabulátor!"
            try:
                azon = int(s[0])
            except:
                return  f"Hiba az egyik rekordban. Az 1. mezőben egész számot kell megadni!"
            try:
                kiadasiev = None if s[2]=='' else int(s[2])          
            except:
                return  f"Hiba az egyik rekordban. A 3. mezőben egész számot kell megadni!"
            try:
                kocka = None if s[3]=='' else int(s[3])          
            except:
                return  f"Hiba az egyik rekordban. A 4. mezőben egész számot kell megadni!"
            try:
                kiadoazon = int(s[5])
            except:
                return  f"Hiba az egyik rekordban. Az 6. mezőben egész számot kell megadni!"
            try:
                kiado = Kiado.objects.get(azon=kiadoazon)
            except:
                return  f"Nincs ilyen azonosítójú kiadó!"
           
            Film.objects.create(azon=azon,cim=s[1],kiadasiev=kiadasiev, kocka=kocka, szinese=s[4]=='-1',kiado=kiado)
        return None
    
