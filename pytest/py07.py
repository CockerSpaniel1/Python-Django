class Fruit():
    no = 1
    name =""
    price=0.0

    def showInfo(self):
        print("水果編號: ",self.no)
        print("水果名稱: ",self.name)
        print("水果售價: ",self.price)

fruit = Fruit()
fruit.showInfo()

print("---------------------------")
fruit.name= "芒果"
fruit.price =300
fruit.showInfo()