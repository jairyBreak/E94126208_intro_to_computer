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
        print("狗現在的體重=",self.weight,",狗現在的心情=",self.mood)
class Cats(Animal):
    def __init__(self, weight, mood):
        super().__init__(weight,mood)#繼承屬性
    def walk(self,t_walk):
        self.weight -= 0.1*t_walk#設定子類別方法
        self.mood -= 1*t_walk
    def feed(self,t_feed):
        super().feed(t_feed)
        self.weight += 0.1*t_feed
    def bath(self,t_bath):
        super().bath(t_bath)
    def printf(self, n_feed, n_walk, n_bath):
        self.walk(n_walk)
        self.feed(n_feed)
        self.bath(n_bath)
        print("貓現在的體重=",self.weight,",貓現在的心情=",self.mood)
dog = Dogs(4.8, 65) #建立物件
dog.printf(18, 10, 4)#執行方法
cat = Cats(8.2, 60) 
cat.printf(40, 7, 1)