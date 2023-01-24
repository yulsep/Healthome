from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.auxiliar import Auxiliar
from .models.familiar import Familiar
from .models.paciente import Paciente
from .models.personalSalud import PersonalSalud
from .models.historiaClinica import HistoriaClinica
from .models.signosVitales import SignosVitales
from .models.sugerencias import Sugerencias

admin.site.register(User)
admin.site.register(Auxiliar)
admin.site.register(Familiar)
admin.site.register(Paciente)
admin.site.register(PersonalSalud)
admin.site.register(HistoriaClinica)
admin.site.register(SignosVitales)
admin.site.register(Sugerencias)