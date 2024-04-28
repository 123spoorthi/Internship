class dog:
    def sound(self):
        print("bow")
class duck:
    def sound(self):
        print("quack")
class cat:
    def sound(self):
        print("meow")
def make_sound(sound):
    sound.sound()
c=cat()
d=dog()
du=duck()
make_sound(d)