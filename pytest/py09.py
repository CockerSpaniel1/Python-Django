class Animal():
    def __init__(self,cateogry, live):
        self.cateogry = cateogry
        self.live = live

    def setCategory(self,cateogry):
        self.cateogry = cateogry

    def setLive(self,live):
        self.live = live

    def getCategory(self):
        return self.cateogry
    
    def getLive(self):
        return self.live
    
ani = Animal("昆蟲", "陸地")
print(ani.getCategory())

ani.setCategory("哺乳動物")
print(ani.getCategory())


class Bird(Animal):
    def __init__(self):
        self.__title = "企鵝"
        self.__fly = "不會飛"
    def getInfo(self):
        return self.__title,self.__fly
    
print("------------------------------------")
bird = Bird()
print(bird.getInfo())

bird.setCategory("鳥類")
print(bird.getCategory())