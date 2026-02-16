#aircraft.pyからAircraftInventoryクラスをもってくる
from aircraft import AircraftInventory

inventry = AircraftInventory()

try:
    inventry.add_item("A6M 零戦",10)
    inventry.remove_item("J7W 震電",10)
except ValueError as e :
    print("値エラー:",e)
except KeyError as e :
    print("キーエラー:",e)
except TypeError as e :
    print("型エラー:",e)

print(inventry)