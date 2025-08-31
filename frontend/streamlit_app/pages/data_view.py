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



st.header("Data View")
render_chart()


# カラムを3つ作る（左:余白, 中:余白, 右:ボタン用）
col1, col2, col3 = st.columns([2, 2, 1])  # ← 数字で比率を調整できる

with col3:
    btn = st.button("送信", type="primary")  # 右カラムにボタンを置く

refresh = st.button("データ更新")

if refresh:
    st.experimental_rerun()


st.button("通常ボタン")  # デフォルト (secondary)
st.button("プライマリーボタン", type="primary")
st.button("セカンダリーボタン", type="secondary")
st.button("目立たないボタン", type="tertiary")

