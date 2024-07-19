import datetime
from datetime import datetime
from datetime import date

# mi_hora = datetime.time(23, 20, 50, 1500)
# print(type(mi_hora))
# print(mi_hora)
# print(mi_hora.hour)

# mi_fecha = datetime.date(2024, 6, 29)
# print(mi_fecha)
# print(mi_fecha.year)
# print(mi_fecha.ctime())
# print(mi_fecha.today())

# mi_fecha = datetime(2024, 6, 29, 23, 26, 10, 1000)
# mi_fecha = mi_fecha.replace(month = 10)

# print(mi_fecha)

# nacimiento = date(1995, 3, 9)
# defuncion = date(2035, 2, 10)

# vida = defuncion - nacimiento
# print(vida.days)

despierta = datetime(2024, 6, 29, 7, 30)
duerme = datetime(2024, 6, 29, 23, 30)

vigilia = duerme - despierta
print(vigilia.seconds)


