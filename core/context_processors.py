def user_context(request):
    """
    Add user-specific attributes to the context.
    """
    
    user_context_dict = {
        'is_authenticated': request.user.is_authenticated
    }
    
    if request.user.is_authenticated:
        user_context_dict['is_superuser'] = request.user.is_superuser,
        user_context_dict['is_staff'] = request.user.is_staff,
        user_context_dict['is_root'] = request.user.is_root,
        user_context_dict['is_client_admin'] = request.user.is_root
    
    return user_context_dict