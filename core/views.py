from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html', {})

def about(request):
    return render(request, 'core/about.html', {})

def error(request, code):
    if code == 400:
        return error400(request, None)
    elif code == 403:
        return error403(request, None)
    elif code == 404:
        return error404(request, None)
    elif code == 500:
        return error500(request)
    else:
        return errorGeneral(request)

def error400(request, exception):
    return __loadErrorView(request, 400, 'Sorry, you\'ve messed up. Check your request! Double check it!')

def error403(request, exception):
    return __loadErrorView(request, 403, 'Sorry, this is forbidden knowledge, and we can\'t show it to you :)')

def error404(request, exception):
    return __loadErrorView(request, 404, 'Sorry, we can\'t find what you\'re asking to see.')

def error500(request):
    return __loadErrorView(request, 500, 'Sorry, the website has some bugs. No worries, we\'ll fire the developer.')

def errorGeneral(request):
    return __loadErrorView(request, 'Error', 'Sorry, something\'s not right. Please check back later.')

def __loadErrorView(request, error_code, error_text):
    context = {
        'error_code': error_code,
        'error_text': error_text,
    }

    return render(request, 'core/error.html', context)
