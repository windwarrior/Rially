from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils.decorators import available_attrs
from django.utils.encoding import force_str
from functools import wraps
from django.utils.six.moves.urllib.parse import urlparse
from django.shortcuts import resolve_url

def require_team_captain(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, teamId, *args, **kwargs):
            print("hasattr", hasattr(request.user, "riallyuser"))
            print("is_team_captain", request.user.riallyuser.is_team_captain)
            print("is_from_team", request.user.riallyuser.team.pk, teamId)
            if hasattr(request.user, "riallyuser") and request.user.riallyuser.is_team_captain and request.user.riallyuser.team.pk == int(teamId):
                return view_func(request, teamId, *args, **kwargs)
            path = request.build_absolute_uri()
            # urlparse chokes on lazy objects in Python 3, force to str
            resolved_login_url = force_str(
                resolve_url(login_url or settings.LOGIN_URL))
            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_scheme) and
                    (not login_netloc or login_netloc == current_netloc)):
                path = request.get_full_path()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(
                path, resolved_login_url, redirect_field_name)
        return _wrapped_view
    return decorator
