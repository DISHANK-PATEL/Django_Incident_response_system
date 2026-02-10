from rest_framework import permissions

class IsAdminOrResponder(permissions.BasePermission):
    """
    Custom permission to only allow Admins or Responders to edit incidents.
    Standard Users can only Create or View.
    """
    def has_permission(self, request, view):
       
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.method == 'POST':
            return True

        return request.user.role in ['ADMIN', 'RESPONDER']