import streamlit as st
import pandas as pd
from PIL import Image
import io
import base64

st.set_page_config(
    page_title="个人简历生成器",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
