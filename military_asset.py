class MilitaryAssetInventory:

    def __init__(self):
        self.items = {}
    
    #追加メソッド
    def add_item(self,name,quantitiy):
        if not isinstance(name,str):
            raise TypeError("名前は文字列で入力してください")
        if not isinstance(quantitiy,int):
            raise TypeError("追加数は数値で入力してください")
        if quantitiy <= 0:
            raise ValueError("数値は１以上で入力してください")
        if name in self.items:
            self.items[name] += quantitiy
        else:
            self.items[name] = quantitiy

    #削除メソッド
    def remove_item(self,name,quantitiy):
        if not isinstance(name,str):
            raise TypeError("名前は文字列で入力してください")
        if not isinstance(quantitiy,int):
            raise TypeError("追加数は数値で入力してください")
        if quantitiy <= 0:
            raise ValueError("数値は１以上で入力してください")
        if name in self.items:
            raise KeyError("登録がありません")
        else:
            self.items[name] -= quantitiy

    #在庫表示
    def get_stock(self,name):
        return self.items[name]
    
    #printの設定
    def __str__(self):
        result = "=== 在庫一覧 ===\n"
        for name ,stock in self.items.items():
            result += f"{name}:{stock:>2}\n"
        return result