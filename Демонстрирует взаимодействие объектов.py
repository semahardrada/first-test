#Гибель пришельца
#Демонстрирует взаимодействие объектов
class Player(object):
    """Игрок в экшен-игре"""
    def blast(self,enemy):
        print("Игрок стреляет во врага.\n")
        enemy.die()

class Alien(object):
    """Враждебный пришелец-инопланетянин в экшен-игре"""
    def die(self):
        print('Тяжело дыша, пришелец произносит: "Ну, вот и все... Спета моя песенка" \n \
              "Уже и в глазах темнеет... ГГ проебали"')
        
#Основная часть программы
print("\t\tГибель пришельца\n")
hero = Player()
invader = Alien()
hero.blast(invader)
input("Enter, чтобы выйти")
