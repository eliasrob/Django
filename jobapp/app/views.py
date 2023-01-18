from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, reverse
from django.template import loader

# Create your views here.

job_title = [
    "first job title",
    "second job title"
]

job_description = [
    "first job desc",
    "second job desc"
]

class tempClass():
    x = 5


def hello(request):
    # template = loader.get_template('app/hello.html')
    is_authenticated = False
    context = { "name":"django", "jobList":job_title, "temp":tempClass, "age":"30", "is_authenticated":is_authenticated}
    
    # return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html", context)
    # return render(request, "app/happyNewyear.html", context)

res =""
# def job_list(request):
#     # return HttpResponse("hello world")
#     res = "<ul>"
#     for i in range(len(job_title)):
#         reversedDetailUrl = reverse('jobs_detail', args=(i,))
        
        
#         res += f"<li> <a href= '{reversedDetailUrl}'> {job_title[i]}</a>  / {job_description[i]} </li>"
#     res +="</ul>"    
#     return HttpResponse(res)

def job_list(request):
    context = {"job_titleList":job_title, "job_descriptionList": job_description, "length": len(job_title) }
    return render(request, "app/index.html", context)
    # return render(request, "app/happyNewyear.html", context)

def jobDetails(request, id):
    context = {"job_title":job_title[id], "job_description": job_description[id] }
    print("the id here is: "+str(id))
    try:
        if(id == 0):
            return redirect(reverse('jobs_home'))
        else:
            # return_html = f"<h1>{job_title[id]}</h1> <h3> {job_description[id]}</h3>"
            # return HttpResponse(return_html)
            
            return render(request, "app/job_details.html", context)
    except:
        return HttpResponseNotFound("Not Found")