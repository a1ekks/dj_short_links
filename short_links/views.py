# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.db.models import F
from models import ShortLink
from forms import ShortUrlForm
import simplejson as json
# Create your views here.


def main(request):
    form = ShortUrlForm()
    links = ShortLink.objects.all().order_by('-use', '-created')[:20]
    return render(request, 'index.html', {'links': links, 'form': form})


def list(request):
    links = ShortLink.objects.all().order_by('-use', '-created')
    return render(request, 'list.html', {'links': links})


def add_short_link(request):
    errors = {}
    if request.method == "POST":
        form = ShortUrlForm(request.POST)
        if form.is_valid():
            short_url = form.save(commit=False)
            short_url.save()
            errors['state'] = '/url_info/{}'.format(short_url.id)
            return HttpResponse(json.dumps(errors, sort_keys=True))
        else:
            errors.update(form.errors)
            return HttpResponse(json.dumps(errors, sort_keys=True))


def del_short_link(request, id):
    cur_url = get_object_or_404(ShortLink, id=id)
    cur_url.delete()
    return redirect('list')


def url_info(request, id):
    cur_url = get_object_or_404(ShortLink, id=id)
    return render(request, 'url_info.html', {'cur_url': cur_url})


def redir_to(request, short_url):
    cur_dst = get_object_or_404(ShortLink, link_short=short_url)
    cur_dst.use = F('use') + 1
    cur_dst.save()
    return HttpResponseRedirect(cur_dst.link_orig)
