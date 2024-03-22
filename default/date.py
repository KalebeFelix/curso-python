# DATETIME
import datetime

data = datetime.datetime.now()
nasc = datetime.datetime(2006,4,19)              

print(f'{data.day:02}/{data.month:02}/{data.year}')

print(data.strftime("%d/%m/%Y"))

# dia da semana
print(nasc.strftime("%A"))