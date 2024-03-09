slogan = "Enjoy the science and Technology"

try:
    print(slogan)
except:
    print("other error")
finally:
    print("~~~ The End ~~~")


try:
    print(slogan)
except:
    print("other error")
else:
    print("Congratuation!")    
finally:
    print("~~~ The End ~~~")