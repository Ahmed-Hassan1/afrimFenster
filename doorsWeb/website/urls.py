from django.urls import path
from .views import *


urlpatterns = [
    path('',homePage,name="home"),
    path('fenster',fenster,name="fenster"),
    path('kunalufenster',kunAluFenster,name="kunalufenster"),
    path('holzalufenster',holzAluFenster,name="holzalufenster"),
    path('holzfenster',holzfenster,name="holzfenster"),
    path('turen',turen,name="turen"),
    path('toranlagen',toranlagen,name="toranlagen"),
    path('sonnen',sonnen,name="sonnen"),
    path('kontakt',kontakt,name="kontakt"),
    path('datenschutzerklärung',Datenschutzerklärung,name="datenschutzerklärung"),
    path('impressum',impressum,name="impressum"),
]