import streamlit as st
import pandas as pd
from PIL import Image
import io
import base64

# 页面基础配置
st.set_page_config(
    page_title="多功能Streamlit应用",
    layout="wide",
    initial_sidebar_state="auto"
)

# 全局样式（增加间距、统一容器样式）
st.markdown("""
    <style>
    /* 每个tab的容器样式，避免内容粘连 */
    .tab-container {
        padding: 20px;
        margin: 10px 0;
        background-color: #f9f9f9;
        border-radius: 8px;
    }
    /* 进度条样式补全 */
    .progress-bar {
        width: 100%;
        height: 20px;
        background-color: #e0e0e0;
        border-radius: 10px;
        overflow: hidden;
        margin: 8px 0;
    }
    .progress-fill {
        height: 100%;
        background-color: #4CAF50;
        border-radius: 10px;
    }
    /* 统一标题间距 */
    h1, h2, h3 {
        margin-bottom: 16px;
    }
    /* 表格样式优化 */
    table {
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

st.title("选项卡简单示例")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "数字档案", "南宁美食", "个人简历生成器",
    "相册", "音乐播放器", "视频网站"
])

# ======================== Tab1: 数字档案 ========================
with tab1:
    # 用container包裹，增加间距
    with st.container(border=True):
        st.title("学生 小八 数字档案")
        st.header("基础信息", divider="rainbow")

        # 2. 基础信息（text/markdown）
        st.markdown("""
        - 学生ID: N03-2023-001
        - 注册时间: 2023-09-01 | 精神状态: ✅ 正常
        - 当前教室: 实训楼108  | 安全等级：绝密
        """)

        # 3. 技能矩阵（metric组件）
        st.header("技能矩阵", divider="rainbow")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Python", value="95%", delta="+3%")
        with col2:
            st.metric(label="SQL", value="87%", delta="-2%")
        with col3:
            st.metric(label="Vue", value="68%", delta="-10%")

        # 4.课程进度
        st.header("📚 Streamlit课程进度", divider="rainbow")
        with st.container():
            st.markdown('<div class="streamlit-progress">', unsafe_allow_html=True)
            
            # 1. 整体进度条
            total_progress = 82  # 整体进度82%
            st.markdown(f"""
                <div>
                    <span>课程整体完成度：{total_progress}%</span>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {total_progress}%"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        # 5. 任务日志（table组件）
        st.header("任务日志", divider="rainbow")
        task_data = {
            "日期": ["2023-10-01", "2023-10-12", "2023-10-20"],
            "任务": ["学生数字档案", "模型管理系统", "数据可视化展示"],
            "状态": ["✅ 已完成", "🔄 进行中", "❌ 未完成"],
            "难度": ["★★☆☆☆", "★★★☆☆", "★★★★☆"]
        }
        task_df = pd.DataFrame(task_data)
        st.table(task_df)

        # 6. 最新代码成果（code组件）
        st.header("最新代码成果", divider="rainbow")
        code = """
def detect_villain(identity):
    if identity == "Z":
        detect_villain.identity = "T-ACCESS GRANTED"
        return "ALERT"
    stevil_db.update()
"""
        st.code(code, language="python")

        # 7. 系统日志（markdown）
        st.markdown("""
---
> **SYSTEM MESSAGE**: 下一个任务已解锁
> **SYSTEM**: 模型管理系统
> **CONTINUE**: 2025-03-01 12:42:48
> 系统状态: 在线 | 连接状态: 已加密
""")

# ======================== Tab2: 南宁美食 ========================
with tab2:
    with st.container(border=True):
        st.title("南宁美食指南")
        
        restaurants = {
            "店铺名称": [
                "猪霸王", "中山路复记老友粉", "螺遇牛",
                "邕州老街南宁酸嘢", "三品王", "水街老牌糯米饭"
            ],
            "特色美食": [
                "老友粉", "老友粉", "老友粉",
                "南宁酸嘢", "螺蛳粉", "南宁糯米饭"
            ],
            "评分": [4.5, 4.7, 4.8, 4.6, 4.4, 4.9],
            "人均(元)": [18, 20, 19, 15, 17, 12],
            "经度": [108.3228, 108.3245, 108.3189, 108.3125, 108.3088, 108.3056],
            "纬度": [22.8156, 22.8178, 22.8211, 22.8235, 22.8198, 22.8256]
        }
        df_rest = pd.DataFrame(restaurants)

        months = [f"{i}月" for i in range(1, 13)]
        price_data = {
            "月份": months,
            "猪霸王": [16,20,27,30,16,18,12,15,13,18,17,20],
            "中山路复记老友粉": [18,19,20,15,17,25,25,27,20,14,12,22],
            "螺遇牛": [17,18,10,19,25,30,20,14,18,19,27,21],
            "三品王": [13,14,10,17,11,15,19,16,20,15,27,17],
            "水街老牌糯米饭": [15,17,26,17,37,17,18,28,17,16,21,19]
        }
        df_price = pd.DataFrame(price_data)

        time_data = {
            "时段": ["11:00", "12:00", "13:00", "17:00", "18:00", "19:00", "20:00"],
            "猪霸王": [30, 50, 40, 25, 45, 55, 40],
            "中山路复记老友粉": [20, 15, 10, 35, 40, 30, 25],
            "螺遇牛":[30,25,16,45,34,78,54]
        }
        df_time = pd.DataFrame(time_data)

        st.markdown('### <div class="section-title map-icon">📍美食店铺分布</div>', unsafe_allow_html=True)
        with st.container():
            st.map(df_rest, latitude="纬度", longitude="经度", size="评分", color="#3B82F6", zoom=13)

        st.markdown('### <div class="section-title rating-icon">⭐餐厅评分</div>', unsafe_allow_html=True)
        with st.container():
            st.bar_chart(df_rest, x="店铺名称", y="评分", color="#3B82F6", height=400)

        st.markdown('### <div class="section-title price-icon">💰不同类型餐厅价格（12个月）</div>', unsafe_allow_html=True)
        with st.container():
            st.line_chart(df_price, x="月份", y=df_price.columns[1:], height=400, 
                        color=["#3B82F6", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6"])

        st.markdown('### <div class="section-title time-icon">🕛用餐高峰时段</div>', unsafe_allow_html=True)
        with st.container():
            st.area_chart(df_time, x="时段", y=df_time.columns[1:], height=400,
                        color=["#3B82F6", "#10B981", "#F59E0B"])

# ======================== Tab3: 个人简历生成器 ========================
with tab3:
    with st.container(border=True):
        # 全局样式定义
        st.markdown("""
            <style>
                /* 全局背景与文字 */
                .stApp {
                    background-color: #F8FBFF;
                    color: #333333;
                }
                /* 输入框/下拉框样式 */
                .stTextInput > div > div > input,
                .stSelectbox > div > div > select,
                .stDateInput > div > div > input,
                .stTextArea > div > div > textarea,
                .stNumberInput > div > div > input {
                    background-color: #FFFFFF;
                    color: #333333;
                    border: 1px solid #E0E7FF;
                    border-radius: 6px;
                    box-shadow: 0 2px 4px rgba(224, 231, 255, 0.5);
                }
                /* 按钮样式 */
                .stButton > button {
                    background-color: #4F46E5;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    box-shadow: 0 2px 4px rgba(79, 70, 229, 0.2);
                }
                .stButton > button:hover {
                    background-color: #4338CA;
                }
                /* 分隔线 */
                .divider {
                    height: 1px;
                    background-color: #E0E7FF;
                    margin: 15px 0;
                }
                /* 预览区卡片样式（清新风） */
                .preview-card {
                    background-color: #FFFFFF;
                    padding: 24px;
                    border-radius: 10px;
                    margin-bottom: 20px;
                    box-shadow: 0 4px 12px rgba(224, 231, 255, 0.6);
                    border-left: 4px solid #60A5FA;
                }
                /* 标题样式 */
                .stTitle, .stSubheader {
                    color: #1E40AF;
                }
                /* 证件照容器（固定尺寸+居中） */
                .avatar-container {
                    width: 120px;
                    height: 160px; /* 1寸证件照比例 */
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    overflow: hidden;
                    border-radius: 8px;
                    border: 2px solid #E0E7FF;
                    background-color: #F0F4FF;
                }
                /* 证件照图片（强制适配容器） */
                .avatar-img {
                    width: 100%;
                    height: 100%;
                    object-fit: cover; /* 保持比例，裁剪多余部分 */
                }
                /* 技能标签样式 */
                .skill-tag {
                    display: inline-block;
                    background-color: #EEF2FF;
                    color: #4F46E5;
                    padding: 4px 12px;
                    border-radius: 20px;
                    margin: 0 4px 8px 0;
                    font-size: 14px;
                }
            </style>
        """, unsafe_allow_html=True)

        # 图片转base64函数（用于HTML渲染）
        def image_to_base64(image):
            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            return base64.b64encode(buffer.getvalue()).decode()

        # 初始化会话状态
        if "resume_data" not in st.session_state:
            st.session_state.resume_data = {
                "name": "",
                "position": "",
                "phone": "",
                "email": "",
                "address": "",
                "birthday": "2000-01-01",
                "gender": "男",
                "education": "本科",
                "major": "",
                "skills": [],
                "work_years": 0,
                "salary_min": 5000,
                "salary_max": 8000,
                "job_start_date": "2024-1",
                "self_intro": "个人简介："
            }

        if "avatar" not in st.session_state:
            st.session_state.avatar = None
        if "avatar_base64" not in st.session_state:
            st.session_state.avatar_base64 = None

        # 分栏布局
        col_form, col_preview = st.columns([0.4, 0.6], gap="large")

        with col_form:
            st.title("✏️ 个人简历生成器")
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

            # 基础信息
            st.subheader("基础信息", anchor=False)
            st.session_state.resume_data["name"] = st.text_input("姓名", value=st.session_state.resume_data["name"])
            st.session_state.resume_data["position"] = st.text_input("求职职位", value=st.session_state.resume_data["position"])
            
            # 联系方式行布局
            col_phone, col_email = st.columns(2)
            with col_phone:
                st.session_state.resume_data["phone"] = st.text_input("电话", value=st.session_state.resume_data["phone"])
            with col_email:
                st.session_state.resume_data["email"] = st.text_input("邮箱", value=st.session_state.resume_data["email"])
            
            st.session_state.resume_data["address"] = st.text_input("现居地址", value=st.session_state.resume_data["address"])
            
            # 个人信息行布局
            col_birth, col_gender = st.columns(2)
            with col_birth:
                st.session_state.resume_data["birthday"] = st.date_input(
                    "出生日期", 
                    value=pd.to_datetime(st.session_state.resume_data["birthday"])
                ).strftime("%Y-%m-%d")
            with col_gender:
                st.session_state.resume_data["gender"] = st.radio(
                    "性别", ["男", "女", "其他"], 
                    index=["男", "女", "其他"].index(st.session_state.resume_data["gender"]),
                    horizontal=True
                )

            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

            # 教育工作
            st.subheader("教育与工作", anchor=False)
            col_edu, col_major = st.columns(2)
            with col_edu:
                st.session_state.resume_data["education"] = st.selectbox(
                    "学历", ["本科", "专科", "硕士", "博士"],
                    index=["本科", "专科", "硕士", "博士"].index(st.session_state.resume_data["education"])
                )
            with col_major:
                st.session_state.resume_data["major"] = st.text_input("专业", value=st.session_state.resume_data["major"])
            
            st.session_state.resume_data["work_years"] = st.slider(
                "工作经验（年）", 
                min_value=0, max_value=20, 
                value=st.session_state.resume_data["work_years"],
                help="拖动滑块选择工作年限"
            )

            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

            # 求职期望
            st.subheader("求职期望", anchor=False)
            col_sal_min, col_sal_max = st.columns(2)
            with col_sal_min:
                st.session_state.resume_data["salary_min"] = st.number_input(
                    "期望薪资（最低/月）", 
                    min_value=0, value=st.session_state.resume_data["salary_min"]
                )
            with col_sal_max:
                st.session_state.resume_data["salary_max"] = st.number_input(
                    "期望薪资（最高/月）", 
                    min_value=0, value=st.session_state.resume_data["salary_max"]
                )
            
            st.session_state.resume_data["job_start_date"] = st.selectbox(
                "最早入职时间", 
                ["2024-1", "2024-2", "2024-3", "2024-4"],
                index=["2024-1", "2024-2", "2024-3", "2024-4"].index(st.session_state.resume_data["job_start_date"])
            )

            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

            # 技能与简介
            st.subheader("技能与简介", anchor=False)
            st.session_state.resume_data["skills"] = st.multiselect(
                "掌握技能", 
                ["HTML/CSS", "Python", "Java", "UI设计", "SQL", "JavaScript"],
                default=st.session_state.resume_data["skills"],
                help="可多选技能"
            )
            
            st.session_state.resume_data["self_intro"] = st.text_area(
                "个人简介", 
                value=st.session_state.resume_data["self_intro"],
                height=120
            )

            # 证件照上传
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            st.subheader("证件照上传", anchor=False)
            uploaded_avatar = st.file_uploader(
                "上传证件照（建议尺寸：1寸/2寸，支持JPG/PNG）",
                type=["jpg", "jpeg", "png"],
                help="支持JPG、PNG格式的证件照，大小不超过5MB"
            )
            
            if uploaded_avatar is not None:
                image = Image.open(uploaded_avatar)
                max_size = (800, 800)
                image.thumbnail(max_size)
                st.session_state.avatar = image
                # 转base64用于HTML渲染
                st.session_state.avatar_base64 = image_to_base64(image)
                
                # 表单内预览（HTML方式）
                st.markdown("### 预览")
                st.markdown(f"""
                    <div class="avatar-container">
                        <img src="data:image/png;base64,{st.session_state.avatar_base64}" class="avatar-img">
                    </div>
                """, unsafe_allow_html=True)

        with col_preview:
            st.title("👀 简历实时预览")
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

            # 简历预览卡片（基础信息+证件照）
            st.markdown('<div class="preview-card">', unsafe_allow_html=True)
            
            # 证件照+信息网格布局（垂直居中对齐）
            st.markdown("""
                <div style="display: grid; grid-template-columns: 120px 1fr; align-items: center; gap: 16px;">
            """, unsafe_allow_html=True)
            
            # 证件照区域
            if st.session_state.avatar_base64 is not None:
                st.markdown(f"""
                    <div class="avatar-container">
                        <img src="data:image/png;base64,{st.session_state.avatar_base64}" class="avatar-img">
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="avatar-container">
                        <span style="color: #94A3B8; font-size: 12px;">暂无照片</span>
                    </div>
                """, unsafe_allow_html=True)
            
            # 信息区域（姓名+求职意向+联系方式）
            name = st.session_state.resume_data['name'] or '未填写姓名'
            position = st.session_state.resume_data['position'] or '未填写求职职位'
            phone = st.session_state.resume_data['phone'] or '未填写'
            email = st.session_state.resume_data['email'] or '未填写'
            address = st.session_state.resume_data['address'] or '未填写'
            birthday = st.session_state.resume_data['birthday']
            gender = st.session_state.resume_data['gender']
            
            st.markdown(f"""
                <div>
                    <h3 style="margin: 0; color: #1E40AF;">{name}</h3>
                    <p style="margin: 4px 0; color: #666;">求职意向：{position}</p>
                    <div style="display: flex; flex-wrap: wrap; gap: 16px; margin-top: 8px; font-size: 14px;">
                        <p style="margin: 0;"><span>📞</span> {phone}</p>
                        <p style="margin: 0;"><span>📧</span> {email}</p>
                        <p style="margin: 0;"><span>📍</span> {address}</p>
                        <p style="margin: 0;"><span>🎂</span> {birthday}</p>
                        <p style="margin: 0;"><span>⚥</span> {gender}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)  # 关闭网格布局
            st.markdown('</div>', unsafe_allow_html=True)  # 关闭preview-card

            # 教育与工作经历
            st.markdown('<div class="preview-card" style="border-left: 4px solid #34D399;">', unsafe_allow_html=True)
            st.subheader("教育与工作经历", anchor=False)
            col_edu, col_work = st.columns(2)
            with col_edu:
                st.write(f"**学历：** {st.session_state.resume_data['education']}")
                st.write(f"**专业：** {st.session_state.resume_data['major'] or '未填写'}")
            with col_work:
                st.write(f"**工作经验：** {st.session_state.resume_data['work_years']}年")
                st.write(f"**最早入职：** {st.session_state.resume_data['job_start_date']}")
            st.markdown('</div>', unsafe_allow_html=True)

            # 求职期望
            st.markdown('<div class="preview-card" style="border-left: 4px solid #A78BFA;">', unsafe_allow_html=True)
            st.subheader("求职期望", anchor=False)
            st.write(f"**期望薪资：** {st.session_state.resume_data['salary_min']} - {st.session_state.resume_data['salary_max']} 元/月")
            st.markdown('</div>', unsafe_allow_html=True)

            # 技能与个人简介
            st.markdown('<div class="preview-card" style="border-left: 4px solid #FBBF24;">', unsafe_allow_html=True)
            st.subheader("技能与个人简介", anchor=False)
            
            # 技能标签化展示
            st.write("**掌握技能：**")
            if st.session_state.resume_data["skills"]:
                skill_tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in st.session_state.resume_data["skills"]])
                st.markdown(skill_tags, unsafe_allow_html=True)
            else:
                st.write("未填写")
            
            # 个人简介
            st.write("**个人简介：**")
            st.write(st.session_state.resume_data["self_intro"])
            st.markdown('</div>', unsafe_allow_html=True)

            # 底部标语
            st.markdown(
                '<p style="text-align: center; color: #6B7280; margin-top: 30px;">保持热爱，奔赴下一场山海 🌱</p>',
                unsafe_allow_html=True
            )

# ======================== Tab4: 相册 ========================
with tab4:
    with st.container(border=True):
        # 修改标签页的文字和图标
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

# ======================== Tab5: 音乐播放器 ========================
with tab5:
    with st.container(border=True):
        # 页面配置：音乐播放器主题
        st.title("简易音乐播放器")
        st.caption("使用Streamlit制作的音乐播放器，支持切换与基础信息展示")

        # 1. 初始化状态：存储当前音乐索引
        if 'music_ind' not in st.session_state:
            st.session_state['music_ind'] = 0

        # 2. 音乐数据：包含封面、歌曲名、歌手、时长、音乐链接（注：需用可公开访问的音频URL）
        music_list = [
        {
                "cover": "http://p2.music.126.net/wRDGhwhhzJuUkWMrjrPwKw==/109951172137146717.jpg?param=130y130",
                "title": "Blue Valentine",
                "singer": "NMIXX",
                "duration": "03：06",
                "audio_url": "https://music.163.com/song/media/outer/url?id=8499257255.mp3"  # 替换为实际可访问的音频URL
            },
            {
                "cover": "http://p1.music.126.net/srse1pR1hPtnBIrGcqHvNA==/109951169939972270.jpg?param=130y130",
                "title": "ONCE AGAIN",
                "singer": "WINTER / NINGNING",
                "duration": "02：49",
                "audio_url": "https://music.163.com/song/media/outer/url?id=1949928569.mp3"  # 替换为实际可访问的音频URL
            },
            
            {
                "cover": "http://p2.music.126.net/FTzl-oT9JIKFvQzkDibibw==/109951169721143692.jpg?param=130y130",
                "title": "BAHAMA",
                "singer": "aespa",
                "duration": "03:10",
                "audio_url": "https://music.163.com/song/media/outer/url?id=2160419150.mp3"  # 替换为实际可访问的音频URL
            }
        ]

        # 3. 获取当前播放的音乐信息
        current_music = music_list[st.session_state['music_ind']]

        # 4. 布局：封面+歌曲信息（左右排列）
        col_cover, col_info = st.columns([1, 2])
        with col_cover:
            st.image(current_music["cover"], caption="专辑封面", width=150)
        with col_info:
            st.subheader(current_music["title"])
            st.write(f"歌手: {current_music['singer']}")
            st.write(f"时长: {current_music['duration']}")

        # 5. 音乐播放组件（Streamlit原生audio组件）
        st.audio(current_music["audio_url"], format="audio/mp3")

        # 6. 切换函数：上一首/下一首（循环切换）
        def prev_music():
            st.session_state['music_ind'] = (st.session_state['music_ind'] - 1) % len(music_list)

        def next_music():
            st.session_state['music_ind'] = (st.session_state['music_ind'] + 1) % len(music_list)

        # 7. 切换按钮
        col_prev, col_next = st.columns(2)
        with col_prev:
            st.button("◀️ 上一首", on_click=prev_music)
        with col_next:
            st.button("下一首 ▶️", on_click=next_music)

# ======================== Tab6: 视频网站 ========================
with tab6:
    with st.container(border=True):
        # -------------------- 0. 页面配置 --------------------
        st.title("还珠格格 · 少女心专场")
        st.caption("少女风视频播放页面")

        # -------------------- 1. 全局少女风 CSS --------------------
        st.markdown("""
        <style>
        /* 1. 马卡龙渐变背景 + 云朵纹理 */
        body, .main {
            background: linear-gradient(135deg, #fff0f8 0%, #ffeaf4 50%, #fff5f9 100%);
            background-image:
                radial-gradient(circle at 10% 20%, rgba(255,255,255,0.8) 0%, transparent 20%),
                radial-gradient(circle at 90% 80%, rgba(255,255,255,0.6) 0%, transparent 25%);
            font-family: "Quicksand", "PingFang SC", sans-serif;
        }

        /* 2. 闪光软萌标题 */
        .main-title {
            text-align: center;
            font-size: 2.6rem;
            font-weight: 700;
            letter-spacing: 3px;
            margin: 20px 0 10px 0;
            background: linear-gradient(45deg, #ff85a2, #ffc2d1, #ff85a2);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shine 3s ease infinite;
        }
        @keyframes shine {
            0%{background-position:0% 50%}
            50%{background-position:100% 50%}
            100%{background-position:0% 50%}
        }

        /* 3. 视频奶油卡片 */
        .video-card {
            display: flex;
            justify-content: center;
            margin: 0 auto 30px auto;
            position: relative;
            width: fit-content;
            border-radius: 18px;
            padding: 8px;
            background: white;
            box-shadow: 0 0 0 3px #ffe3f1, 0 8px 30px rgba(255, 182, 193, 0.35);
        }
        .stVideo {
            border-radius: 12px;
            overflow: hidden;
        }
        /* 四角小桃心 */
        .video-card::before,
        .video-card::after {
            content: "💗";
            position: absolute;
            font-size: 18px;
            animation: pulse 1.5s ease-in-out infinite;
        }
        .video-card::before { top: -10px; left: -10px; }
        .video-card::after  { bottom: -10px; right: -10px; }
        @keyframes pulse {
            0%,100%{transform:scale(1)}
            50%{transform:scale(1.2)}
        }

        /* 4. 糖果胶囊按钮 */
        div.stButton > button {
            height: 42px;
            border-radius: 21px;
            font-size: 15px;
            font-weight: 600;
            border: none;
            background: linear-gradient(45deg, #ffa6c9, #ffc2d1);
            color: #fff;
            box-shadow: 0 4px 15px rgba(255, 166, 201, 0.4);
            transition: all .3s ease;
        }
        div.stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(255, 166, 201, 0.6);
        }

        /* 5. 当前集跳动闪耀 */
        div.stButton > button[kind="secondary"]:disabled {
            background: linear-gradient(45deg, #ff85a2, #ffb6c1);
            animation: bounce 1s ease infinite;
            cursor: not-allowed;
        }
        @keyframes bounce {
            0%,100%{transform:translateY(0)}
            50%{transform:translateY(-5px)}
        }

        /* 6. 樱花瓣漂浮彩蛋 */
        .sakura {
            position: fixed;
            top: -20px;
            font-size: 20px;
            color: #ffb6c1;
            animation: fall 10s linear infinite;
            z-index: 9999;
        }
        @keyframes fall {
            to { transform: translateY(110vh) rotate(360deg); }
        }
        </style>
        """, unsafe_allow_html=True)

        # -------------------- 2. 数据 & session_state --------------------
        video_arr = [
            {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4", "title": "第 1 集"},
            {"url": "https://www.w3schools.com/html/movie.mp4",               "title": "第 2 集"},
            {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4",        "title": "第 3 集"},
        ]

        if "ind" not in st.session_state:
            st.session_state.ind = 0

        # -------------------- 3. 标题 --------------------
        st.markdown('<div class="main-title">还珠格格 第一部</div>', unsafe_allow_html=True)

        # -------------------- 4. 视频播放区（奶油卡片） --------------------
        with st.container():
            st.markdown('<div class="video-card">', unsafe_allow_html=True)
            st.video(video_arr[st.session_state.ind]["url"], autoplay=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # -------------------- 5. 选集按钮（原列布局不动） --------------------
        def play(i):
            st.session_state.ind = int(i)

        cols = st.columns(len(video_arr))
        for idx, col in enumerate(cols):
            with col:
                disabled = (idx == st.session_state.ind)
                st.button(
                    f"第 {idx + 1} 集",
                    use_container_width=True,
                    on_click=None if disabled else play,
                    args=(idx,) if not disabled else (),
                    disabled=disabled
                )

        # -------------------- 6. 随机樱花瓣彩蛋（纯 CSS） --------------------
        # 随机生成 3~5 片花瓣，延迟飘落
        import random
        for _ in range(random.randint(3, 5)):
            left = random.randint(0, 100)
            delay = random.randint(0, 5)
            st.markdown(f'<div class="sakura" style="left:{left}%; animation-delay:{delay}s;">🌸</div>',
                        unsafe_allow_html=True)
