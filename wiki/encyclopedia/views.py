from django.shortcuts import render

from . import util

import markdown2

from markdown2 import *

import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method == "POST":
        entry = request.POST['q']
        new_list = []
        for p in util.list_entries():
            if entry.lower() == p.lower():
                return render(request, "encyclopedia/page.html", {
                "body": markdown2.markdown(util.get_entry(p)), "title": p
                })
            elif entry.lower() in p.lower():
                new_list.append(p)
        if new_list:
                return render(request, "encyclopedia/search_page.html", {
                "entries": new_list
                })
        else:
            return render(request, "encyclopedia/error.html", {"error": "This page does not exist"})
    
def new_page(request):
    if request.method == "POST":
        title= request.POST['new_title']
        for p in util.list_entries():
            if title.lower() == p.lower():
                return render(request, "encyclopedia/error.html", {"error": "This page already exists"})
        content = request.POST['new_content']
        util.save_entry(title, content)            
        return render(request, "encyclopedia/page.html", {"body": markdown2.markdown(util.get_entry(title)), "title": title})
    else:
        return render(request, "encyclopedia/newpage.html")

def edit(request):
    if request.method == "POST":
        title=request.POST['entry_title']
        content = util.get_entry(title)
    return render(request, "encyclopedia/editpage.html", {'title': title, "content": content})

def editsub(request):
    if request.method == "POST":
        title=request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content) 
    return render(request, "encyclopedia/page.html", {"body": markdown2.markdown(util.get_entry(title)), "title":title})

def randompage(request):
    entries = []
    for entry in util.list_entries():
        entries.append(entry)
    title = random.choice(entries)
    return render(request, "encyclopedia/page.html", {"body": markdown2.markdown(util.get_entry(title)), "title":title})

def title(request, title):
    if util.get_entry(title) == None:
        return render(request,"encyclopedia/error.html", {"error": "This page does not exist"})
    else:
        return render(request, "encyclopedia/page.html", {"body": markdown2.markdown(util.get_entry(title)), "title":title})







