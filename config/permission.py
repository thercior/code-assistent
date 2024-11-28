from django.core.exceptions import PermissionDenied


class UserPermissionMixin:

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.pk == self.get_object().pk):
            raise PermissionDenied("Você não tem permissão para alterar a senha deste usuário")

        return super().dispatch(request, *args, **kwargs)
