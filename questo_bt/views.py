from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Quest


def index(request):
    context = {}
    context["quests"] = Quest.objects.all(
    ).exclude(
        status="D"
    ).order_by('-status')
    #context["quests"] = Quest.objects.filter(priority="S")
    return render(request, "questo_bt/index.html", context)


def detail(request, quest_id):
    quest = get_object_or_404(Quest, pk=quest_id)
    return render(request, 'questo_bt/detail.html', {'quest': quest})


def add_quest(request):
    if "text" in request.POST:
        quest = Quest()
        quest.text = request.POST["text"]
        #print("text: ",quest.text)
        if quest.text != None and quest.text != "":
            quest.priority = request.POST["priority"]
            quest.save()
        else:
            response = HttpResponse()
            response.status_code = 400
            return   response
    return redirect('questo_bt:index',)


def delete_quest(request,quest_id):
    quest = Quest.objects.get(pk=quest_id)
    quest.delete()
    return redirect('questo_bt:index')


def update_status(request, quest_id):
    if "status" in request.POST:
        quest = Quest.objects.get(pk=quest_id)
        quest.status = request.POST["status"]
        quest.save()
    return HttpResponseRedirect(reverse('questo_bt:index'))


def update_priority(request, quest_id):
    if "priority" in request.POST:
        quest = Quest.objects.get(pk=quest_id)
        quest.priority = request.POST["priority"]
        quest.save()
    return render(request, 'questo_bt/detail.html', {'quest': quest})


def filter_quests(request):
    context = {}
    if "priority" in request.POST:
        choice = request.POST["priority"]
        context["quests"] = Quest.objects.filter(priority=choice).order_by('-status')
    #return HttpResponse("You're looking at filter_quests)
    return render(request, "questo_bt/index.html", context)


def solved_quests(request):
    context = {}
    context["solved_quests"] = Quest.objects.filter(status="D")
    return render(request, "questo_bt/solved_quests.html", context)

