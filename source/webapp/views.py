from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, FormView

from webapp.forms import ProductForm, ReviewForm
from webapp.models import Product, Review


# Create your views here.

class ProductIndexView(ListView):
    template_name = 'product/product_view.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['review_form'] = ReviewForm()
        return context


class ProductDetail(TemplateView):
    template_name = 'product/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=kwargs['pk'])
        return context


class CreateProduct(LoginRequiredMixin, View):
    template_name = 'product/product_add.html'

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request, 'product/product_add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if not form.is_valid():
            return render(request, 'product/product_add.html', {'form': form})
        else:
            tracker = form.save()
            return redirect('product_detail', pk=tracker.pk)


class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class DeleteProduct(LoginRequiredMixin, DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    success_url = reverse_lazy('index')


class ReviewView(LoginRequiredMixin, FormView):
    form_class = ReviewForm

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            grade = form.cleaned_data.get('grade')
            author = request.user
            if not Review.objects.filter(author=author, product=product).exists():
                Review.objects.create(author=author, product=product, text=text, grade=grade)
                messages.success(request, 'Отзыв добавлен')
        return redirect('index')


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'review/review_update.html'
    model = Review
    form_class = ReviewForm

    def dispatch(self, request, *args, **kwargs):
        review = self.get_object()
        if request.user != review.author:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        review = Review.objects.get(pk=self.kwargs.get('pk'))
        product_id = review.product.pk
        return reverse('product_detail',  kwargs={'pk': product_id})


class ReviewDelete(LoginRequiredMixin, DeleteView):
    template_name = 'review/review_delete.html'
    model = Review
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        review = self.get_object()
        if request.user != review.author:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        review = Review.objects.get(pk=self.kwargs.get('pk'))
        product_id = review.product.pk
        return reverse('product_detail',  kwargs={'pk': product_id})
