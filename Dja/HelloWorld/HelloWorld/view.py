from django.shortcuts import render
 
def runoob(request):
    views_list = ["菜鸟教程","菜鸟教程1","菜鸟教程2","菜鸟教程3"]
    name = "wzq"
    return render(request, "runoob.html",{"name":name})