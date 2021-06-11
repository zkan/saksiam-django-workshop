from django.test import TestCase

from core.models import Profile, Subscriber


class TestProfile(TestCase):
    def test_profile_should_have_defined_fields(self):
        profile = Profile.objects.create(
            name="Kan Ouivirach",
            short_bio="My short bio",
            github_url="https://github.com/zkan",
            facebook_url="https://www.facebook.com/zkan.cs",
            twitter_url="https://twitter.com/zkancs",
        )

        assert profile.name == "Kan Ouivirach"
        assert profile.short_bio == "My short bio"
        assert profile.github_url == "https://github.com/zkan"
        assert profile.facebook_url == "https://www.facebook.com/zkan.cs"
        assert profile.twitter_url == "https://twitter.com/zkancs"


class TestIndexView(TestCase):
    def test_index_view_should_see_my_name(self):
        # Given
        Profile.objects.create(name="Kan Ouivirach")

        # When
        response = self.client.get("/")

        # Then
        assert response.status_code == 200
        assert "Kan Ouivirach" in str(response.content)

    def test_index_view_should_save_subscriber_email_when_input_form(self):
        # Given
        Profile.objects.create(name="Kan Ouivirach")

        # When
        data = {"email": "kan@odds.team"}
        self.client.post("/", data=data)

        # Then
        subscriber = Subscriber.objects.last()
        assert subscriber.email == "kan@odds.team"
