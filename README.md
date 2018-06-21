Passwordwall
============

This puts your Plone site behind a Basic Auth login,
without actually logging in a Plone user.


Use case
--------

This is intended for use in acceptance environments, where you want give a
some people full testing access (also anonymous access), but without opening
the site to the whole world.


Alternatives
------------

You might also achieve this with:
- web server Basic Auth
- IP restriction

But if your hosting setup is such that that isn't an option,
this package might help.


Related products
----------------

Use iw.rejectanonymous if you require users to log in anyway.


How to use
----------

Go to the Plone control panel, to the "Security" tab.

You will see a checkbox "Site behind password". Check it to activate the passwordwall.
This means users will need to supply credentials before they can use the site.

Users that are already logged in as Plone users are not asked for credentials.

The password can be set by the "Password" field.
This is what people have to type in the "password" box in the dialog to get access.
The "username" in the dialog is not used.


Thank you
---------

- Ingeniweb for iw.rejectanonymous, some of whose code this product copied.
  All spelling mistakes are also their fault.
