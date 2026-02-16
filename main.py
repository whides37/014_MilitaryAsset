#aircraft.pyからAircraftInventoryクラスをもってくる
from aircraft import AircraftInventry

inventry = AircraftInventry()

inventry.add_item("A6M 零戦",100)
inventry.add_item("J7W 震電",200)
inventry.add_item("J1N 月光",1)
inventry.add_item("A7M 烈風",3)

print(inventry)