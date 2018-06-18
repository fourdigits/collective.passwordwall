"""Set up the Passwordwall settings in Plone control panel."""
from zope.interface import implementedBy
from zope.interface import classImplementsOnly
from zope.interface import alsoProvides
from zope.interface import noLongerProvides
from zope.component import getGlobalSiteManager
from zope.formlib.form import FormFields

from plone.app.controlpanel.security import SecurityControlPanel
from plone.app.controlpanel.security import SecurityControlPanelAdapter
from plone.app.controlpanel.security import ISecuritySchema

from .interfaces import IPasswordwall, IPasswordwallSchema


# add accessors to adapter


def get_passwordwall(self):
    """Getter."""
    return IPasswordwall.providedBy(self.portal)


SecurityControlPanelAdapter.get_passwordwall = get_passwordwall


def set_passwordwall(self, value):
    """Setter."""
    operator = value and alsoProvides or noLongerProvides
    operator(self.portal, IPasswordwall)

SecurityControlPanelAdapter.set_passwordwall = set_passwordwall

SecurityControlPanelAdapter.passwordwall = property(
    SecurityControlPanelAdapter.get_passwordwall,
    SecurityControlPanelAdapter.set_passwordwall
)

# re-register adapter with new interface
_decl = implementedBy(SecurityControlPanelAdapter)
_decl -= ISecuritySchema
_decl += IPasswordwallSchema
classImplementsOnly(SecurityControlPanelAdapter, _decl.interfaces())
del _decl

getGlobalSiteManager().registerAdapter(SecurityControlPanelAdapter)

# re-instantiate form
SecurityControlPanel.form_fields = FormFields(IPasswordwallSchema)
