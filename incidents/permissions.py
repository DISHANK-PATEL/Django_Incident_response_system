from rest_framework import permissions

class IsAdminOrResponder(permissions.BasePermission):
    """
    Custom permission to only allow Admins or Responders to edit incidents.
    Standard Users can only Create or View.
    """
    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for everyone authenticated
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow POST (Create) for everyone authenticated
        if request.method == 'POST':
            return True

        # For PATCH/PUT/DELETE, check if user is ADMIN or RESPONDER
        return request.user.role in ['ADMIN', 'RESPONDER']