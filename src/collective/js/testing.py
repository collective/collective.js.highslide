from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CollectiveJs(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.js
        xmlconfig.file('configure.zcml',
                       collective.js,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.js:default')

COLLECTIVE_JS_FIXTURE = CollectiveJs()
COLLECTIVE_JS_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_JS_FIXTURE, ),
                       name="CollectiveJs:Integration")