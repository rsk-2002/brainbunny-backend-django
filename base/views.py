from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from account.models import Profile
from quiz.models import UserRank
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

    leaderboard_users = UserRank.objects.order_by('rank')[:4]

    if request.user.is_authenticated:
        # request user
        user_object = User.objects.get(username=request.user)
        user_profile = Profile.objects.get(user=user_object)
        context = {"user_profile": user_profile, "leaderboard_users": leaderboard_users}
    else:
        context = {"leaderboard_users": leaderboard_users}

    return render(request, 'welcome.html', context)


@login_required(login_url="login")
def leaderboard_view(request):

    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)

    leaderboard_users = UserRank.objects.order_by('rank')

    context = {"leaderboard_users": leaderboard_users, "user_profile": user_profile}
    return render(request, "leaderboard.html", context)