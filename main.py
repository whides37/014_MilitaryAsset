#aircraft.pyからAircraftInventoryクラスをもってくる
from aircraft import AircraftInventry

#継承
inventry = AircraftInventry()

inventry.add_item("A6M 零戦",10)
inventry.add_item("J7W 震電",2)
inventry.add_item("J1N 月光",1)
inventry.add_item("A7M 烈風",3)

print(inventry)