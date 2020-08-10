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