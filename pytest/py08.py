class FruitCategory():
    title = "水果管理系統"

    def __init__(self, id , category):
        self.id = id 
        self.category = category

    def showInfo(self):
        print("類別編號",self.id)
        print("類別名稱: ",self.category)

print("--------------使用自訂建構子-------------------")

fc=FruitCategory("c01", "春天水果")
fc.showInfo()

fc.category = "Spring Fruit"
fc.showInfo()