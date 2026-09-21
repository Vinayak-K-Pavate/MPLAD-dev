import streamlit as st
import pandas as pd
import plotly.express as px


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="MPLAD Development Monitoring System",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}

.gov-header {
    background-color: white;
    padding: 18px 25px;
    border-bottom: 5px solid #ff9933;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.gov-title {
    font-size: 26px;
    font-weight: 700;
    color: #222222;
}

.gov-subtitle {
    font-size: 14px;
    color: #666666;
}

.ministry {
    text-align: right;
    font-size: 15px;
    font-weight: 600;
    color: #333333;
}

.hero {
    background: linear-gradient(
        rgba(0,0,0,0.65),
        rgba(0,0,0,0.65)
    );
    padding: 65px 35px;
    border-radius: 10px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 40px;
    font-weight: 700;
}

.hero-subtitle {
    font-size: 20px;
    margin-top: 10px;
}

.hero-description {
    font-size: 15px;
    margin-top: 20px;
}

.stat-card {
    background-color: white;
    padding: 25px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
    border-top: 5px solid #ff9933;
}

.stat-number {
    font-size: 30px;
    font-weight: bold;
    color: #138808;
}

.stat-label {
    color: #555555;
    font-size: 15px;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 15px;
    color: #222222;
}

.rule-box {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 12px;
    border-left: 5px solid #138808;
}

.footer {
    background-color: #222222;
    color: white;
    padding: 25px;
    text-align: center;
    margin-top: 50px;
}

.login-box {
    background-color: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# DEMO DATA
# ---------------------------------------------------------

projects = pd.DataFrame({

    "Project ID": [
        "MPLAD001",
        "MPLAD002",
        "MPLAD003",
        "MPLAD004",
        "MPLAD005",
        "MPLAD006"
    ],

    "Project": [
        "Community Hall Construction",
        "Rural Road Development",
        "Government School Improvement",
        "Drinking Water Facility",
        "Public Library",
        "Health Centre Development"
    ],

    "State": [
        "Karnataka",
        "Karnataka",
        "Maharashtra",
        "Tamil Nadu",
        "Karnataka",
        "Maharashtra"
    ],

    "District": [
        "Dharwad",
        "Belagavi",
        "Pune",
        "Chennai",
        "Dharwad",
        "Nagpur"
    ],

    "Taluka": [
        "Dharwad",
        "Athani",
        "Haveli",
        "Ambattur",
        "Hubballi",
        "Katol"
    ],

    "Status": [
        "Completed",
        "Ongoing",
        "Completed",
        "Ongoing",
        "Completed",
        "Ongoing"
    ],

    "Sanctioned Amount": [
        2500000,
        3500000,
        1800000,
        2200000,
        1500000,
        3000000
    ],

    "Utilized Amount": [
        2500000,
        1900000,
        1800000,
        1100000,
        1500000,
        900000
    ]

})


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_type" not in st.session_state:
    st.session_state.user_type = ""

if "username" not in st.session_state:
    st.session_state.username = ""


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown("""
<div class="gov-header">

<div>

<div class="gov-title">
🇮🇳 MPLAD Development Monitoring System
</div>

<div class="gov-subtitle">
Members of Parliament Local Area Development Scheme
</div>

</div>

<div class="ministry">

Ministry of Infrastructure, Housing<br>
and Urban Development

</div>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# LOGIN FUNCTION
# ---------------------------------------------------------

def login_page():

    st.markdown(
        "<h1 style='text-align:center;'>Official Login</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>Access the MPLAD Monitoring Portal</p>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown('<div class="login-box">', unsafe_allow_html=True)

        user_type = st.selectbox(
            "User Type",
            [
                "Central Level",
                "District Level",
                "Taluka Level",
                "Inspection Authority"
            ]
        )

        username = st.text_input(
            "User ID"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        login = st.button(
            "Login",
            use_container_width=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

        if login:

            if username and password:

                st.session_state.logged_in = True
                st.session_state.user_type = user_type
                st.session_state.username = username

                st.success(
                    f"Successfully logged in as {user_type}"
                )

                st.rerun()

            else:

                st.error(
                    "Please enter User ID and Password."
                )


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg",
        width=100
    )

    st.title("MPLAD Portal")

    if st.session_state.logged_in:

        st.success(
            st.session_state.user_type
        )

        menu = st.radio(
            "Navigation",
            [
                "Dashboard",
                "Development",
                "Funds",
                "Rules & Regulations",
                "Inspection"
            ]
        )

        st.divider()

        if st.button(
            "Logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False
            st.session_state.user_type = ""
            st.session_state.username = ""

            st.rerun()

    else:

        menu = st.radio(
            "Navigation",
            [
                "Home",
                "Development",
                "Funds",
                "Rules & Regulations",
                "Login"
            ]
        )


# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------

def home_page():

    st.markdown("""
    <div class="hero">

        <div class="hero-title">
            MPLAD Development Monitoring System
        </div>

        <div class="hero-subtitle">
            Transparent Development • Efficient Monitoring • Accountable Governance
        </div>

        <div class="hero-description">
            A centralized platform for monitoring development
            projects, fund utilization and implementation
            under the Members of Parliament Local Area
            Development Scheme.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Development Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown("""
        <div class="stat-card">

        <div class="stat-number">
        12,450
        </div>

        <div class="stat-label">
        Total Projects
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="stat-card">

        <div class="stat-number">
        8,920
        </div>

        <div class="stat-label">
        Completed Projects
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="stat-card">

        <div class="stat-number">
        3,530
        </div>

        <div class="stat-label">
        Ongoing Projects
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown("""
        <div class="stat-card">

        <div class="stat-number">
        ₹4,250 Cr
        </div>

        <div class="stat-label">
        Funds Released
        </div>

        </div>
        """, unsafe_allow_html=True)


    st.markdown(
        '<div class="section-title">Development Status</div>',
        unsafe_allow_html=True
    )

    status_count = projects["Status"].value_counts().reset_index()

    status_count.columns = [
        "Status",
        "Count"
    ]

    fig = px.pie(
        status_count,
        names="Status",
        values="Count",
        hole=0.45,
        title="Project Status"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ---------------------------------------------------------
# DEVELOPMENT PAGE
# ---------------------------------------------------------

def development_page():

    st.markdown(
        '<div class="section-title">Development Projects</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Monitor completed and ongoing development projects."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        state = st.selectbox(
            "State",
            ["All"] + sorted(
                projects["State"].unique().tolist()
            )
        )

    with col2:

        district = st.selectbox(
            "District",
            ["All"] + sorted(
                projects["District"].unique().tolist()
            )
        )

    with col3:

        status = st.selectbox(
            "Project Status",
            [
                "All",
                "Completed",
                "Ongoing"
            ]
        )


    filtered = projects.copy()


    if state != "All":

        filtered = filtered[
            filtered["State"] == state
        ]


    if district != "All":

        filtered = filtered[
            filtered["District"] == district
        ]


    if status != "All":

        filtered = filtered[
            filtered["Status"] == status
        ]


    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )


# ---------------------------------------------------------
# FUNDS PAGE
# ---------------------------------------------------------

def funds_page():

    st.markdown(
        '<div class="section-title">Fund Monitoring</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Track released, utilized and remaining funds."
    )

    total_sanctioned = projects[
        "Sanctioned Amount"
    ].sum()

    total_utilized = projects[
        "Utilized Amount"
    ].sum()

    remaining = (
        total_sanctioned -
        total_utilized
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Total Funds Released",
            "₹4,250 Cr"
        )


    with col2:

        st.metric(
            "Funds Utilized",
            "₹3,480 Cr"
        )


    with col3:

        st.metric(
            "Remaining Funds",
            "₹770 Cr"
        )


    st.divider()


    fund_data = pd.DataFrame({

        "Category": [
            "Released",
            "Utilized",
            "Remaining"
        ],

        "Amount": [
            4250,
            3480,
            770
        ]

    })


    fig = px.bar(
        fund_data,
        x="Category",
        y="Amount",
        title="MPLAD Fund Position",
        text="Amount"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.subheader(
        "Project-wise Fund Utilization"
    )

    fund_table = projects[
        [
            "Project ID",
            "Project",
            "Sanctioned Amount",
            "Utilized Amount"
        ]
    ].copy()


    fund_table[
        "Remaining Amount"
    ] = (
        fund_table["Sanctioned Amount"]
        -
        fund_table["Utilized Amount"]
    )


    st.dataframe(
        fund_table,
        use_container_width=True,
        hide_index=True
    )


# ---------------------------------------------------------
# RULES PAGE
# ---------------------------------------------------------

def rules_page():

    st.markdown(
        '<div class="section-title">Rules & Regulations</div>',
        unsafe_allow_html=True
    )

    rules = [

        (
            "MPLAD Guidelines",
            "Official guidelines governing the implementation "
            "and monitoring of MPLAD projects."
        ),

        (
            "Fund Utilization",
            "Funds must be utilized only for eligible "
            "development works according to applicable "
            "government guidelines."
        ),

        (
            "Project Monitoring",
            "Development projects should be monitored "
            "and inspected at appropriate administrative levels."
        ),

        (
            "Transparency and Accountability",
            "Project information, fund utilization and "
            "implementation status should be maintained "
            "for monitoring and accountability."
        ),

        (
            "Inspection Requirements",
            "Authorized inspection authorities may inspect "
            "project implementation and verify the reported "
            "status of development works."
        )

    ]


    for title, description in rules:

        st.markdown(
            f"""
            <div class="rule-box">

            <h3>{title}</h3>

            <p>{description}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# INSPECTION PAGE
# ---------------------------------------------------------

def inspection_page():

    st.markdown(
        '<div class="section-title">Inspection Authority</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Inspection authorities can monitor projects "
        "across the system."
    )


    if st.session_state.user_type != "Inspection Authority":

        st.warning(
            "This section is intended for Inspection Authority users."
        )

        return


    st.success(
        "Inspection Authority access enabled."
    )


    inspection_project = st.selectbox(
        "Select Project",
        projects["Project"]
    )


    selected = projects[
        projects["Project"] ==
        inspection_project
    ].iloc[0]


    st.subheader(
        "Project Details"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.write(
            f"**Project ID:** {selected['Project ID']}"
        )

        st.write(
            f"**State:** {selected['State']}"
        )

        st.write(
            f"**District:** {selected['District']}"
        )

        st.write(
            f"**Taluka:** {selected['Taluka']}"
        )


    with col2:

        st.write(
            f"**Status:** {selected['Status']}"
        )

        st.write(
            f"**Sanctioned Amount:** ₹{selected['Sanctioned Amount']:,}"
        )

        st.write(
            f"**Utilized Amount:** ₹{selected['Utilized Amount']:,}"
        )


    st.subheader(
        "Inspection Status"
    )


    inspection_status = st.selectbox(
        "Inspection Result",
        [
            "Pending",
            "Verified",
            "Requires Further Inspection"
        ]
    )


    remarks = st.text_area(
        "Inspection Remarks"
    )


    if st.button(
        "Submit Inspection Report"
    ):

        st.success(
            "Inspection report submitted successfully."
        )


# ---------------------------------------------------------
# DASHBOARD
# ---------------------------------------------------------

def dashboard_page():

    user_type = st.session_state.user_type

    st.title(
        f"{user_type} Dashboard"
    )

    st.write(
        f"Welcome, {st.session_state.username}"
    )


    if user_type == "Central Level":

        st.info(
            "Central Level users can view development "
            "information for the entire country."
        )

        home_page()


    elif user_type == "District Level":

        st.info(
            "District Level users can view their district "
            "and the talukas under that district."
        )

        development_page()


    elif user_type == "Taluka Level":

        st.info(
            "Taluka Level users can view projects "
            "within their assigned taluka."
        )

        development_page()


    elif user_type == "Inspection Authority":

        st.info(
            "Inspection Authority users can inspect "
            "projects across the system."
        )

        inspection_page()


# ---------------------------------------------------------
# PAGE ROUTING
# ---------------------------------------------------------

if not st.session_state.logged_in:

    if menu == "Home":

        home_page()

    elif menu == "Development":

        development_page()

    elif menu == "Funds":

        funds_page()

    elif menu == "Rules & Regulations":

        rules_page()

    elif menu == "Login":

        login_page()


else:

    if menu == "Dashboard":

        dashboard_page()

    elif menu == "Development":

        development_page()

    elif menu == "Funds":

        funds_page()

    elif menu == "Rules & Regulations":

        rules_page()

    elif menu == "Inspection":

        inspection_page()


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("""
<div class="footer">

<p><b>Government of India</b></p>

<p>MPLAD Development Monitoring System</p>

<p>
Development Monitoring • Fund Transparency •
Project Inspection
</p>

<p>
© MPLAD Monitoring Portal
</p>

</div>
""", unsafe_allow_html=True)