def cry113(request):

        refr = ''
        count = '' 
        if 'cri113kash' in request.POST:
                count = request.POST['cri113kash']
                print(count)                
                flcontext = {**context, **{'refr': refr,'count': count}}       
        
        
        
        if 'cri113flbtn' in request.POST:
                
                refr = request.POST['cri113flbtn']
                print(refr)
                print(count)
                #print(request.FILES)
                flcontext = {**context, **{'refr': refr,'count': count}}
                return render(request, 'cri1app/templates/crt/dt113.html', flcontext)
               
        else: return render(request, 'cri1app/templates/crt/dt113.html', flcontext) 

#cry1
        elif    'cri113kashbtn' in request.POST:
                rdfl = open('cri1app/countfl', "w")
                rdfl.write(request.POST['cri113kash'])
                rdfl.close()
#cry113
def cry113(request):

        refr = ''
        rdfl =open('cri1app/countfl',"r")
        count = rdfl.read()
        rdfl.close()
        flcontext = {**context, **{'refr': refr,'count': count}}
        
        if 'cri113flbtn' in request.POST:
                
                refr = request.POST['cri113flbtn']
                #M113.optn = count
                print(refr)
                print(count)
                #print(request.FILES)
                flcontext = {**context, **{'refr': refr,'count': count}}
                return render(request, 'cri1app/templates/crt/dt113.html', flcontext)
               
        else: return render(request, 'cri1app/templates/crt/dt113.html', flcontext) 


try:
    chck = request.session['usr']
    print(chck)
    if chck in psdct:

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', ve1.logon, name='logon'),
            path('111', ve1.cry1, name='cry1'),
            #path('12/', ve1.cry12, name='cry12'),    
            path('113/', ve1.cry113, name='cry113'),
            path('121/', ve1.cry121, name='cry121'),
            path('122/', ve1.cry122, name='cry122'),
            path('d1/', ve1.cryd1, name='cryd1'),
            path('tbl/', ve1.page, name='nota'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    else:
        urlpatterns = [
            path('', ve1.logon, name='logon'),
        ]

except:
    urlpatterns = [
        path('', ve1.logon, name='logon'),
    ]

        if 'cri111flbtn' in request.POST:
                
                lnkBase = mdl.M111m12(metric=request.POST['cri111flbtn'], description_500wrds=request.POST['cri111txt'])
                lnkBase.save()                
                myfile = request.FILES['cri111upld']
                nname = '-'.join((request.POST['cri111flbtn'], myfile.name))
                fs = FileSystemStorage()
                if fs.exists(nname): fs.delete(nname)
                filename = fs.save(nname, myfile)
                fileUpload = fs.url(filename)
                flnk = mdl.Filelinks(metric=request.POST['cri111flbtn'], file_name=nname, file_link=fileUpload)
                flnk.save()
                flcontext = {**context, **{'fileUpload': fileUpload,}}
                return render(request, 'cri1app/templates/crt/criteria1.html', flcontext)
        
        elif 'cri112flbtn' in request.POST:
                
                lnkBase = mdl.M111m12(metric=request.POST['cri112flbtn'], description_500wrds=request.POST['cri112txt'])
                lnkBase.save()                
                myfile = request.FILES['cri112upld']
                nname = '-'.join((request.POST['cri112flbtn'], myfile.name))
                fs = FileSystemStorage()
                if fs.exists(nname): fs.delete(nname)
                filename = fs.save(nname, myfile)
                fileUpload = fs.url(filename)
                flnk = mdl.Filelinks(metric=request.POST['cri112flbtn'], file_name=nname, file_link=fileUpload)
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
                lnkBase = mdl.M123(metric=request.POST['cri123countbtn'], year=request.POST['cri123yr'], enrolled_students_no=request.POST['cri123count'])
                lnkBase.save()

        else: return render(request, 'cri1app/templates/crt/criteria1.html', context)