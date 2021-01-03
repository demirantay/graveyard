from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from home_app.models import Office, OfficeWorkers, Announcament
from profile_app.models import ProfileSettings
from desk_app.models import Desk, DeskWorkers, Article
from home_app.forms import NormalAccountForm, OfficeAccountForm
from home_app.forms import AnnouncamentForm, LoginGateForm


# HOME
# --------------------
# Desc: This is the index page of the app where the site gives information ab
#       -out it is services.
def home(request):
    return render(request, 'home_app/home.html', context=None)


# SIGN UP
# --------------------
# Desc: Signup page which consists of two forms since there will be two user
#       types one for office admin who will have total control and an admin p-
#       -age for it & a normal user who will join the office either with requ-
#       -est or with the code provided by the office admin(boss)
def signup(request):
    invalid_office_form_credits = False
    invalid_account_form_credits = False

    # Form Submission
    if request.method == 'POST':
        normal_account_form = NormalAccountForm(request.POST)
        if normal_account_form.is_valid():
            username = normal_account_form['username'].value()
            email = normal_account_form['email'].value()
            first_name = normal_account_form['first_name'].value()
            last_name = normal_account_form['last_name'].value()
            password = normal_account_form['password'].value()
            office_key = normal_account_form['office_key'].value()

            if User.objects.filter(username=username, email=email).exists():
                # Do nothing since there is a user already created
                invalid_account_form_credits = True
            else:
                if Office.objects.filter(secret_key=office_key).exists():
                    new_user = User(
                        username=username, email=email, first_name=first_name,
                        last_name=last_name, password=password
                    )
                    new_user.save()
                    # Now get the user from the db and assign it to the office
                    new_user = User.objects.get(username=username, email=email)
                    office = Office.objects.get(secret_key=office_key)
                    new_office_worker = OfficeWorkers(
                        user=new_user, joined_office=office
                    )
                    new_office_worker.save()
                    return HttpResponseRedirect('/home/login/')
                else:
                    # Do nothing
                    invalid_account_form_credits = True
    else:
        normal_account_form = NormalAccountForm()

    if request.method == 'POST':
        office_account_form = OfficeAccountForm(request.POST)
        if office_account_form.is_valid():
            office_name = office_account_form.cleaned_data['office_name']
            office_type = office_account_form.cleaned_data['office_type']
            username = office_account_form.cleaned_data['username']
            email = office_account_form.cleaned_data['email']
            first_name = office_account_form.cleaned_data['first_name']
            last_name = office_account_form.cleaned_data['last_name']
            password = office_account_form.cleaned_data['password']

            if Office.objects.filter(name=office_name).exists() or\
                    User.objects.filter(username=username).exists():
                # Do nothing since there is already an office
                invalid_office_form_credits = True
            else:
                # Create a new user
                new_user = User(
                    username=username, email=email, first_name=first_name,
                    last_name=last_name, password=password
                )
                new_user.save()
                # Create a new office with the new user as admin
                new_user = User.objects.get(username=username)
                new_office = Office(
                    admin=new_user, name=office_name, type=office_type
                )
                new_office.save()
                # Create a new office worker
                new_office = Office.objects.get(name=office_name)
                new_office_worker = OfficeWorkers(
                    user=new_user, joined_office=new_office
                )
                new_office_worker.save()
                return HttpResponseRedirect('/home/login/')
        else:
            invalid_office_form_credits = True
    else:
        office_account_form = OfficeAccountForm()

    data = {
        'invalid_office_form_credits': invalid_office_form_credits,
        'invalid_account_form_credits': invalid_account_form_credits,
        'normal_account_form': normal_account_form,
        'office_account_form': office_account_form,
    }
    return render(request, 'home_app/signup.html', context=data)


# LOGIN GATE
# ---------------------
# Desc: This is a gate that seperates staff members from curious eyes
def login_gate(request):
    invalid_user_credits = False

    if request.method == 'POST':
        login_form = LoginGateForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = User.objects.get(username=username, password=password)
            user_office = OfficeWorkers.objects.get(user=user)
            try:
                user_settings = ProfileSettings.objects.get(user=user)
            except ObjectDoesNotExist:
                user_settings = None

            if user is not None:
                login(request, user)
                if user_settings is not None:
                    return HttpResponseRedirect(
                        '/' + str(user_office.joined_office.name) +
                        '/home/dashboard/'
                    )
                else:
                    return HttpResponseRedirect(
                        '/' + str(user_office.joined_office.name) +
                        '/profile/settings/'
                    )
            else:
                invalid_user_credits = True
        else:
            invalid_user_credits = True
    else:
        login_form = LoginGateForm()
    data = {
        'invalid_user_credits': invalid_user_credits,
        'login_form': login_form,
    }
    return render(request, 'home_app/login_gate.html', context=data)


# DASHBOARD
# --------------------
# Desc: Home page showing the announcaments of every user
@login_required
def dashboard(request, officename):
    current_user = get_object_or_404(User, pk=request.user.id)
    current_office = Office.objects.get(name=officename)
    # Office Worker objects
    try:
        office_worker = OfficeWorkers.objects.get(user=current_user)
    except ObjectDoesNotExist:
        office_worker = None

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    # Announcament Create Mechanism
    if request.method == 'POST':
        announcament_form = AnnouncamentForm(request.POST)
        if announcament_form.is_valid():
            content = announcament_form.cleaned_data['content']
            new_announcament = Announcament(
                user=current_user, office=current_office, content=content,
                profile_settings=current_user_settings,
            )
            new_announcament.save()
    else:
        announcament_form = AnnouncamentForm()

    # Announcament Delete Mechanism
    if request.POST.get("announcament_delete_btn"):
        hidden_id = request.POST.get("hidden_id")
        announcament = Announcament.objects.filter(pk=hidden_id)
        announcament.delete()

    # Announcament Objects
    try:
        all_announcaments = Announcament.objects.order_by('-publish_date')
        office_announcaments = Announcament.objects.filter(
            office=current_office).order_by('-publish_date')
    except ObjectDoesNotExist:
        all_announcaments = None
        office_announcaments = None

    # Desk Objects
    try:
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        current_user_desks = None

    data = {
        'current_user': current_user,
        'current_office': current_office,
        'office_worker': office_worker,
        'has_home_navbar': True,
        'current_user_settings': current_user_settings,
        'announcament_form': announcament_form,
        'all_announcaments': all_announcaments,
        'current_user_desks': current_user_desks,
        'office_announcaments': office_announcaments,
    }
    return render(request, 'home_app/dashboard.html', context=data)


# DESK BROWSE
# ---------------------
# Desc: This is a page where you can create new desks(departments) for your
#       newspaper or browse some to join them
@login_required
def desk_browse(request, officename):
    current_user = get_object_or_404(User, pk=request.user.id)
    current_office = Office.objects.get(name=officename)
    # Office Worker objects
    try:
        office_worker = OfficeWorkers.objects.get(user=current_user)
    except ObjectDoesNotExist:
        office_worker = None
    invalid_desk_credits = False
    wrong_form_input = False

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    # Desk Create Mechanism
    if request.POST.get('desk_create_button'):
        desk_create_image = request.FILES.get('desk_create_image')
        desk_create_category = request.POST.get('desk_create_category')
        desk_create_category_color = request.POST.get('desk_create_category')
        desk_create_name = request.POST.get('desk_create_name')
        desk_create_desc = request.POST.get('desk_create_desc')
        if Desk.objects.filter(name=desk_create_name, office=current_office,
                               category=desk_create_category).exists():
            # Do nothing
            invalid_desk_credits = True
        elif desk_create_image is None:
            # Do nothing
            wrong_form_input = True
        else:
            new_desk = Desk(
                sub_editor=current_user, image=desk_create_image,
                category=desk_create_category, name=desk_create_name,
                description=desk_create_desc, office=current_office,
                category_color=desk_create_category_color,
            )
            new_desk.save()

    # Joining a desk mechanism
    if request.POST.get('join_desk_button'):
        worker_that_joined = current_user
        hidden_name = request.POST.get('hidden_value')
        joined_desk = Desk.objects.get(pk=hidden_name)

        try:
            DeskWorkers.objects.get(
                worker=worker_that_joined, joined_desk=joined_desk
            )
            # if it exists Do nothing
        except ObjectDoesNotExist:
            new_worker = DeskWorkers(
                worker=worker_that_joined, joined_desk=joined_desk
            )
            new_worker.save()

    #  Desk objects
    try:
        all_desks = Desk.objects.order_by('-creation_date')
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        all_desks = None
        current_user_desks = None

    data = {
        'current_user': current_user,
        'current_office': current_office,
        'office_worker': office_worker,
        'invalid_desk_credits': invalid_desk_credits,
        'wrong_form_input': wrong_form_input,
        'has_home_navbar': True,
        'current_user_settings': current_user_settings,
        'all_desks': all_desks,
        'current_user_desks': current_user_desks,
    }
    return render(request, 'home_app/desk_browse.html', context=data)


# SEARCH
# ----------
# Desc: A search page for the requested articles by the authors @username
@login_required
def search(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    filtered_user_articles = None
    # Search Mechanism
    if request.GET.get("search_submit_btn"):
        username = request.GET.get('search_name')
        user = get_object_or_404(User, username=username)
        try:
            filtered_user_articles = Article.objects.filter(author=user)\
                .order_by('-publish_date')
        except ObjectDoesNotExist:
            filtered_user_articles = None

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    #  Desk objects
    try:
        all_desks = Desk.objects.order_by('-creation_date')
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        all_desks = None
        current_user_desks = None

    data = {
        'current_user': current_user,
        'has_home_navbar': True,
        'current_user_settings': current_user_settings,
        'all_desks': all_desks,
        'current_user_desks': current_user_desks,
        'filtered_user_articles': filtered_user_articles,
    }
    return render(request, 'home_app/search.html', context=data)


# PUBLISH
# -----------
# Desc: Page that has all of the finished articles that are ready to publish
@login_required
def publish(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # All articles
    try:
        all_articles = Article.objects.filter(pushed_to_publish=True)\
            .order_by('-publish_date')
    except ObjectDoesNotExist:
        all_articles = None

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    #  Desk objects
    try:
        all_desks = Desk.objects.order_by('-creation_date')
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        all_desks = None
        current_user_desks = None

    data = {
        'current_user': current_user,
        'has_home_navbar': True,
        'current_user_settings': current_user_settings,
        'all_desks': all_desks,
        'current_user_desks': current_user_desks,
        'all_articles': all_articles,
    }
    return render(request, 'home_app/publish.html', context=data)
