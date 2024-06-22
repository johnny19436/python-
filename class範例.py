#建立一個bear類別
class Bear:
    # bear的預設屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定義say_hello函數
    def say_hello(self):
        print("Hello my name is " + self.name)
        print("Im " + str(self.age) + " years old")

# 建立名為Chiikawa的物件
Chiikawa = Bear("Chiikawa", 9)
Chiikawa.say_hello()


# Chiikawa = Bear("Chiikawa", 9)
# Jayin = Bear("Jayin", 20)
# BearBoss = Bear("爆爆熊抱哥", 43)

# Chiikawa.say_hello()
# Jayin.say_hello()
# BearBoss.say_hello()
