from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verifica se a queryset existe na view
        if hasattr(view, 'queryset') and view.queryset is not None:
            model_permission_codename=self.get_model_permission_codename(request.method, view)
            if not model_permission_codename:
                return False
            return request.user.has_perm(model_permission_codename)
        # Se a view não tem queryset, permite a requisição
        return True

    def get_model_permission_codename(self, method, view):
        try:
            model_name=view.queryset.model._meta.model_name
            app_label=view.queryset.model._meta.app_label
            action=self.get_action_suffix(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None

    def get_action_suffix(self, method):
        method_actions={
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
