from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse

class CustomAdminLoginView(LoginView):
    template_name = "templates/admin/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("admin:index"))
        return super().dispatch(request, *args, **kwargs)
