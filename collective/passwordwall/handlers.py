"""Initalize Passwordwall."""
from AccessControl import getSecurityManager

from .settings import COOKIE_NAME
from .utils import get_password


def is_anonymous_user():
    """Return False if user is logged in."""
    u = getSecurityManager().getUser()
    return (u is None or u.getUserName() == 'Anonymous User')


def show_basicauth_popup(request):
    """Show basic auth popup."""
    realm = request.response.realm
    request.response.setStatus(401)
    request.response.setHeader(
        'WWW-Authenticate',
        'basic realm="%s"' % realm, 1)
    request.response.setBody("""
<html><head><title>Login</title></head><body><p>
    This site has been password-walled.
    Your site user credentials are invalid here.
    Contact your site administrator for credentials.
</p></body></html>""")


def basicauth_validate(username_password_tuple):
    """Check that basic auth-supplied username + password is valid."""
    username, password = username_password_tuple
    # username doesn't matter
    if password == get_password():
        return True


def reject_missing_password(portal, request):
    """Check for passwordwall cookie / basicauth creds."""
    # Copied from rejectAnonymous
    if request['REQUEST_METHOD'] == 'OPTIONS':
        return
    # Don't ask again if already logged in
    if not is_anonymous_user():
        return
    if request.cookies.get(COOKIE_NAME):
        return
    username_password_tuple = request._authUserPW()
    if not username_password_tuple:
        show_basicauth_popup(request)
        return
    if not basicauth_validate(username_password_tuple):
        show_basicauth_popup(request)
        return
    request.response.setCookie(
        COOKIE_NAME,
        'content doesnt matter',
        path='/',
    )


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
