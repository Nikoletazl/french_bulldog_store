
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, ListView, UpdateView, DeleteView

from french_bulldog_store.auth_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from french_bulldog_store.auth_app.models import Customer, FrenchieUser
from french_bulldog_store.web.models import Product, Order


class UserRegistrationView(CreateView):
    form_class = CreateProfileForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items

        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']


        context.update({
            'cart_items': cart_items,
        })

        return context


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items

        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']


        context.update({
            'cart_items': cart_items,
        })

        return context


class UserLogoutView(LogoutView):
    pass



class ProductCreateView(UserPassesTestMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'admin/product_create.html'
    success_url = reverse_lazy('store')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items

        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']


        context.update({
            'cart_items': cart_items,
        })

        return context


class ProductEditView(UserPassesTestMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'admin/product_edit.html'
    success_url = reverse_lazy('store')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items

        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']


        context.update({
            'cart_items': cart_items,
        })

        return context


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    fields = '__all__'
    template_name = 'admin/product_delete.html'
    success_url = reverse_lazy('store')

    def test_func(self):
        return self.request.user.is_staff


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items

        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']


        context.update({
            'cart_items': cart_items,
        })

        return context


class Profile(DetailView):
    model = Customer
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items

        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']


        context.update({
            'cart_items': cart_items,
        })

        return context


class EditProfileView(UpdateView):
    model = Customer
    form_class = EditProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items

        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']


        context.update({
            'cart_items': cart_items,
        })

        return context


class DeleteProfileView(DeleteView):
    model = FrenchieUser
    form_class = DeleteProfileForm
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items

        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']


        context.update({
            'cart_items': cart_items,
        })

        return context



