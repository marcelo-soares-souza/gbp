from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator


# import logging
# logger = logging.getLogger('sequenciamento')


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class CreatedByRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.criado_por != self.request.user and not self.request.user.is_superuser:
            return HttpResponseRedirect(reverse('permission_denied'))

        return super(CreatedByRequiredMixin, self).dispatch(request, *args, **kwargs)


class ColaboradorRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if (self.request.user not in obj.colaborador.all() and obj.criado_por != self.request.user and not self.request.user.is_superuser and obj.responsavel != self.request.user):
            return HttpResponseRedirect(reverse('permission_denied'))

        return super(ColaboradorRequiredMixin, self).dispatch(request, *args, **kwargs)


class ResponsavelRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if (obj.criado_por != self.request.user and not self.request.user.is_superuser and obj.responsavel != self.request.user):
            return HttpResponseRedirect(reverse('permission_denied'))

        return super(ResponsavelRequiredMixin, self).dispatch(request, *args, **kwargs)


class ListColaboradorRequiredMixin(object):

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            queryset = self.model._default_manager.all()
        else:
            queryset = self.model._default_manager.filter(Q(colaborador__in=[user.id]) | Q(
                criado_por_id=user.id) | Q(responsavel_id=user.id))

        return queryset


class ListResponsavelRequiredMixin(object):

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            queryset = self.model._default_manager.all()
        else:
            queryset = self.model._default_manager.filter(Q(criado_por_id=user.id) | Q(responsavel_id=user.id))

        return queryset
