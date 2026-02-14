class AircraftInventory:

    def __init__(self):
        self.items = {
            "A6M Zero": 5,
            "J7W Shinden": 2,
            "J1N Gekko": 3,
            "A7M Reppu": 4
        }
    def add_item(self,name, quantity):
        if not isinstance(name,str):
            raise TypeError("名前は機種と機種名で入力してください")
        if not isinstance(quantity,int):
            raise TypeError("機体数は数値で入力してください")
        if quantity <= 0 :
            raise ValueError("機体数は0以上の数で入力してください")
        #辞書にあるか確認
        if name in self.items:
            self.items[name] += quantity
        #なければ追加
        else:
            self.items[name] = quantity

        