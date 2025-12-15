from django.shortcuts import render
def fueleff(request):
    d = int(request.POST.get('distance', 0))
    f = int(request.POST.get('fuel', 0))
    efficiency = d/f if request.method == 'POST' else 0
    print("Distance=",d)
    print("Fuel=",f)
    print("Efficiency=",efficiency)
    return render(request, 'mathserverapp/math.html', {'d': d, 'f': f, 'efficiency': efficiency})