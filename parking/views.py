from django.shortcuts import render
from django.http import HttpResponse
from .models import Pass, Log, History
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def index(request):
    try:
        passes = Pass.objects.all()

        tags = cache.keys("tag:*")

        print([t[4:] for t in tags])
        print(tags)
        for pass1 in passes:
            print(pass1.name)
        return render(request, "passes.html", {"passes": passes})
    except:
        return render(request, "passes.html")


def get_current(request):
    if request.htmx:
        info = []
        try:
            tags = cache.keys("tag:*")
            new_tag = [(t[4:], int(cache.get(t))) for t in tags]
            sorted_list = sorted(new_tag, key=lambda tag: tag[1])
            for t in sorted_list:
                try:
                    current_pass = Pass.objects.get(epc=t[0])
                except:
                    current_pass = None
                if current_pass:
                    info.append(current_pass)
            return render(request, "current_passes.html", {"passes": info})
        except:
            pass


@csrf_exempt
def tag_handler(request):
    if request.method == "GET":
        tag = request.GET["epc"]
        try:
            checked_pass = Pass.objects.get(epc=tag)
        except:
            checked_pass = None
        if checked_pass:
            return HttpResponse("true")
        return HttpResponse("false")
    if request.method == "POST":
        # data = request.POST
        try:
            print(json.loads(request.body))
            epc = json.loads(request.body)["epc"]
            # date = data.get("timestamp")
            park_pass = Pass.objects.get(epc=epc)
            new_history = History(
                parking_pass=park_pass,
            )
            new_history.save()
            # new_log = Log(
            #     epc=epc,
            # )
            # new_log.save()
            return HttpResponse("Data saved")
        except:
            return HttpResponse("Failed")

    # passes = Pass.objects.all()
    # tags = cache.keys("tag:*")
    # print([t[4:] for t in tags])
    # print(tags)
    # return render(request, "passes.html", {"passes": passes})
