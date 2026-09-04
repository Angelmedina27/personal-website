from django.shortcuts import render

def home_view(request):
    items = [
        {"name": "Learn Django basics", "completed": True},
        {"name": "Set up project repository", "completed": True},
        {"name": "Build out personal website views", "completed": False},
        {"name": "Pass all 14 automation tests", "completed": False},
        {"name": "Submit repository link on Canvas", "completed": False},
    ]
    return render(request, "home.html", {"items": items})

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")