from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    html = """
      <html>
        <head>
          <title>Kan Ouivirach</title>
        </head>
        <body>
          <h1>Kan Ouivirach</h1>
          <p>Data Craftsman. Passionate in software engineering, data engineering, and data science.</p>
          <div><span>GitHub:</span> https://github.com/zkan/</div>
          <div><span>Facebook:</span> https://www.facebook.com/zkan.cs/</div>
          <div><span>Twitter:</span> https://twitter.com/zkancs</div>
        </body>
      </html>
    """
    return HttpResponse(html)
