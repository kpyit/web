from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)

# def index(request):
#     logger.info('index page accessed')
#     return HttpResponse("HelW")
 
def index(request): 
    logger.debug('index page accessed')
    html_text = """
        <h1>main Vindow</h1>
        <p>la la la </p>
        <p>all good</p>
    """
    return render(request, 'index.html', {'html_text': html_text})

def obout_me(request):
    # Multiline text variable with HTML layout
    logger.debug('obout_me page accessed')
    html_text = """
        <h1>PK</h1>
        <p> </p>
        <p>  </p>
    """
    return render(request, 'obout_me.html', {'html_text': html_text})


def about(request):
    try:
        result = 1/0
    except Exception as e:
        logger.exception(f'Error in ab page{e}')
        return HttpResponse(" Error ")
    else:
        logger.debug('ab page access')
    return HttpResponse("ab us")



