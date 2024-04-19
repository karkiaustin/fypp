from django.shortcuts import render, redirect
from django.views import View

from home.forms import VehicleForm
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
import re
from django.db.models import Avg
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def custom_logout(request):
    logout(request)
    return redirect("/")


# Create your views here.
class Base(View):
    views = {}


class HomeView(Base):
    def get(self, request):
        self.views["category"] = Category.objects.all()
        self.views["ads"] = Ads.objects.all().order_by("rank")
        self.views["type"] = Type.objects.all()
        return render(request, "index.html", self.views)


class About(Base):
    def get(self, request):
        self.views["category"] = Category.objects.all()
        self.views["member"] = Member.objects.all()
        return render(request, "about.html", self.views)


class Blog(Base):
    def get(self, request):
        self.views["category"] = Category.objects.all()
        return render(request, "blog.html", self.views)


class BulkBidding(Base):
    def get(self, request):
        data = bulkbidding.objects.filter(user=request.user, is_accepted=False)
        comments = comment.objects.filter(bid__in=data)
        print(comments)
        return render(request, "bulkbidding.html", locals())

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        phone = request.POST["phone"]
        requirements = request.POST["requirements"]
        date = request.POST["date"]
        print(requirements)
        bid = bulkbidding.objects.create(
            user=request.user, Phone=phone, requirements=requirements, date=date
        )
        data = bulkbidding.objects.filter(user=request.user, is_accepted=False)
        return render(request, "bulkbidding.html", locals())


class BiddingComment(Base):
    def get(self, request):
        data = bulkbidding.objects.filter(is_accepted=False)
        comments = comment.objects.filter(bid__in=data).distinct
        return render(request, "admin/admin-home.html", locals())

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        bid = request.POST["id"]
        text = request.POST["text"]
        bid = comment.objects.create(user=request.user, bid_id=bid, text=text)
        data = bulkbidding.objects.filter(user=request.user, is_accepted=False)
        return render(request, "admin/admin-home.html", locals())


def bidconfirm(request, id):
    bid = bulkbidding.objects.get(pk=id)
    comments = comment.objects.get(bid_id=id)
    bid.is_accepted = True
    comments.is_accepted = True
    bid.save()
    comments.save()
    return redirect("/bulkbidding/")


def AddVehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle_instance = form.save(commit=False)
            vehicle_instance.vehicle_owner = request.user
            vehicle_instance.save()
            return redirect("/addvehicle")
    else:
        form = VehicleForm()
    return render(request, "admin/addvehicle.html", {"form": form})


class booking(Base):
    def get(self, request):
        comments = comment.objects.filter(is_accepted=True)
        vehicles = checkout.objects.filter(
            vehicle_description__vehicle_owner_id=request.user.id, is_completed=False
        )

        return render(request, "admin/admin-booking.html", locals())


class My_Account(Base):
    def get(self, request):
        self.views["category"] = Category.objects.all()
        user = User.objects.get(id=self.request.user.id)
        vehicles = checkout.objects.filter(user=self.request.user)
        if request.user.is_staff:
            vehicles = checkout.objects.filter(
                vehicle_description__vehicle_owner_id=self.request.user.id
            )
            return render(request, "admin/admin-account.html", locals())
        return render(request, "my account.html", locals())


class Service(Base):
    def get(self, request):
        self.views["category"] = Category.objects.all()
        return render(request, "service.html", self.views)


def Login(request):
    if request.method == "POST":
        user = request.POST["username"]
        passw = request.POST["password"]
        try:
            users = authenticate(request, username=user, password=passw)
            if users is not None:
                login(request, users)
                messages.success(request, "Successfully Logged In")
                if users.is_staff:
                    return redirect("/adminhome")
                return redirect("/")
            else:
                messages.error(request, "Username or password not correct")
                return redirect("/login")
        except:
            messages.error(request, "Username or password not correct")
            return redirect("/login")
    return render(request, "login.html")


def signup(request):
    category = Category.objects.all()
    context = {
        "category": category,  # Add categories to the context
    }
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        password_pattern = (
            r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        )

        if password == cpassword:
            if not re.match(password_pattern, password):
                messages.error(
                    request,
                    "Password must contain at least 8 characters, 1 special character, and 1 digit!",
                )
                return redirect("/signup")

            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!!")
                return redirect("/signup")

            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken!!")
                return redirect("/signup")

            else:
                data = User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    email=email,
                    username=username,
                    password=password,
                )
                messages.success(request, "User created successfully!!Enjoy")
                data.save()
        else:
            messages.error(request, "Password doesn't match!!")
            return redirect("/signup")

    return render(request, "signup.html", context)


def stafff(request):
    category = Category.objects.all()
    context = {
        "category": category,  # Add categories to the context
    }
    if request.method == "POST":
        First_name = request.POST["sfname"]
        Last_name = request.POST["slname"]
        email = request.POST["semail"]
        Cname = request.POST["Cname"]
        username = request.POST["susername"]
        password = request.POST["spassword"]
        company_document = request.FILES["Cdocument"]
        citizenship_document = request.FILES["Scitizenship"]
        password_pattern = (
            r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        )
        if not re.match(password_pattern, password):
            messages.error(
                request,
                "Password must contain at least 8 characters, 1 special character, and 1 digit!",
            )
            return redirect("/contact")

        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!!")
            return redirect("/contact")

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken!!")
            return redirect("/contact")

        else:
            users_details = User.objects.create_user(
                first_name=First_name,
                last_name=Last_name,
                email=email,
                username=username,
                password=password,
                is_staff=True,
            ).save()
            data = staff.objects.create(
                user=users_details,
                Company_name=Cname,
                Company_document=company_document,
                Citizenship_document=citizenship_document,
            )
            messages.success(
                request,
                "Your data is under review!!"
                "You will receive a mail after verification",
            )
            data.save()

    return render(request, "contact.html", context)


class Vehicle(Base):
    def get(self, request):
        self.views["vehicle"] = vehicle.objects.all()
        return render(request, "vehicle.html", self.views)


class CategoryView(Base):
    def get(self, request, slug):
        cat_id = Category.objects.get(slug=slug).id
        self.views["cat_products"] = vehicle.objects.filter(category_id=cat_id)
        self.views["category"] = Category.objects.all()

        return render(request, "category.html", self.views)


class TypeView(Base):
    def get(self, request, slug):
        type_id = Type.objects.get(slug=slug).id
        self.views["type_products"] = vehicle.objects.filter(type_id=type_id)
        self.views["category"] = Category.objects.all()

        return render(request, "type.html", self.views)


class VehicleView(Base):
    def get(self, request, slug):
        self.views["category"] = Category.objects.all()
        self.views["vehicle_detail"] = vehicle.objects.filter(slug=slug)
        self.views["review"] = User_review.objects.filter(slug=slug)

        return render(request, "vehicle detail.html", self.views)


class SearchView(Base):
    def get(self, request):
        if request.method == "GET":
            query = request.GET["query"]
            if query != "":
                self.views["search_vehicle"] = vehicle.objects.filter(
                    name__icontains=query
                )
            else:
                redirect("/")
        self.views["categories"] = Category.objects.all()
        return render(request, "search.html", self.views)


class StartCheckout(Base):
    def post(self, request, id):
        vehicle_id = id
        checkout_data = checkout.objects.create(
            vehicle_description_id=vehicle_id, user=self.request.user
        )
        return redirect("/checkout")


class CheckOutVehicle(Base):
    def get(self, request):
        checkoutdata = checkout.objects.filter(user=self.request.user)
        data = checkout.objects.filter(user=self.request.user, is_ordered=False).first
        return render(request, "checkout.html", locals())

    def post(self, request):
        name = request.POST["name"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        date = request.POST["sdate"]
        days = request.POST["days"]
        data = checkout.objects.get(user=self.request.user, is_ordered=False)
        data.name = name
        data.Phone = phone
        data.Address = address
        data.Start_date = date
        data.total_days = days
        data.is_ordered = True
        data.is_completed = False
        data.save()
        return redirect("/my_account")


def vehicle_review(request, slug):
    if vehicle.objects.filter(slug=slug):
        if request.method == "POST":
            username = request.user.username
            star = request.POST["star"]
            comment = request.POST["comment"]
            User_review.objects.create(
                username=username, star=star, review=comment, slug=slug
            ).save()
    else:
        return redirect(f"/detail/{slug}")
    return redirect(f"/detail/{slug}")


def updateprofile(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        user = User.objects.get(id=request.user.id)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect("/my_account/")
    return redirect("/my_account/")


def updatepaswword(request):
    if request.method == "POST":
        newpw = request.POST["newpw"]
        conf = request.POST["conpw"]
        if newpw == conf:
            user = User.objects.get(id=request.user.id)
            user.set_password(newpw)
            user.save()
            return redirect("/my_account/")
        else:
            return redirect("/my_account/")
    return redirect("/my_account/")

def booking_complete(request, id):
    if request.method == "POST":
        data = checkout.objects.get(id=id)
        data.is_completed = True
        data.save()
        return redirect("/my_account/")
       
    return redirect("/my_account/")