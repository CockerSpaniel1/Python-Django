from py09 import Animal,Bird


ani = Animal("昆蟲", "陸地")
print(ani.getCategory())

ani.setCategory("哺乳動物")
print(ani.getCategory())

print("------------------------------------")
bird = Bird()
print(bird.getInfo())

bird.setCategory("鳥類")
print(bird.getCategory())