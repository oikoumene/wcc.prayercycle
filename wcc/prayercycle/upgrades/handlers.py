from collective.grok import gs
from Products.CMFCore.utils import getToolByName

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.prayercycle to 1002',
                description=u'Upgrade wcc.prayercycle to 1002',
                source='1001', destination='1002',
                sortkey=1, profile='wcc.prayercycle:default')
def to1002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.prayercycle.upgrades:to1002')
