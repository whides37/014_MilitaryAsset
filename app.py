import streamlit as st
from aircraft import AircraftInventry

# インスタンス生成
inventry = AircraftInventry()

st.title("✈ 航空機インベントリ管理アプリ（検索機能つき）")

# -----------------------------
# 検索機能
# -----------------------------
st.subheader("航空機を検索")

keyword = st.text_input("検索キーワード（例：F-15、零戦 など）")

if keyword:
    # 部分一致で検索
    results = {k: v for k, v in inventry.items.items() if keyword.lower() in k.lower()}

    if results:
        st.write("🔍 **検索結果**")
        st.table(results)
    else:
        st.warning("該当する航空機が見つかりませんでした")
else:
    st.info("キーワードを入力すると検索できます")

# -----------------------------
# 全データ一覧
# -----------------------------
st.subheader("全航空機一覧")
st.table(inventry.items)

# -----------------------------
# 新規追加フォーム
# -----------------------------
st.subheader("航空機を追加")

name = st.text_input("航空機名")
quantity = st.number_input("数量", min_value=1, step=1)

if st.button("追加する"):
    try:
        inventry.add_item(name, int(quantity))
        st.success(f"{name} を {quantity} 機追加しました")
        st.experimental_rerun()
    except Exception as e:
        st.error(str(e))

# -----------------------------
# 削除機能
# -----------------------------
st.subheader("航空機を削除")

if inventry.items:
    delete_target = st.selectbox("削除する航空機を選択", list(inventry.items.keys()))
    if st.button("削除する"):
        del inventry.items[delete_target]
        inventry.save_data()
        st.warning(f"{delete_target} を削除しました")
        st.experimental_rerun()
else:
    st.info("削除できる航空機がありません")

# -----------------------------
# 再読み込み
# -----------------------------
if st.button("データを再読み込み"):
    inventry.load_data()
    st.info("データを再読み込みしました")
    st.experimental_rerun()