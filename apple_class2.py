class Apple:
    def __init__(self, w, c):
        self.weight = w
        self.color = c

    def fresh(self, days, temp):
        self.freshness = days*temp
        print(f"入荷してから{days}日、平均{temp}度で保管されており新鮮度は{self.freshness}です.新鮮度は０がもっとも新鮮です。")



