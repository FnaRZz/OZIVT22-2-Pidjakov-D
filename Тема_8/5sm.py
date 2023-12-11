# для вывода текущего времени
import datetime
r = datetime.datetime.now()
print (r)

# основной код
class ON_OFF:
    def on(self):
        print('включён')

    def off(self):
        print('не включён')


class PEREF:
    def ok(self):
        print('подключено')

    def neok(self):
        print('не подключено')

class PC(ON_OFF, PEREF):
    pass

camera_phone = PC()
camera_phone.on()
camera_phone.off()
camera_phone.ok()
camera_phone.neok()
