import streamlit as st
from components.chart_area import render_chart

with st.sidebar:
    st.header("設定")
    dark_mode = st.toggle("ダークモード")
    refresh = st.toggle("自動更新")


# カラムを3つ作成
col1, col2, col3 = st.columns(3)

with col1:
    toggle = st.toggle("ダークモード")

with col2:
    notification = st.toggle("通知ON")

with col3:
    auto_refresh = st.toggle("自動更新")





if toggle:
    st.write("🌙 ダークモード ON")
else:
    st.write("☀️ ライトモード ON")





# カラムを3つ作る（左:余白, 中:余白, 右:ボタン用）
col1, col2, col3, col4 = st.columns(4)  # ← 数字で比率を調整できる

with col1:
    keyTateya = st.text_input("建屋", value="A")  # 左カラムにテキスト入力を置く
    searchBtn = st.button("検索") 

with col2:
    searchList = st.checkbox("選択肢1")  # 中カラムにチェックボックスを置く

with col3:
    appendBtn = st.button("追加")  # 右カラムにボタンを置く

with col4:
    appendList = st.selectbox("選択肢2", options=["A", "B", "C"])  # 右カラムにセレクトボックスを置く


st.button("通常ボタン")  # デフォルト (secondary)
st.button("プライマリーボタン", type="primary")
st.button("セカンダリーボタン", type="secondary")
st.button("目立たないボタン", type="tertiary")

