import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from server.forms import LogDataForm
from server.models import Log


@csrf_exempt
def update_log(request):
    if request.method == "POST":
        try:
            form = LogDataForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data.get('data')
                log, _ = Log.objects.get_or_create(data=data)
                return HttpResponse(json.dumps({'status': 200, 'message': "data saved successfully"}), content_type='application/json')
            return HttpResponse(json.dumps({'status': 403, 'message': form.errors}), content_type='application/json')

        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({'status': 503, 'message': e}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'status': 404, 'message': 'only POST request allowed'}), content_type='application/json')


def home(request):
    logs = map(lambda i: i.data, Log.objects.all())
    data = []
    for log in logs:
        data.append(log.split("@"))
    # print(data)
    return render(request, 'home.html', context={'logs': data})
