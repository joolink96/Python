
#__init__은 생성자를 의미
class Unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0}유닛이 생성 되었습니다" .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp,self.damage))


marine1= Unit("마린",40,5) #객체
marine2= Unit("마린",40,5) #객체
tank=Unit("탱크",150,35)   #객체

#marine3= Unit("마린") #인수 부족 <---오류
#marine2= Unit("마린",40) #인수 부족 <---오류