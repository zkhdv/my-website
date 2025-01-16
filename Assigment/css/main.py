from reg import *
from log import *

kirish = 1

class Kirish:
    def init(self):
        self.admin = ['admin']
        self.admin_password = [1111]
        self.user = []
        self.password = []

    def tekshiruv(self):
        while True:
            print("\n--- Glavniy menyu ---")
            a = input('1. Login\n2. Register\n3. Chiqish\nSizning tanlovingiz: ')
            if a == '1':
                logg.login(self.admin, self.admin_password, self.user, self.password)
                break
            elif a == '2':
                self.user, self.password = register(self.user, self.password)
            elif a == '3':
                print("Dasturdan chiqildi.")
                break
            else:
                print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")

if name == "main":
    global kirish
    kirish = Kirish()
    kirish.tekshiruv()