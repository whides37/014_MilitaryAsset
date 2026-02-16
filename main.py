""" 
import aircraft                 ←成功する、import Errorはでない。
inventry = AircraftInventory()  →NameError 

"""

#aircraft.pyからAircraftInventoryクラスをもってくる
from aircraft import AircraftInventory

inventry = AircraftInventory()

inventry.add_item("A6M 零戦",10)
inventry.remove_item("J7W 震電",1)

print(inventry)