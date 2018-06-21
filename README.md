# Passwordwall

This puts your Plone site behind a Basic Auth login,
without actually logging in a Plone user.


## Use case

This is intended for use in acceptance environments, where you want give a
some people full testing access (also anonymous access), but without opening
the site to the whole world.


### Plain text

The site password is stored internally as plain text. Do not use your personal
super secure password here, because we intended it to be used by several
people.

The password should be easy to look up and communicate, which is why we store
it in plain text.

If you have a different use case for this product where you want a different
behaviour: We *do* welcome pull requests!


## Alternatives

You might also achieve this with:
- web server Basic Auth
- IP restriction

But if your hosting setup is such that that isn't an option,
this package might help.


## Related products

Use iw.rejectanonymous if you require users to log in anyway.


## How to use

Go to the Plone control panel, to the "Security" tab.

You will see a checkbox "Site behind password". Check it to activate the passwordwall.
This means users will need to supply credentials before they can use the site.

Users that are already logged in as Plone users are not asked for credentials.

The password can be set by the "Password" field.
This is what people have to type in the "password" box in the dialog to get access.
The "username" in the dialog is not used.


### Picking a password

It's recommended to not use dictionary words as is, nor should you use other
well known phrases as passwords. This is because their MD5 hashes (which we
store as the cookie value) would easily reveal the password. Just mixing in a
couple of numbers or other characters should make for a fine password.
Try it on https://isc.sans.edu/tools/reversehash.html if you're not sure.


### Changing the password

When you change the password, existing cookies will be invalid, because the
password hash changed. People without Plone accounts (or who are logged out
from Plone) will be forced to re-enter the credentials.


## Thank you

- Ingeniweb for iw.rejectanonymous, some of whose code this product copied.
  All spelling mistakes are also their fault.
