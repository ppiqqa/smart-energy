import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Saudi Smart Energy System",
    page_icon="⚡",
    layout="wide"
)

# ==========================
# CSS STYLE
# ==========================

st.markdown("""
<style>

/* الخلفية */
.stApp{
background:
linear-gradient(
135deg,
#020617 0%,
#0f172a 25%,
#0b2447 50%,
#082f49 75%,
#020617 100%
);
}

/* النصوص */
h1,h2,h3,h4,h5,h6,p,label,span,div{
color:white !important;
}

/* البطاقات */
[data-testid="metric-container"]{
background:rgba(15,23,42,0.85);
border:1px solid #38bdf8;
padding:20px;
border-radius:18px;
box-shadow:0 0 15px rgba(56,189,248,.3);
}

/* الإدخالات */
.stNumberInput input{
background:#0f172a !important;
color:#38bdf8 !important;
border:1px solid #38bdf8 !important;
border-radius:12px !important;
font-size:18px !important;
}

/* القوائم */
.stSelectbox div[data-baseweb="select"]{
background:#0f172a !important;
border-radius:12px;
}

/* السايد بار */
section[data-testid="stSidebar"]{
background:#020617;
}

/* إخفاء الفوتر */
footer{
visibility:hidden;
}

header{
visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================

st.markdown("""
<div style="
padding:35px;
border-radius:25px;
background:linear-gradient(
90deg,
#0ea5e9,
#2563eb,
#1d4ed8
);
text-align:center;
box-shadow:0 0 30px rgba(59,130,246,.6);
">

<h1>⚡ SAUDI SMART ENERGY SYSTEM ⚡</h1>

<h3>Smart Electrical Load Monitoring Platform</h3>

<p>
Real-Time Monitoring • Energy Analysis • Breaker Protection
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================
# SYSTEM STATUS
# ==========================

col1,col2,col3=st.columns(3)

with col1:
    st.success("🟢 Grid Status : ONLINE")

with col2:
    st.success("🟢 System Health : GOOD")

with col3:
    st.success("🟢 Monitoring : ACTIVE")

# ==========================
# INPUTS
# ==========================

st.subheader("⚡ Device Loads")

c1,c2,c3=st.columns(3)

with c1:
    ac1=st.number_input(
        "❄️ AC1 Load (W)",
        min_value=0,
        value=2268,
        step=10,
        format="%d"
    )

with c2:
    ac2=st.number_input(
        "❄️ AC2 Load (W)",
        min_value=0,
        value=1761,
        step=10,
        format="%d"
    )

with c3:
    fridge=st.number_input(
        "🧊 Fridge Load (W)",
        min_value=0,
        value=150,
        step=10,
        format="%d"
    )

hours=st.slider(
    "⏰ Hours Per Day",
    1,
    24,
    8
)

breaker=st.selectbox(
    "🛡️ Breaker Rating (A)",
    [20,32,40,63]
)

# ==========================
# CALCULATIONS
# ==========================

voltage=220

total_load=ac1+ac2+fridge

current=total_load/voltage

monthly_energy=(total_load/1000)*hours*30

bill=monthly_energy*0.18

breaker_loading=(current/breaker)*100

# ==========================
# DASHBOARD
# ==========================

st.subheader("📊 System Dashboard")

d1,d2,d3,d4=st.columns(4)

d1.metric(
    "⚡ Total Load",
    f"{total_load:.0f} W"
)

d2.metric(
    "🔌 Current",
    f"{current:.2f} A"
)

d3.metric(
    "📈 Monthly Energy",
    f"{monthly_energy:.1f} kWh"
)

d4.metric(
    "💰 Estimated Bill",
    f"{bill:.2f} SAR"
)

# ==========================
# PIE CHART
# ==========================

st.subheader("📊 Load Distribution")

data=pd.DataFrame({
    "Device":["AC1","AC2","Fridge"],
    "Load":[ac1,ac2,fridge]
})

fig=px.pie(
    data,
    values="Load",
    names="Device",
    hole=0.55,
    color_discrete_sequence=[
        "#0ea5e9",
        "#38bdf8",
        "#22c55e"
    ]
)

fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="white",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# BREAKER
# ==========================

st.subheader("🛡️ Breaker Utilization")

st.progress(
    min(int(breaker_loading),100)
)

st.write(
    f"Breaker Loading = {breaker_loading:.1f}%"
)

# ==========================
# STATUS
# ==========================

if current < breaker*0.6:
    st.success("✅ SAFE LOAD")

elif current < breaker*0.8:
    st.warning("⚠️ HIGH LOAD")

else:
    st.error("🚨 OVERLOAD")

# ==========================
# RECOMMENDATIONS
# ==========================

st.subheader("📈 System Recommendations")

if current > breaker*0.8:
    st.error(
        "Reduce electrical load immediately."
    )

elif current > breaker*0.6:
    st.warning(
        "Electrical load approaching breaker limit."
    )

else:
    st.success(
        "Electrical load operating safely."
    )

# ==========================
# TIPS
# ==========================

st.subheader("💡 Energy Saving Tips")

st.info("""
• Clean AC filters regularly

• Turn off unused devices

• Use high efficiency appliances

• Reduce unnecessary operating hours

• Avoid simultaneous heavy loads
""")

# ==========================
# SYSTEM INFO
# ==========================

st.subheader("📋 System Information")

st.success("""
⚡ Real-Time Monitoring Enabled

⚡ Load Analysis Running

⚡ Monthly Bill Estimation Active

⚡ Breaker Protection Monitoring Active
""")

# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.markdown("""
<div style="text-align:center">

### ⚡ Saudi Smart Energy Control Center

Electrical Engineering Project

Designed by Mohammed

</div>
""", unsafe_allow_html=True)