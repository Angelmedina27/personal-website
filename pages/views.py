from django.shortcuts import render

def home_view(request):
    items = [
        {"name": "Learn Django basics", "completed": False},
        {"name": "Learn more about the stock market", "completed": False},
        {"name": "Enjoy my car as much as I can", "completed": True},
        {"name": "Save up some money", "completed": False},
        {"name": "Install a cam in my car", "completed": False},
    ]
    return render(request, "home.html", {"items": items})

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")