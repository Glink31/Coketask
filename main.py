from bottlebuilder import BottleBuilder
from colafactory import ColaFactory
from pepsifactory import PepsiFactory
b1=BottleBuilder(PepsiFactory())
b1.takebottle()
b1.applylabelonbottle()
b1.fillbottle()
b1.closebottle()
cp=b1.BuildProduct()
b2=BottleBuilder(ColaFactory())
b2.takebottle()
b2.applylabelonbottle()
b2.fillbottle()
b2.closebottle()
cc=b2.BuildProduct()