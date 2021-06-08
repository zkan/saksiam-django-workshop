from django.contrib import admin

from core.models import Profile, Subscriber


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_bio",
        "github_url",
        "facebook_url",
        "twitter_url",
    )
    search_fields = (
        "name",
        "short_bio",
    )


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
    )
    search_fields = (
        "email",
    )
