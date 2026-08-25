from django.shortcuts import render


def bienvenido(request):
    return render(request, "base.html")
