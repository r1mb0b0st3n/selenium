 # Class yapıları
class Human:
    #Constracter
    def __init__(self,name):
        self.name = name
        print ("Human instance is a created")
    def __str__(self):
        return f"Str Fonksiyonundan dönen değer : {self.name}"
    def walk(self,sentence):
        print(f"{self.name} : {sentence}")
    def talk(self):
        print(f"{self.name} talking")

human1 = Human("Enes")
human1.talk()
print("----------------")
human2 = Human("Cem")
human2.walk("Hello")
print(human1)