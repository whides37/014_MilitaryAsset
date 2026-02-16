class AircraftInventory:

    def __init__(self):
        self.items = {
            "A6M 零戦": 5,
            "J7W 震電": 2,
            "J1N 月光": 3,
            "A7M 烈風": 4
        }
    def add_item(self,name, quantity):
        if not isinstance(name,str):
            raise TypeError("名前は機種と機種名で入力してください")
        if not isinstance(quantity,int):
            raise TypeError("機体数は数値で入力してください")
        if quantity <= 0 :
            raise ValueError("機体数は1以上の数で入力してください")
        # 既に登録済みの機体（キーの値）なら、なければ新規登録
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def remove_item(self,name, quantity):

        if not isinstance(name,str):
            raise TypeError("名前は機種と機種名で入力してください")
        if not isinstance(quantity,int):
            raise TypeError("機体数は数値で入力してください")
        if quantity <= 0 :
            raise ValueError("機体数は1以上の数で入力してください")
        if name not in self.items:
            raise KeyError("その機体は登録されていません")
        if quantity > self.items[name]:
            raise ValueError("在庫不足です")
        self.items[name] -= quantity

    def get_stock(self, name):
        return self.items[name]

