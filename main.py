from bottlebuilder import BottleBuilder
from colafactory import ColaFactory
from pepsifactory import PepsiFactory

colabuilder = BottleBuilder(ColaFactory)
pepsibuilder = BottleBuilder(PepsiFactory)
colabuilder.takebottle()
colabuilder.fillbottle()
colabuilder.closebottle()
colabuilder.applylabelonbottle()
pepsibuilder.takebottle()
pepsibuilder.fillbottle()
pepsibuilder.closebottle()
pepsibuilder.applylabelonbottle()