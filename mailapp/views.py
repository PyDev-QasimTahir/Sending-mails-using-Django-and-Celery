from mailapp.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse

class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thank's for Your Valueable Review!"
        return HttpResponse(msg)