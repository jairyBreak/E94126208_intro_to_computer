class Animal():#建立animal類別
    def __init__(self, weight, mood):#設定屬性
        self.weight = weight
        self.mood = mood
    def feed(self,t_feed):#設定方法
        self.mood += 1*t_feed
    def walk(self):
        pass
    def bath(self, t_bath):
        self.mood = self.mood - 2*t_bath
class Dogs(Animal):
    def __init__(self, weight, mood):
        super().__init__(weight,mood)#繼承屬性
    def walk(self,t_walk):
        self.weight -= 0.2*t_walk#設定子類別方法
        self.mood += 2*t_walk
    def feed(self,t_feed):
        super().feed(t_feed)
        self.weight += 0.2*t_feed
    def bath(self,t_bath):
        super().bath(t_bath)
    def printf(self, n_feed, n_walk, n_bath):
        self.walk(n_walk)
        self.feed(n_feed)
        self.bath(n_bath)
        print("狗現在的體重=",self.weight,"kg,狗現在的心情=",self.mood)
class Shiba(Dogs):
    def __init__(self, weight, mood):
        super().__init__(weight,mood)#繼承屬性
    def walk(self,t_walk):
        super().feed(t_walk)
    def feed(self,t_feed):
        self.mood += 5 * t_feed
        self.weight += 0.3*t_feed
    def bath(self,t_bath):
        super().bath(t_bath)
    def printf(self, n_feed, n_walk, n_bath):
        self.walk(n_walk)
        self.feed(n_feed)
        self.bath(n_bath)
        print("柴犬現在的體重=",self.weight,"kg,現在的心情=",self.mood)
    def mood_constraint(self, constr):
        self.constr = constr
        print("mood最高只能為=" ,self.constr )
        if self.constr < self.mood:
            self.mood = self.constr
            print("所以，柴犬現在的心情", self.mood)

shiba1 = Shiba(5, 70) 
shiba1.printf(10, 0, 0) 
shiba1.mood_constraint(90) #改變mood上限
shiba2 = Shiba(5, 70) 
shiba2.printf(50, 0, 0) 
shiba2.mood_constraint(300) #請在這邊改變你的mood_constraint
