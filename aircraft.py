from military_asset import MilitaryAssetInventory

class AircraftInventry(MilitaryAssetInventory):
    def __init__(self):
        super().__init__()  # 親クラスの初期化（items = {}）
        self.items = {
            "A6M 零戦": 5,
            "J7W 震電": 2,
            "J1N 月光": 1,
            "A7M 烈風": 3
        }