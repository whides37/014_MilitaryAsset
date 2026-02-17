import streamlit as st
from aircraft import AircraftInventry

# インスタンス生成
inventry = AircraftInventry()

st.title("✈ 航空機インベントリ管理アプリ")

# 現在の一覧表示
st.subheader("現在の航空機一覧")
st.table(inventry.items)

# 新規追加フォーム
st.subheader("航空機を追加")

name = st.text_input("航空機名")
quantity = st.number_input("数量", min_value=1, step=1)

if st.button("追加する"):
    try:
        inventry.add_item(name, int(quantity))
        st.success(f"{name} を {quantity} 機追加しました")
    except Exception as e:
        st.error(str(e))

# 再読み込みボタン
if st.button("データを再読み込み"):
    inventry.load_data()
    st.info("データを再読み込みしました")