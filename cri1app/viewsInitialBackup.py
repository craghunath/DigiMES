from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

gblMetric = {'c1':{'m11':'1.1.1', 'm12':'1.1.2', 'm13':'1.1.3', 'm21':'1.2.1', 'm22':'1.2.2', 'm23':'1.2.3', 'm31':'1.3.1', 'm32':'1.3.2', 'm33':'1.3.3', 'm41':'1.4.1', 'm42':'1.4.2'}, 'c2':{'m11':'2.1.1'}}
gblYr = ['Year',2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
DEPT = ['DEPARTMENT','BOT','BIOTECH','CHEM','COMRC','COMPSC','ECO','ELE','ENG','HIN','HIS','JOU','KAN','KANpg','LIB','MAT','MATpg','PHY','PHYEDU','PSY','POLSC','SAN','SCO','STA','ZOO']
gblMnth = ['Month','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
context = {
        'gblYr': gblYr,
        'gblMetric': gblMetric,
        'DEPT': DEPT,
        'gblMnth':gblMnth,
        }
#count = 'none'

def cry1(request):
        if 'cri111flbtn' in request.POST:
                #from .models import M11m12
                #lnkBase = M111m12.objects.all()
                print(request.POST)
                print(request.FILES.getlist('cri111upld'))

                myfile = request.FILES['cri111upld']
                nname = '-'.join((request.POST['cri111flbtn'], myfile.name))
                fs = FileSystemStorage()
                if fs.exists(nname): fs.delete(nname)
                filename = fs.save(nname, myfile)
                fileUpload = fs.url(filename)
                #lnkBase.metricno = request.post['cri111flbtn']
                #lnkBase.discription500 = request.post['cri111text']
                #lnkBase.flname = nname
                #lnkBase.save()
                flcontext = {**context, **{'fileUpload': fileUpload,}}
                return render(request, 'cri1app/templates/crt/criteria1.html', flcontext)
        
        elif    'cri113optnbtn' in request.POST:
                #print(request.session)
                request.session['cri113optn'] = request.POST['cri113optn']
                return redirect('cry113')
        
        elif    'cri112flbtn' in request.POST:

                myfile = request.FILES['cri112upld']
                nname = '-'.join((request.POST['cri112flbtn'], myfile.name))
                fs = FileSystemStorage()
                if fs.exists(nname): fs.delete(nname)
                filename = fs.save(nname, myfile)
                fileUpload = fs.url(filename)
                flcontext = {**context, **{'fileUpload': fileUpload,}}
                return render(request, 'cri1app/templates/crt/criteria1.html', flcontext)
        elif    'cri121countbtn' in request.POST:
                request.session['cri121count'] = request.POST['cri121count']
                return redirect('cry121')
        elif    'cri122countbtn' in request.POST:
                request.session['cri122count'] = request.POST['cri122count']
                return redirect('cry122')

        else: return render(request, 'cri1app/templates/crt/criteria1.html', context)

def cry113(request):

        count = request.session['cri113optn']

        if 'cri113databtn' in request.POST:
               
                pass
                # M113.---= updation
                # count updation
                # Single file links to separate model with metric
                # only data upload
                # M113m23.totalprgm = request.session['cri113countbtn']             
     
        
        elif 'cri113flbtn' in request.POST:                
                      
                myfile = request.FILES['cri113upld']
                nname = '-'.join((request.POST['cri113flbtn'], myfile.name))
                fs = FileSystemStorage()
                if fs.exists(nname): fs.delete(nname)
                filename = fs.save(nname, myfile)
                fileUpload = fs.url(filename)
                flcontext = {**context, **{'fileUpload': fileUpload,'count': count, }}
                return render(request, 'cri1app/templates/crt/dt113.html', flcontext)

        
        flcontext = {**context, **{'count': count }}
        return render(request, 'cri1app/templates/crt/dt113.html', flcontext)

                



def cry121(request):

        count = request.session['cri121count']

        if 'cri121databtn' in request.POST:
               
                pass
                # M121.---= updation
                # count updation
                # Single file links to separate model with metric
                # only data upload
                # M121m23.totalprgm = request.session['cri121countbtn']             
     
        
        elif 'cri121flbtn' in request.POST:                
                      
                myfile = request.FILES['cri121upld']
                nname = '-'.join((request.POST['cri121flbtn'], myfile.name))
                fs = FileSystemStorage()
                if fs.exists(nname): fs.delete(nname)
                filename = fs.save(nname, myfile)
                fileUpload = fs.url(filename)
                flcontext = {**context, **{'fileUpload': fileUpload,'count': count, }}
                return render(request, 'cri1app/templates/crt/dt1211.html', flcontext)

        
        flcontext = {**context, **{'count': count }}
        return render(request, 'cri1app/templates/crt/dt1211.html', flcontext)

def cry122(request):

        count = request.session['cri122count']

        if 'cri122databtn' in request.POST:
               
                pass
                # M122.---= updation
                # count updation
                # Single file links to separate model with metric
                # only data upload
                # M122m23.totalprgm = request.session['cri122countbtn']             
     
        
        elif 'cri122flbtn' in request.POST:                
                      
                myfile = request.FILES['cri122upld']
                nname = '-'.join((request.POST['cri122flbtn'], myfile.name))
                fs = FileSystemStorage()
                if fs.exists(nname): fs.delete(nname)
                filename = fs.save(nname, myfile)
                fileUpload = fs.url(filename)
                flcontext = {**context, **{'fileUpload': fileUpload,'count': count, }}
                return render(request, 'cri1app/templates/crt/dt1221.html', flcontext)

        
        flcontext = {**context, **{'count': count }}
        return render(request, 'cri1app/templates/crt/dt1221.html', flcontext)




def page(request):
        

        #dingo = ''
        #flRef = []
#        if  'cri113btn' in request.POST:
#                print(request.POST)
#                dingo = request.POST['cri113']
#                dtemp = dingo
#                #flRef = list( request.POST.dict().copy() )
#                return render(request, 'cri1app/templates/tbl.html', { 'dingo': dingo,  })
        if 'cri113flbtn' in request.POST:#if request.method == 'POST' and request.FILES['upup'] : #and request.FILES['upup']
                
                print(request.POST)
                print(request.FILES.getlist('cri113upld'))

                #for rq in request.FILES.getlist('cri113upld'): print(rq)    
                        #myfile = request.FILES.getlist('cri113upld')[1]
                
                myfile = request.FILES['cri113upld']
                nname = '_'.join((request.POST['cri113yr'],request.POST['cri113flbtn'], myfile.name))
                fs = FileSystemStorage()
                if fs.exists(nname): fs.delete(nname)
                filename = fs.save(nname, myfile)
                uploaded_file_url = fs.url(filename)
                flcontext = {**context, **{'uploaded_file_url': uploaded_file_url,}}
                return render(request, 'cri1app/templates/tblx.html', flcontext)
        else: return render(request, 'cri1app/templates/tblx.html', context)




#'gblYr':gblYr,'gblMetric':gblMetric,