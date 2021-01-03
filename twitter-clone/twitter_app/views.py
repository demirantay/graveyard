from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import ProfileSettingsModel, TweetModel, FollowModel, RetweetModel
from .forms import SignupForm, LoginForm, ProfileSettingsForm, TweetForm
from .forms import SearchForm
from io import BytesIO
from PIL import Image
import random
import cloudinary.uploader



# Index Page
# ---------------
# Desc: Page displaying why you shall signup.You cannot pass this dipslay unles
#       you signup or login. It is the gate that seperates our users from anons
def index(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = signup_form['username'].value()
            password = signup_form['password'].value()
            email = signup_form['email'].value()
            new_user = User.objects.create_user(username=username, email=email,
                                                password=password,)
            settings_model = ProfileSettingsModel(user=new_user)
            settings_model.save()
            return HttpResponseRedirect('/thanks/')
    # For get requests for the first time to get a blank form.
    else:
        login_form = LoginForm()
        signup_form = SignupForm()

    return render(request, 'index.html', context={'signup_form': signup_form,
                                                  'login_form': login_form,
                                                  'has_navbar': False, })


# Thanks Page
# --------------
# Desc: This page appears after the user has completed the sign up form
def thanks(request):
    return render(request, 'thanks.html', context={'has_navbar': False, })


# Profile Page
# ---------------
# Desc: displayingy the users bio, name , links, tweets, suggestion box for its
#       followers, trends box for displaying most clicked '#'s
@login_required
def profile(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # Settings Objects
    try:
        current_user_settings = ProfileSettingsModel.objects.get(
            user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    # Search Mechanism
    # Desc: Searches for the users
    filtered_db_user = None
    filtered_db_user_settings = None
    search_form = SearchForm(request.GET)
    if request.method == 'GET':
        if search_form.is_valid():
            key_word = search_form['key_word'].value()
            try:
                filtered_db_user = User.objects.get(username=key_word)
                filtered_db_user_settings = ProfileSettingsModel.objects.get(
                    user=filtered_db_user)
            except ObjectDoesNotExist:
                filtered_db_user = None
                filtered_db_user_settings = None

    # Tweet Mechanism
    # Desc: These are These are 280 charater entires and updates you make.
    tweet_form = TweetForm(request.POST)
    if request.method == 'POST':
        if tweet_form.is_valid():
            tweet_content = tweet_form['tweet_content'].value()
            new_tweet_model = TweetModel.objects.create(
                user=current_user, tweet_content=tweet_content)
            new_tweet_model.save()
            return HttpResponseRedirect('/profile/')
        else:
            tweet_form = TweetForm()
    # Tweet Objects
    current_user_tweets_count = 0
    try:
        current_user_tweets = TweetModel.objects.filter(user=current_user)\
            .order_by('-publish_date')
        current_user_tweets_count = current_user_tweets.count()
    except ObjectDoesNotExist:
        current_user_tweets = None
        current_user_tweets_count = 0

    # Like mechanism
    # Desc: Liking each tweet, and there is a count that dispalys it
    if request.POST.get('like_button'):
        hidden_value = request.POST.get('hidden_tweet_value')
        current_tweet = TweetModel.objects.get(
            user=current_user, pk=hidden_value)
        current_tweet.tweet_likes += 1
        current_tweet.save()

    # Retweet mechanism
    # Desc: Retweeting each tweet means posting their post on your profile
    if request.POST.get('retweet_button'):
        tweet_id = request.POST.get('hidden_retweet_value')
        current_tweet = TweetModel.objects.get(pk=tweet_id)
        current_tweet.tweet_retweets += 1
        current_tweet.save()
        new_retweet = RetweetModel(user=current_user, retweet=current_tweet, retweet_settings=ProfileSettingsModel.objects.get(user=current_tweet.user))
        new_retweet.save()
    # retweet mechanism objects
    retweets = RetweetModel.objects.filter(user=current_user).order_by('-retweet_date')[:50]

    # Retweet like mechanism
    if request.POST.get('retweet_like_button'):
        tweet_id = request.POST.get('hidden_retweet_value')
        current_tweet = TweetModel.objects.get(pk=tweet_id)
        current_tweet.tweet_likes += 1
        current_tweet.save()

    # Follow mechanism objects
    try:
        current_user_followings = FollowModel.objects.filter(follower=current_user)
        current_user_followings_for_suggestion = FollowModel.objects.filter(follower=current_user)[:5]
        current_user_followings_count = current_user_followings.count()
        current_user_followings_settings = []
        for i in range(current_user_followings_for_suggestion.count()):
            current_user_followings_settings\
                .append(ProfileSettingsModel.objects.get(user=current_user_followings[i].followed))
        current_user_followers = FollowModel.objects.filter(
            followed=current_user)
        current_user_followers_count = current_user_followers.count()
    except ObjectDoesNotExist:
        current_user_followings = None
        current_user_followings_count = 0
        current_user_followings_settings = []
        current_user_followers = None
        current_user_followers_count = 0
    return render(request, 'profile.html', context={'current_user': current_user,
                                                    'has_navbar': True,
                                                    'current_user_settings': current_user_settings,
                                                    'search_form': search_form,
                                                    'filtered_db_user': filtered_db_user,
                                                    'filtered_db_user_settings': filtered_db_user_settings,
                                                    'tweet_form': tweet_form,
                                                    'current_user_tweets': current_user_tweets,
                                                    'current_user_tweets_count': current_user_tweets_count,
                                                    'current_user_followings': current_user_followings,
                                                    'current_user_followings_count': current_user_followings_count,
                                                    'current_user_followers': current_user_followers,
                                                    'current_user_followers_count': current_user_followers_count,
                                                    'current_user_followings_settings': current_user_followings_settings,
                                                    'following_data': zip(current_user_followings_for_suggestion, current_user_followings_settings),
                                                    'retweets': retweets,
                                                    })


# Settings Page
# ---------------
# Desc: change the settings of your profile such as your bio, chosen name, etc.
@login_required
def profile_settings(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # Search mechanism
    # Desc: Searches for the user
    search_form = SearchForm(request.GET)
    filtered_db_user = None
    filtered_db_user_settings = None
    if request.method == 'GET':
        if search_form.is_valid():
            key_word = search_form['key_word'].value()
            try:
                filtered_db_user = User.objects.get(username=key_word)
                filtered_db_user_settings = ProfileSettingsModel.objects.get(
                    user=filtered_db_user)
            except ObjectDoesNotExist:
                filtered_db_user = None
                filtered_db_user_settings = None


    if request.method == 'POST':
        settings_form = ProfileSettingsForm(request.POST, request.FILES)
        settings_model = ProfileSettingsModel.objects.get(user=current_user)
        if settings_form.is_valid():
            #settings_model.profile_photo = settings_form.cleaned_data['profile_photo']
            settings_model.profile_photo = cloudinary.uploader.upload_resource(settings_form.cleaned_data['profile_photo'])
            #image_file = BytesIO(photo)
            #image = Image.open(image_file)
            #image = image.resize((230, 230))
            #image_file = BytesIO()
            settings_model.first_name = settings_form['first_name'].value()
            settings_model.bio = settings_form['bio'].value()
            settings_model.location = settings_form['location'].value()
            settings_model.personal_link = settings_form['personal_link'].value(
            )
            settings_model.save()
            return HttpResponseRedirect('/profile/')
    else:
        settings_form = ProfileSettingsForm()
    return render(request, 'profile_settings_page.html', context={'current_user': current_user,
                                                                  'has_navbar': True,
                                                                  'settings_form': settings_form,
                                                                  'search_form': search_form,
                                                                  'filtered_db_user': filtered_db_user,
                                                                  'filtered_db_user_settings': filtered_db_user_settings,
                                                                  })


# Other User Profile Page
# --------------
# Desc: Shows the other user profile pages. All functionality is same, yet it
#       has `follow` instead of `tweet`
@login_required
def other_user_profile(request, username):
    current_user = get_object_or_404(User, pk=request.user.id)
    other_user = get_object_or_404(User, username=username)

    # other user settings objects
    try:
        other_user_settings = ProfileSettingsModel.objects.get(user=other_user)
    except ObjectDoesNotExist:
        other_user_settings = None

    # Search mechanism
    # Desc: Searches for the users
    search_form = SearchForm(request.GET)
    filtered_db_user = None
    filtered_db_user_settings = None
    if request.method == 'GET':
        if search_form.is_valid():
            key_word = search_form['key_word'].value()
            try:
                filtered_db_user = User.objects.get(username=key_word)
                filtered_db_user_settings = ProfileSettingsModel.objects.get(
                    user=filtered_db_user)
            except ObjectDoesNotExist:
                filtered_db_user = None
                filtered_db_user_settings = None

    # Tweet objects
    other_user_tweets_count = 0
    try:
        other_user_tweets = TweetModel.objects.filter(user=other_user)\
            .order_by('-publish_date')
        other_user_tweets_count = other_user_tweets.count()
    except ObjectDoesNotExist:
        other_user_tweets = None
        other_user_tweets_count = 0

    # Like mechanism
    # Desc: Liking each tweet, and there is a count that dispalys it
    if request.POST.get('like_button_other_profiles'):
        hidden_value = request.POST.get('hidden_tweet_value')
        current_tweet = TweetModel.objects.get(
            user=other_user, pk=hidden_value)
        current_tweet.tweet_likes += 1
        current_tweet.save()

    # Retweet other user objects
    retweets = RetweetModel.objects.filter(user=other_user).order_by('-retweet_date')[:50]



    # Follow mechanism
    # Desc: Allows you to follow users and have their tweets on your feed
    if request.POST.get('follow_button'):
        if FollowModel.objects.filter(follower=current_user,
                                      followed=other_user) .exists():
            pass  # Do not save a model if it already exists.
        else:
            follow_instance = FollowModel(
                follower=current_user, followed=other_user)
            follow_instance.save()
    # Follow mechanism objects
    try:
        other_user_followings = FollowModel.objects.filter(follower=other_user)[
            :5]
        other_user_followings_count = other_user_followings.count()
        other_user_followings_settings = []
        for i in range(other_user_followings_count):
            other_user_followings_settings\
                .append(ProfileSettingsModel.objects.get(user=other_user_followings[i].followed))
        other_user_followers = FollowModel.objects.filter(followed=other_user)
        other_user_followers_count = other_user_followers.count()
    except ObjectDoesNotExist:
        other_user_followings = None
        other_user_followings_count = 0
        other_user_followings_settings = []
        other_user_followers = None
        other_user_followers_count = 0

    return render(request, 'other_user_profile.html', context={'current_user': current_user,
                                                               'other_user': other_user,
                                                               'has_navbar': True,
                                                               'other_user_settings': other_user_settings,
                                                               'search_form': search_form,
                                                               'filtered_db_user': filtered_db_user,
                                                               'filtered_db_user_settings': filtered_db_user_settings,
                                                               'other_user_tweets': other_user_tweets,
                                                               'other_user_tweets_count': other_user_tweets_count,
                                                               'other_user_followings': other_user_followings,
                                                               'other_user_followings_count': other_user_followings_count,
                                                               'other_user_followers': other_user_followers,
                                                               'other_user_followers_count': other_user_followers_count,
                                                               'other_user_followings_settings': other_user_followings_settings,
                                                               'following_data': zip(other_user_followings, other_user_followings_settings),
                                                               'retweets': retweets,
                                                               })


# Follow-info Page
# --------------
# Desc: Gives the follower and following info about each of the profilesself.
#       Following is like subscribing to that users feed.
@login_required
def follow_info(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # Search mechanism
    # Desc: Searches for the user
    search_form = SearchForm(request.GET)
    filtered_db_user = None
    filtered_db_user_settings = None
    if request.method == 'GET':
        if search_form.is_valid():
            key_word = search_form['key_word'].value()
            try:
                filtered_db_user = User.objects.get(username=key_word)
                filtered_db_user_settings = ProfileSettingsModel.objects.get(
                    user=filtered_db_user)
            except ObjectDoesNotExist:
                filtered_db_user = None
                filtered_db_user_settings = None

    # Following objects
    try:
        current_user_followings = FollowModel.objects.filter(
            follower=current_user)
        current_user_followings_count = current_user_followings.count()
        current_user_followings_settings = []
        for i in range(current_user_followings_count):
            current_user_followings_settings\
                .append(ProfileSettingsModel.objects.get(user=current_user_followings[i].followed))
        current_user_followers = FollowModel.objects.filter(
            followed=current_user)
        current_user_followers_count = current_user_followers.count()
        current_user_followers_settings = []
        for i in range(current_user_followers_count):
            current_user_followers_settings\
                .append(ProfileSettingsModel.objects.get(user=current_user_followers[i].follower))
    except ObjectDoesNotExist:
        current_user_followings = None
        current_user_followings_count = 0
        current_user_followings_settings = []
        current_user_followers_count = 0
        current_user_followers = None
        current_user_followers_settings = []

    return render(request, 'follow_info.html', context={'has_navbar': True,
                                                        'current_user': current_user,
                                                        'search_form': search_form,
                                                        'filtered_db_user': filtered_db_user,
                                                        'filtered_db_user_settings': filtered_db_user_settings,
                                                        'current_user_followings': current_user_followings,
                                                        'current_user_followings_count': current_user_followings_count,
                                                        'current_user_followers': current_user_followers,
                                                        'current_user_followers_count': current_user_followers_count,
                                                        'current_user_followings_settings': current_user_followings_settings,
                                                        'current_user_followers_settings': current_user_followers_settings,
                                                        'following_data': zip(current_user_followings, current_user_followings_settings),
                                                        'follower_data': zip(current_user_followers, current_user_followers_settings),
                                                        })

# Follow Page for other users
# -----------------
# Desc: Gives the follower and following info about each of the profilesself.
#       Following is like subscribing to that users feed.
@login_required
def other_user_follow_info(request, username):
    current_user = get_object_or_404(User, pk=request.user.id)
    other_user = get_object_or_404(User, username=username)

    # Search mechanism
    # Desc: Searches for the user
    search_form = SearchForm(request.GET)
    filtered_db_user = None
    filtered_db_user_settings = None
    if request.method == 'GET':
        if search_form.is_valid():
            key_word = search_form['key_word'].value()
            try:
                filtered_db_user = User.objects.get(username=key_word)
                filtered_db_user_settings = ProfileSettingsModel.objects.get(
                    user=filtered_db_user)
            except ObjectDoesNotExist:
                filtered_db_user = None
                filtered_db_user_settings = None

    # Following objects
    try:
        other_user_followings = FollowModel.objects.filter(follower=other_user)
        other_user_followings_count = other_user_followings.count()
        other_user_followings_settings = []
        for i in range(other_user_followings_count):
            other_user_followings_settings\
                .append(ProfileSettingsModel.objects.get(user=other_user_followings[i].followed))
        other_user_followers = FollowModel.objects.filter(followed=other_user)
        other_user_followers_count = other_user_followers.count()
        other_user_followers_settings = []
        for i in range(other_user_followers_count):
            other_user_followers_settings\
                .append(ProfileSettingsModel.objects.get(user=other_user_followers[i].follower))
    except ObjectDoesNotExist:
        other_user_followings = None
        other_user_followings_count = 0
        other_user_followings_settings = []
        other_user_followers_count = 0
        other_user_followers = None
        other_user_followers_settings = []

    return render(request, 'other_user_follow_info.html', context={'has_navbar': True,
                                                                   'current_user': current_user,
                                                                   'other_user': other_user,
                                                                   'search_form': search_form,
                                                                   'filtered_db_user': filtered_db_user,
                                                                   'filtered_db_user_settings': filtered_db_user_settings,
                                                                   'other_user_followings': other_user_followings,
                                                                   'other_user_followings_count': other_user_followings_count,
                                                                   'other_user_followers': other_user_followers,
                                                                   'other_user_followers_count': other_user_followers_count,
                                                                   'other_user_followings_settings': other_user_followings_settings,
                                                                   'other_user_followers_settings': other_user_followers_settings,
                                                                   'following_data': zip(other_user_followings, other_user_followings_settings),
                                                                   'follower_data': zip(other_user_followers, other_user_followers_settings),
                                                                  })


# Home Page
# ------------
# Desc: A chronological collection of tweets of the users you follow displayed
@login_required
def home(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # Settings Objects
    try:
        current_user_settings = ProfileSettingsModel.objects.get(
            user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    # Tweet Mechanism
    # Desc: These are These are 280 charater entires and updates you make.
    if request.POST.get('home_tweet_submit'):
        content = request.POST.get('tweet_content')
        tweet_instance = TweetModel(user=current_user, tweet_content=content)
        tweet_instance.save()
        return HttpResponseRedirect('/profile/')
    # Tweet Objects
    # Tweet Objects
    current_user_tweets_count = 0
    try:
        current_user_tweets = TweetModel.objects.filter(user=current_user)\
            .order_by('-publish_date')
        current_user_tweets_count = current_user_tweets.count()
    except ObjectDoesNotExist:
        current_user_tweets = None
        current_user_tweets_count = 0

    # Like mechanism
    # Desc: Liking each tweet, and there is a count that dispalys it
    if request.POST.get('like_button'):
        hidden_value = request.POST.get('hidden_tweet_value')
        current_tweet = TweetModel.objects.get(pk=hidden_value)
        current_tweet.tweet_likes += 1
        current_tweet.save()

    # Retweet mechanism
    # Desc: Retweeting each tweet means posting their post on your profile
    if request.POST.get('retweet_button'):
        tweet_id = request.POST.get('hidden_retweet_value')
        current_tweet = TweetModel.objects.get(pk=tweet_id)
        current_tweet.tweet_retweets += 1
        current_tweet.save()
        new_retweet = RetweetModel(user=current_user, retweet=current_tweet, retweet_settings=ProfileSettingsModel.objects.get(user=current_tweet.user))
        new_retweet.save()

    # Search mechanism
    # Desc: Searches for the user
    search_form = SearchForm(request.GET)
    filtered_db_user = None
    filtered_db_user_settings = None
    if request.method == 'GET':
        if search_form.is_valid():
            key_word = search_form['key_word'].value()
            try:
                filtered_db_user = User.objects.get(username=key_word)
                filtered_db_user_settings = ProfileSettingsModel.objects.get(
                    user=filtered_db_user)
            except ObjectDoesNotExist:
                filtered_db_user = None
                filtered_db_user_settings = None


    # Follow mechanism objects
    following = User.objects.filter(followed__follower = current_user)
    following = User.objects.select_related('ProfileSettingsModel').filter(followed__follower = current_user)
    #home_feed = TweetModel.objects.filter(user__in=following).order_by('-publish_date')[:100]

    home_feed_tweets = TweetModel.objects.filter(
        user__followed__follower=request.user.id
    ).select_related('user', 'user__settings').order_by('-publish_date')[:100]

    try:
        current_user_followings = FollowModel.objects.filter(follower=current_user)
        current_user_followers = FollowModel.objects.filter(followed=current_user)
        current_user_followings_count = current_user_followings.count()
        current_user_followers_count = current_user_followers.count()
        current_user_followings_settings = []
        for i in range(current_user_followings_count):
            current_user_followings_settings\
                .append(ProfileSettingsModel.objects.get(user=current_user_followings[i].followed))
    except ObjectDoesNotExist:
        current_user_followings = None
        current_user_followings_count = 0
        current_user_followers = None
        current_user_followers_count = 0
        current_user_followings_settings = []

    # Random follow suggestions
    all_settings = ProfileSettingsModel.objects.all()
    all_settings_count = all_settings.count()

    random_settings_1 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_2 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_3 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_4 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_5 = all_settings[random.randint(1, all_settings_count-1)]

    return render(request, 'home.html', context={'has_navbar': True,
                                                 'current_user': current_user,
                                                 'current_user_settings': current_user_settings,
                                                 'current_user_tweets':current_user_tweets,
                                                 'current_user_tweets_count': current_user_tweets_count,
                                                 'search_form': search_form,
                                                 'filtered_db_user': filtered_db_user,
                                                 'filtered_db_user_settings': filtered_db_user_settings,
                                                 'current_user_followings': current_user_followings,
                                                 'current_user_followers': current_user_followers,
                                                 'current_user_followings_count': current_user_followings_count,
                                                 'current_user_followers_count': current_user_followers_count,
                                                 'current_user_followings_settings': current_user_followings_settings,
                                                 'following': following,
                                                 'home_feed_tweets': home_feed_tweets,
                                                 'random_settings_1':random_settings_1,
                                                 'random_settings_2':random_settings_2,
                                                 'random_settings_3':random_settings_3,
                                                 'random_settings_4':random_settings_4,
                                                 'random_settings_5':random_settings_5,
                                                 })


# Explore page
# -------------
# Desc: displays users to follow, look and explore
@login_required
def explore(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # Search mechanism
    # Desc: Searches for the user
    search_form = SearchForm(request.GET)
    filtered_db_user = None
    filtered_db_user_settings = None
    if request.method == 'GET':
        if search_form.is_valid():
            key_word = search_form['key_word'].value()
            try:
                filtered_db_user = User.objects.get(username=key_word)
                filtered_db_user_settings = ProfileSettingsModel.objects.get(
                    user=filtered_db_user)
            except ObjectDoesNotExist:
                filtered_db_user = None
                filtered_db_user_settings = None

    # Settings objects
    all_settings = ProfileSettingsModel.objects.all()
    all_settings_count = all_settings.count()

    random_settings_1 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_2 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_3 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_4 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_5 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_6 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_7 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_8 = all_settings[random.randint(1, all_settings_count-1)]
    random_settings_9 = all_settings[random.randint(1, all_settings_count-1)]


    return render(request, 'explore.html', context={'has_navbar': True,
                                                    'current_user': current_user,
                                                    'search_form': search_form,
                                                    'filtered_db_user': filtered_db_user,
                                                    'filtered_db_user_settings': filtered_db_user_settings,
                                                    'random_settings_1':random_settings_1,
                                                    'random_settings_2':random_settings_2,
                                                    'random_settings_3':random_settings_3,
                                                    'random_settings_4':random_settings_4,
                                                    'random_settings_5':random_settings_5,
                                                    'random_settings_6':random_settings_6,
                                                    'random_settings_7':random_settings_7,
                                                    'random_settings_8':random_settings_8,
                                                    'random_settings_9':random_settings_9,
                                                    })





# ------------------------------
# Self notes for the future: of this project

# I have finished the prototype 1.0 however the code is very very bad.
# 1- The most important thing i need to change is how i query my models.
# 2- change the name of the models and change their foreing key structuresself.
#    having `null=True` is a very dangerous thing to have in the foreingkeys
# 3- Well the UI is litteraly terrible that needs to be fixed. The repsonsivnes
#    of the site is the ugliest thing i ve seen in a while
# 4- I am using the same mechanisms for the forms on the each view. I need to
#    change that to having a view just for the form and point out that specific
#    form view at each of your forms in the templates
# 5- The seearch mecnhanism isnt even using ajax. I need to refresh the page to
#    see what results i get from the query. I hate it.
# 6 - And lastly before i forget the tweet home feed needs ajax. to let the
#    new tweets keep coming.
# 7- The home page and the exlpre page will not work on the local host if the
#    user does not create content. I am manually creating content at the beg
#    beginig since we have random_settings queries they will break if there is
#    nothing in the array for settings.
# 8- I still dont know which sql to use and how to use it. For the sake of
#    heroku i will go along with postgresql for now but i may change it.
# 9- there is a scaling problem each time a user submit a tweet the site will
#    become slower and slower. I couldnt find a soulition to that since this
#    is my first django project and im a beginnerself.
# 10- most of the algorithms such as , follow suggestions, explore page does
#     not use any kind of sessions or algorithms they are coded very poorly
#     which is not the best use for optimsiation problems that i will have in
#     future ....

# Yet, I am probably not going to use or waste my time on this project, at
# least not for a long time because this was just a learning experience.
