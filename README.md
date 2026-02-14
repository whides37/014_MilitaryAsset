## 目的
引き続き、Pythonの基礎理解。
今回は辞書を覚えることが目的。（辞書＋KeyError練習）
今回仕様書は自分で最初から定義。

---

##  ファイル名
aircraft.py

### クラス名
AircraftInventory:

### 属性
self.items = {}

* key: 機体名（str）
* value: 在庫数（int）

---
## メソッド仕様

### ① add_item(name, quantity)

#### エラー条件

* name が str でない → TypeError
* quantity が int でない → TypeError
* quantity <= 0 → ValueError

#### 処理

* name が存在すれば → 加算
* なければ → 新規追加

---

### ② remove_item(name, quantity)

#### エラー条件

* name が存在しない → KeyError
* quantity が int でない → TypeError
* quantity <= 0 → ValueError
* quantity > 在庫 → ValueError（在庫不足）

#### 処理

* 正常 → 減算

---

### ③ get_stock(name)

#### エラー条件

* name が存在しない → KeyError

#### 処理

* 在庫数を返す

---
# 将来拡張
domain/
military_asset.py ← 親クラス 
aircraft.py 
battleship.py

---

---

### 間違いをAIに直してもらったところ

> 在庫メソッドget_stock(name)
> 在庫増減を「追加、取り出し」から継承して書く。

継承は使わない。役割が違う。

add/remove は「操作」
get_stock は「参照」