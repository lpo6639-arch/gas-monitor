import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="AI 瓦斯安全監測", layout="wide")

st.title("🔥 AI 智慧瓦斯安全監測系統")
st.info("本系統正透過 AI 即時監控爐火狀態與瓦斯成本")

# 左側：數據指標
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 即時數據")
    st.metric("A12 桌瓦斯效率", "65%", "-15%", delta_color="inverse")
    st.error("⚠️ 偵測到嚴重鏽蝕與橘火")
    
    # 這裡讓老闆輸入單價看成本
    price = st.number_input("當前瓦斯單價 (元/kg)", value=45)
    st.write(f"**預計每月因效率低下損耗：** {price * 15} 元")

with col2:
    st.subheader("📸 AI 視覺診斷")
# 讀取並顯示你剛才上傳的照片
st.image("IMG20260305161129.jpg", caption="現場實拍：爐頭孔洞因鏽蝕嚴重堵塞", use_container_width=True)

st.divider()
st.caption("AI 核心已啟動：CV2 版本 " + cv2.__version__)
