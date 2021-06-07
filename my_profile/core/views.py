from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from core.forms import SubscriberForm
from core.models import Profile


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


class IndexView(View):
    def get(self, request):
        profile = Profile.objects.get(id=1)

        form = SubscriberForm()

        name = profile.name
        short_profile = "Data Craftsman. Passionate in software engineering, data engineering, and data science."
        github_url = "https://github.com/zkan/"
        facebook_url = "https://www.facebook.com/zkan.cs/"
        twitter_url = "https://twitter.com/zkancs"

        return render(
            request,
            "index.html",
            {
                "name": name,
                "form": form,
                "short_profile": short_profile,
                "github_url": github_url,
                "facebook_url": facebook_url,
                "twitter_url": twitter_url,
            }
        )

    def post(self, request):
        print(request.POST)
        print(request.POST.get("email"))

        form = SubscriberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("email"))

            # Ready to save into database

        profile = Profile.objects.get(id=1)
        name = profile.name
        short_profile = "Data Craftsman. Passionate in software engineering, data engineering, and data science."
        github_url = "https://github.com/zkan/"
        facebook_url = "https://www.facebook.com/zkan.cs/"
        twitter_url = "https://twitter.com/zkancs"

        return render(
            request,
            "index.html",
            {
                "name": name,
                "form": form,
                "short_profile": short_profile,
                "github_url": github_url,
                "facebook_url": facebook_url,
                "twitter_url": twitter_url,
            }
        )
