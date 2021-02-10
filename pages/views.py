from django.http import HttpResponse


def homePageView(response):
    return HttpResponse('Hello, World!')

