import streamlit as st

# 修改标签页的文字和图标
st.set_page_config(page_title="相册", page_icon="📷")
st.title("我的相册")

# 初始化当前图片索引（存储在session_state中）
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 定义图片列表（至少3张，包含url和图注）
images = [
    {
        'url': "https://ts2.tc.mm.bing.net/th/id/OIP-C.33geQqzMzzvMjQyGtrROkwHaEK?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
        'text': "奶龙"
    },
    {
        'url': "https://ts4.tc.mm.bing.net/th/id/OIP-C.HyghjeluXOQiGrnvKyy69gHaEL?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
        'text': "loopy"
    },
    {
        'url': "https://img-baofun.zhhainiao.com/pcwallpaper_ugc/preview_jpg/407407e31707ccfa9e5cd147a84da801.jpg",
        'text': "噜噜"
    }
]

# 显示当前图片和对应的图注
st.image(images[st.session_state['ind']]['url'], caption=images[st.session_state['ind']]['text'])

# 定义“下一张”函数（循环切换）
def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

# 定义“上一张”函数（循环切换）
def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)

# 显示“上一张”和“下一张”按钮
col1, col2 = st.columns(2)
with col1:
    st.button("上一张", on_click=prevImg)
with col2:
    st.button("下一张", on_click=nextImg)
