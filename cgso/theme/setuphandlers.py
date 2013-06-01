from collective.grok import gs
from cgso.theme import MessageFactory as _

@gs.importstep(
    name=u'cgso.theme', 
    title=_('cgso.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('cgso.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
