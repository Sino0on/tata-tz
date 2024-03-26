from rest_framework import permissions
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404


class CanChangeRestaraunt(permissions.BasePermission):
    message = _('Недостаточно прав')

    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'DELETE']:
            if request.user.is_authenticated:
                if request.user.is_staff:
                    return True
            return False
        return True
