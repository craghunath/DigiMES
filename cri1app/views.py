from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import cri1app.models as mdl

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
psd = {'usr1':'psw1', 'usr2':'psw2'}
#count = 'none'
#try: http://35.188.109.10:9090/
#        lgin = request.session['usr']

def logoff(request):
        del request.session['usr']
        return render(request, 'cri1app/templates/crt/psswd.html', {'psr':''})


def logon(request):
    
    
    psr = ''
    if request.POST:

        try:
            chck = psd[request.POST['usr']]
            request.session['usr'] = request.POST['usr'] 
            if chck == request.POST['password']:                    
                    return redirect('cry1')
            else:
                psr = 'yes'
                #return render(request, 'pages/psswd.html', {'psr':psr})
        except:
            psr = 'yes'

    return render(request, 'cri1app/templates/crt/psswd.html', {'psr':psr})


def cry1(request):
        try:
                if request.session['usr']:
                        #del request.session['usr']
                        if 'cri111flbtn' in request.POST:

                                lnkBase = mdl.M111m12(metric=request.POST['cri111flbtn'], description_500wrds=request.  POST      ['cri111txt'])
                                lnkBase.save()                
                                myfile = request.FILES['cri111upld']
                                nname = '-'.join((request.POST['cri111flbtn'], myfile.name))
                                fs = FileSystemStorage()
                                if fs.exists(nname): fs.delete(nname)
                                filename = fs.save(nname, myfile)
                                fileUpload = fs.url(filename)
                                flnk = mdl.Filelinks(metric=request.POST['cri111flbtn'], file_name=nname,       file_link=fileUpload)
                                flnk.save()
                                flcontext = {**context, **{'fileUpload': fileUpload,}}
                                return render(request, 'cri1app/templates/crt/criteria1.html', flcontext)

                        elif 'cri112flbtn' in request.POST:

                                lnkBase = mdl.M111m12(metric=request.POST['cri112flbtn'], description_500wrds=request.  POST      ['cri112txt'])
                                lnkBase.save()                
                                myfile = request.FILES['cri112upld']
                                nname = '-'.join((request.POST['cri112flbtn'], myfile.name))
                                fs = FileSystemStorage()
                                if fs.exists(nname): fs.delete(nname)
                                filename = fs.save(nname, myfile)
                                fileUpload = fs.url(filename)
                                flnk = mdl.Filelinks(metric=request.POST['cri112flbtn'], file_name=nname,       file_link=fileUpload)
                                flnk.save()
                                flcontext = {**context, **{'fileUpload': fileUpload,}}
                                return render(request, 'cri1app/templates/crt/criteria1.html', flcontext)

                        elif    'cri113optnbtn' in request.POST:
                                request.session['cri113optn'] = request.POST['cri113optn']
                                return redirect('cry113')
                        elif    'cri121countbtn' in request.POST:
                                request.session['cri121count'] = request.POST['cri121count']
                                return redirect('cry121')
                        elif    'cri122countbtn' in request.POST:
                                request.session['cri122count'] = request.POST['cri122count']
                                return redirect('cry122')
                        elif    'cri123countbtn' in request.POST:
                                lnkBase = mdl.M123(metric=request.POST['cri123countbtn'], year=request.POST['cri123yr'] ,        enrolled_students_no=request.POST['cri123count'])
                                lnkBase.save()

                        else: return render(request, 'cri1app/templates/crt/criteria1.html', context)
        except: return redirect('logon')

def cry113(request):

        try:
                if request.session['usr']:
                        count = request.session['cri113optn']

                        if 'cri113databtn' in request.POST:
                        
                                lnkBase = mdl.M113(metric=request.POST['cri113databtn'], option=count, year=request.POST        ['cri113yr'],   month=request.POST['cri113mnth'], department=request.POST['cri113dept'],        teacher_name=request.POST        ['cri113name'], participated_body=request.POST['cri113body'])
                                lnkBase.save()

                        elif 'cri113flbtn' in request.POST:                

                                myfile = request.FILES['cri113upld']
                                nname = '-'.join((request.POST['cri113flbtn'], myfile.name))
                                fs = FileSystemStorage()
                                if fs.exists(nname): fs.delete(nname)
                                filename = fs.save(nname, myfile)
                                fileUpload = fs.url(filename)
                                flnk = mdl.Filelinks(metric=request.POST['cri113flbtn'], file_name=nname,       file_link=fileUpload)
                                flnk.save()
                                flcontext = {**context, **{'fileUpload': fileUpload,'count': count, }}
                                return render(request, 'cri1app/templates/crt/dt113.html', flcontext)


                        flcontext = {**context, **{'count': count }}
                        return render(request, 'cri1app/templates/crt/dt113.html', flcontext)
        except: return redirect('logon') 

def cry121(request):

        try:
                if request.session['usr']:
                        count = request.session['cri121count']

                        if 'cri121databtn' in request.POST:

                                lnkBase = mdl.M121(metric=request.POST['cri121databtn'], program_code=request.POST      ['cri121code'],       program_name=request.POST['cri121name'], year=request.POST['cri121yr'],         month=request.POST    ['cri121mnth'], implment_status=request.POST['cri121implementstatus'],    implment_year=request.POST   ['cri121yrimplement'], implment_month=request.POST    ['cri121mnthimplement'], program_totalNo=count)
                                lnkBase.save()            


                        elif 'cri121flbtn' in request.POST:                

                                myfile = request.FILES['cri121upld']
                                nname = '-'.join((request.POST['cri121flbtn'], myfile.name))
                                fs = FileSystemStorage()
                                if fs.exists(nname): fs.delete(nname)
                                filename = fs.save(nname, myfile)
                                fileUpload = fs.url(filename)
                                flnk = mdl.Filelinks(metric=request.POST['cri121flbtn'], file_name=nname,       file_link=fileUpload)
                                flnk.save()
                                flcontext = {**context, **{'fileUpload': fileUpload,'count': count, }}
                                return render(request, 'cri1app/templates/crt/dt121.html', flcontext)


                        flcontext = {**context, **{'count': count }}
                        return render(request, 'cri1app/templates/crt/dt121.html', flcontext)
        except: return redirect('logon')

def cry122(request):

        try:
                if request.session['usr']:
                        count = request.session['cri122count']

                        if 'cri122databtn' in request.POST:
                                lnkBase = mdl.M122(metric=request.POST['cri122databtn'], year=request.POST['cri122yr'],         month=request.  POST['cri122mnth'], course_name=request.POST['cri122name'],     course_code=request.POST['cri122code'],       department=request.POST['cri122dept'],        offered_year=request.POST['cri122yroffer'],    offered_month=request.POST['cri122mnthoffer'],  offered_times=request.POST['cri122times'],  course_duration=request.POST['cri122duration'],      enrolled_students_no=request.POST        ['cri122studentEnrolled'],  completed_students_no=request.POST['cri122studentCompleted'],        course_totalNo=count)
                                lnkBase.save() 


                        elif 'cri122flbtn' in request.POST:                

                                myfile = request.FILES['cri122upld']
                                nname = '-'.join((request.POST['cri122flbtn'], myfile.name))
                                fs = FileSystemStorage()
                                if fs.exists(nname): fs.delete(nname)
                                filename = fs.save(nname, myfile)
                                fileUpload = fs.url(filename)
                                flnk = mdl.Filelinks(metric=request.POST['cri122flbtn'], file_name=nname,       file_link=fileUpload)
                                flnk.save()
                                flcontext = {**context, **{'fileUpload': fileUpload,'count': count, }}
                                return render(request, 'cri1app/templates/crt/dt122.html', flcontext)

        
                        flcontext = {**context, **{'count': count }}
                        return render(request, 'cri1app/templates/crt/dt122.html', flcontext)
        except: return redirect('logon')

def cryd1(request):
        try:
                if request.session['usr']:
                        filename = mdl.Filelinks.objects.all()
                        return render(request, 'cri1app/templates/crt/filesDisplay.html', {'filename':filename,})
        except: return redirect('logon')




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