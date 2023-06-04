from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.db.models import Count

from appdef.models import Film, Kiado

def index(request):
    return render(request,'index.html',{})

def feltoltes(request, table):
    if(table not in [ 'kiado', 'film' ]):
        raise Exception("Nincs ilyen nevű tábla")

    if(request.method != 'POST'):
        return render(request, 'feltoltes.html',{ "table": table })

    try:
        szoveg = request.POST['szoveg']
    except:
        return HttpResponseServerError("Meg kell adni a 'szoveg' mezőt!")

    sorok = szoveg.replace('\r\n', '\n').split('\n')
    sorok = sorok[1:]
    if sorok[-1] == "":
        sorok = sorok[0:-1]

    feltolt = Kiado.feltolt if table == "kiado" else Film.feltolt 
    err = feltolt(sorok)
    if err:
        return HttpResponseServerError(f"Hiba történt: {err}")

    return HttpResponse(f"Sikeresen feltöltve rekord.")

def feladat2(request):
    return render(request,'feladat2.html',{'filmek':Film.objects.filter(kiadasiev__gte=2000).order_by('cim')})
 
def feladat3(request):
    return render(request,'feladat3.html',{'filmek':Film.objects.filter(cim__icontains='farkas')})

def feladat4(request):
    return render(request,'feladat4.html',{'nevek':Film.objects.filter(cim__icontains='Sicc').values_list("kiado__nev",flat=True).distinct()})

def feladat5(request):
    return render(request,'feladat5.html',{'film':Film.objects.values('cim').annotate(db=Count('cim')).order_by('-db').first()})

def feladat6(request):
    return render(request,'feladat6.html',{'filmek':Film.objects.exclude(kiadasiev=None).values('kiadasiev').annotate(db=Count('kiadasiev')).order_by('-db')})

def feladat7(request):
    szinescimek = Film.objects.filter(szinese=True).order_by('cim').values_list("cim",flat=True).distinct()
    return  render(request,'feladat7.html',{'cimek':[cim for cim in szinescimek if Film.objects.filter(cim=cim,szinese=False).exists()]})

 