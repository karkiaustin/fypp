from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
import re
from django.db.models import Avg
from django.contrib.auth import logout
from django.shortcuts import redirect


def custom_logout(request):
    logout(request)
    return redirect('/')


# Create your views here.
class Base(View):
    views = {}


class HomeView(Base):
    def get(self, request):
        self.views['category'] = Category.objects.all()
        self.views['ads'] = Ads.objects.all().order_by('rank')
        self.views['type'] = Type.objects.all()
        return render(request, 'index.html', self.views)


class About(Base):
    def get(self, request):
        self.views['category'] = Category.objects.all()
        self.views['member'] = Member.objects.all()
        return render(request, 'about.html', self.views)


class Blog(Base):
    def get(self, request):
        self.views['category'] = Category.objects.all()
        return render(request, 'blog.html', self.views)


class BulkBidding(Base):
    def get(self, request):
        self.views['category'] = Category.objects.all()
        return render(request, 'bulkbidding.html', self.views)


class CheckOut(Base):
    def get(self, request):
        self.views['category'] = Category.objects.all()
        return render(request, 'checkout.html', self.views)


class My_Account(Base):
    def get(self, request):
        self.views['category'] = Category.objects.all()
        return render(request, 'my account.html', self.views)


class Service(Base):
    def get(self, request):
        self.views['category'] = Category.objects.all()
        return render(request, 'service.html', self.views)


def signup(request):
    category = Category.objects.all()
    context = {
        'category': category,  # Add categories to the context
    }
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

        if password == cpassword:
            if not re.match(password_pattern, password):
                messages.error(request,
                               "Password must contain at least 8 characters, 1 special character, and 1 digit!")
                return redirect('/signup')

            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!!")
                return redirect('/signup')

            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken!!")
                return redirect('/signup')

            else:
                data = User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    email=email,
                    username=username,
                    password=password
                )
                messages.success(request, "User created successfully!!Enjoy")
                data.save()
        else:
            messages.error(request, "Password doesn't match!!")
            return redirect('/signup')

    return render(request, 'signup.html', context)


def stafff(request):
    category = Category.objects.all()
    context = {
        'category': category,  # Add categories to the context
    }
    if request.method == "POST":
        First_name = request.POST['sfname']
        Last_name = request.POST['slname']
        email = request.POST['semail']
        Cname = request.POST['Cname']
        username = request.POST['susername']
        password = request.POST['spassword']
        company_document = request.FILES['Cdocument']
        citizenship_document = request.FILES['Scitizenship']
        password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        if not re.match(password_pattern, password):
            messages.error(request,
                           "Password must contain at least 8 characters, 1 special character, and 1 digit!")
            return redirect('/contact')

        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!!")
            return redirect('/contact')

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken!!")
            return redirect('/contact')

        else:
            data = staff.objects.create(
                First_name=First_name,
                Last_name=Last_name,
                Email=email,
                Username=username,
                Password=password,
                Company_name=Cname,
                Company_document=company_document,
                Citizenship_document=citizenship_document
            )
            messages.success(request, "Your data is under review!!"
                                      "You will receive a mail after verification")

            data.save()

    return render(request, 'contact.html', context)


class Vehicle(Base):
    def get(self, request):
        self.views['vehicle'] = vehicle.objects.all()
        return render(request, 'vehicle.html', self.views)


class CategoryView(Base):
    def get(self, request, slug):
        cat_id = Category.objects.get(slug=slug).id
        self.views['cat_products'] = vehicle.objects.filter(category_id=cat_id)
        self.views['category'] = Category.objects.all()

        return render(request, 'category.html', self.views)


class TypeView(Base):
    def get(self, request, slug):
        type_id = Type.objects.get(slug=slug).id
        self.views['type_products'] = vehicle.objects.filter(type_id=type_id)
        self.views['category'] = Category.objects.all()

        return render(request, 'type.html', self.views)


class VehicleView(Base):
    def get(self, request, slug):
        self.views['category'] = Category.objects.all()
        self.views['vehicle_detail'] = vehicle.objects.filter(slug=slug)
        self.views['review'] = User_review.objects.filter(slug=slug)

        return render(request, 'vehicle detail.html', self.views)


class SearchView(Base):
    def get(self, request):
        if request.method == 'GET':
            query = request.GET['query']
            if query != "":
                self.views['search_vehicle'] = vehicle.objects.filter(name__icontains=query)
            else:
                redirect('/')
        self.views['categories'] = Category.objects.all()
        return render(request, 'search.html', self.views)


def CheckOutVehicle(request, slug):
    category = Category.objects.all()
    context = {
        'category': category,  # Add categories to the context
    }
    username = request.user.username

    return redirect('/checkout', context)


def vehicle_review(request, slug):
    if vehicle.objects.filter(slug=slug):
        if request.method == 'POST':
            username = request.user.username
            star = request.POST['star']
            comment = request.POST['comment']
            User_review.objects.create(
                username=username,
                star=star,
                review=comment,
                slug=slug
            ).save()
    else:
        return redirect(f'/detail/{slug}')
    return redirect(f'/detail/{slug}')
