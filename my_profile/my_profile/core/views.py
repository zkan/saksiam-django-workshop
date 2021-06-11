from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.forms import SubscriberForm
from core.models import Profile, Subscriber
from core.serializers import SubscriberSerializer


def index_func(request):
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
        short_bio = profile.short_bio
        github_url = profile.github_url
        facebook_url = profile.facebook_url
        twitter_url = profile.twitter_url

        return render(
            request,
            "index.html",
            {
                "name": name,
                "form": form,
                "short_bio": short_bio,
                "github_url": github_url,
                "facebook_url": facebook_url,
                "twitter_url": twitter_url,
            },
        )

    def post(self, request):
        print(request.POST)
        print(request.POST.get("email"))

        form = SubscriberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("email"))

            email = form.cleaned_data.get("email")
            Subscriber.objects.create(email=email)

        profile = Profile.objects.get(id=1)
        name = profile.name
        short_bio = profile.short_bio
        github_url = profile.github_url
        facebook_url = profile.facebook_url
        twitter_url = profile.twitter_url

        return render(
            request,
            "index.html",
            {
                "name": name,
                "form": form,
                "short_bio": short_bio,
                "github_url": github_url,
                "facebook_url": facebook_url,
                "twitter_url": twitter_url,
            },
        )


class SubscriberAPIView(APIView):
    def get(self, request):
        # data = {
        #     "text": "Hello World!",
        # }
        # # {"text": "Hello World!"}
        # return JsonResponse(data)
        
        # subscriber = Subscriber.objects.first()
        # serializer = SubscriberSerializer(subscriber)

        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscribers, many=True)

        return Response(serializer.data)

    def post(self, request):
        print(request.data)

        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)