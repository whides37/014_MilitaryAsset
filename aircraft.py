import json
from military_asset import MilitaryAssetInventory

#load_data()でJSONデータを開く
class AircraftInventry(MilitaryAssetInventory):
    def __init__(self):
        super().__init__()  # 親クラスの初期化（items = {}）
        self.load_data()

    #JSONを辞書に変換
    def load_data(self):
        with open("aircraft_data.json","r",encoding="utf-8") as f:
            self.items = json.load(f)
    
    #JSON保存機能追加
    def save_data(self):
        with open("aircraft_data.json","w",encoding="utf-8") as f:
            json.dump(self.items,f,ensure_ascii=False,indent=4)

    #継承
    def add_item(self,name,quantitiy):
        super().add_item(name,quantitiy)
        self.save_data()

    #更新が終わったあとに追加処理＝更新後になにかあるかもよ
    def _after_update(self):
            self.save_data()