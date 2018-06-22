"""Initalize Passwordwall."""
import hashlib

from AccessControl import getSecurityManager

from .settings import COOKIE_NAME, PASSWORDWALL_VIEW_NAME
from .utils import get_password


def is_anonymous_user():
    """Return False if user is logged in."""
    u = getSecurityManager().getUser()
    return (u is None or u.getUserName() == 'Anonymous User')


def start_auth_dialog(request):
    """Start authentication dialog: redirect to passwordwall login view."""
    pwwall_url = request.ACTUAL_URL.rstrip('/') + PASSWORDWALL_VIEW_NAME

    # If user went to /news, we redirect there after login.
    came_from = request.ACTUAL_URL
    request.form = {'came_from': came_from}

    request.response.redirect(pwwall_url)


def has_valid_cookie(request):
    """Check if request has valid cookie."""
    value = request.cookies.get(COOKIE_NAME)
    password = get_password()
    _hash = hashlib.md5(password).hexdigest()
    return value == _hash


def reject_missing_password(portal, request):
    """Check for passwordwall cookie."""
    # Copied from rejectAnonymous
    if request['REQUEST_METHOD'] == 'OPTIONS':
        return
    # Don't ask again if already logged in
    if not is_anonymous_user():
        return
    # If we're on the passwordwall page, continue
    if request.ACTUAL_URL.rstrip('/').endswith(PASSWORDWALL_VIEW_NAME):
        return
    # If user has a valid cookie, let them in
    if has_valid_cookie(request):
        return
    start_auth_dialog(request)


def insert_reject_missing_password_hook(portal, event):
    """Insert the hook that checks for passwordwall creds."""
    try:
        event.request.post_traverse(
            reject_missing_password,
            (portal, event.request),
        )
    except RuntimeError:
        # Make this work in a testrunner (copied from iw.rejectanonymous)
        pass
