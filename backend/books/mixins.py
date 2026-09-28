from django.http import HttpResponseForbidden


class AdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden(
                "Вы не являетесь администратором данного магазина."
            )
        return super().dispatch(request, *args, **kwargs)
