def user_context(request):
    """
    Add user-specific attributes to the context.
    """
    return {
        'is_authenticated': request.user.is_authenticated,
        'is_superuser': request.user.is_superuser,
        'is_staff': request.user.is_staff,
        'is_root': request.user.is_root,
        'is_client_admin': request.user.is_root
        # Add custom attributes or permissions if needed
    }