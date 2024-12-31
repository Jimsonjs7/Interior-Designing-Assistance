from django.shortcuts import render

def modern(request):
    return render(request,'modern.html')
def living_room_designs(request):
    return render(request,'living_room_designs.html')
