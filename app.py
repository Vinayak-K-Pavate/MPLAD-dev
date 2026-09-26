import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="MPLAD Monitoring System",
    page_icon="🇮🇳",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fa;
    }

    .gov-header {
        background-color: white;
        padding: 20px;
        border-bottom: 5px solid #ff9933;
        margin-bottom: 20px;
    }

    .gov-title {
        font-size: 28px;
        font-weight: bold;
        color: #222222;
    }

    .gov-subtitle {
        font-size: 15px;
        color: #666666;
        margin-top: 5px;
    }

    .ministry {
        text-align: right;
        font-size: 15px;
        font-weight: bold;
        color: #333333;
    }

    .hero {
        background-color: #243447;
        padding: 50px 30px;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }

    .hero-title {
        font-size: 38px;
        font-weight: bold;
    }

    .hero-subtitle {
        font-size: 20px;
        margin-top: 12px;
    }

    .hero-text {
        font-size: 15px;
        margin-top: 20px;
        line-height: 1.6;
    }

    .stat-card {
        background-color: white;
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        border-top: 5px solid #ff9933;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    }

    .stat-number {
        font-size: 30px;
        font-weight: bold;
        color: #138808;
    }

    .stat-label {
        font-size: 15px;
        color: #555555;
        margin-top: 8px;
    }

    .section-title {
        font-size: 28px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .rule-box {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #138808;
        margin-bottom: 15px;
    }

    .footer {
        background-color: #222222;
        color: white;
        padding: 25px;
        text-align: center;
        margin-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DEMO PROJECT DATA
# =========================================================

projects = pd.DataFrame(
    {
        "Project ID": [
            "MPLAD001",
            "MPLAD002",
            "MPLAD003",
            "MPLAD004",
            "MPLAD005",
            "MPLAD006",
            "MPLAD007",
            "MPLAD008"
        ],
        "Project": [
            "Community Hall Construction",
            "Rural Road Development",
            "Government School Improvement",
            "Drinking Water Facility",
            "Public Library",
            "Health Centre Development",
            "Village Drainage Project",
            "Community Park Development"
        ],
        "State": [
            "Karnataka",
            "Karnataka",
            "Maharashtra",
            "Tamil Nadu",
            "Karnataka",
            "Maharashtra",
            "Karnataka",
            "Tamil Nadu"
        ],
        "District": [
            "Dharwad",
            "Belagavi",
            "Pune",
            "Chennai",
            "Dharwad",
            "Nagpur",
            "Mysuru",
            "Madurai"
        ],
        "Taluka": [
            "Dharwad",
            "Athani",
            "Haveli",
            "Ambattur",
            "Hubballi",
            "Katol",
            "Mysuru",
            "Melur"
        ],
        "Status": [
            "Completed",
            "Ongoing",
            "Completed",
            "Ongoing",
            "Completed",
            "Ongoing",
            "Ongoing",
            "Completed"
        ],
        "Sanctioned Amount": [
            2500000,
            3500000,
            1800000,
            2200000,
            1500000,
            3000000,
            2700000,
            1900000
        ],
        "Utilized Amount": [
            2500000,
            1900000,
            1800000,
            1100000,
            1500000,
            900000,
            1300000,
            1900000
        ]
    }
)


# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_type" not in st.session_state:
    st.session_state.user_type = ""

if "username" not in st.session_state:
    st.session_state.username = ""


# =========================================================
# HEADER
# =========================================================

col1, col2 = st.columns([3, 1])

with col1:

    st.markdown(
        """
        <div class="gov-header">

        <div class="gov-title">
        🇮🇳 MPLAD Development Monitoring System
        </div>

        <div class="gov-subtitle">
        Members of Parliament Local Area Development Scheme
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="gov-header">

        <div class="ministry">
        Ministry of Infrastructure, Housing
        <br>
        and Urban Development
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HOME PAGE
# =========================================================

def home_page():

    st.markdown(
        """
        <div class="hero">

        <div class="hero-title">
        MPLAD Development Monitoring System
        </div>

        <div class="hero-subtitle">
        Transparent Development • Efficient Monitoring •
        Accountable Governance
        </div>

        <div class="hero-text">
        A centralized platform for monitoring development
        projects, fund utilization and implementation under
        the Members of Parliament Local Area Development Scheme.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Development Overview</div>',
        unsafe_allow_html=True
    )

    total_projects = len(projects)

    completed_projects = len(
        projects[projects["Status"] == "Completed"]
    )

    ongoing_projects = len(
        projects[projects["Status"] == "Ongoing"]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            f"""
            <div class="stat-card">

            <div class="stat-number">
            {total_projects}
            </div>

            <div class="stat-label">
            Total Projects
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="stat-card">

            <div class="stat-number">
            {completed_projects}
            </div>

            <div class="stat-label">
            Completed Projects
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="stat-card">

            <div class="stat-number">
            {ongoing_projects}
            </div>

            <div class="stat-label">
            Ongoing Projects
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            """
            <div class="stat-card">

            <div class="stat-number">
            ₹4,250 Cr
            </div>

            <div class="stat-label">
            Funds Released
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown(
        '<div class="section-title">Project Status</div>',
        unsafe_allow_html=True
    )

    status_data = (
        projects["Status"]
        .value_counts()
        .reset_index()
    )

    status_data.columns = [
        "Status",
        "Projects"
    ]

    fig = px.pie(
        status_data,
        names="Status",
        values="Projects",
        hole=0.4,
        title="Completed vs Ongoing Projects"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# DEVELOPMENT PAGE
# =========================================================

def development_page():

    st.markdown(
        '<div class="section-title">Development Projects</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Search and monitor development projects."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        state_list = ["All"] + sorted(
            projects["State"].unique().tolist()
        )

        selected_state = st.selectbox(
            "Select State",
            state_list
        )

    with col2:

        district_list = ["All"] + sorted(
            projects["District"].unique().tolist()
        )

        selected_district = st.selectbox(
            "Select District",
            district_list
        )

    with col3:

        selected_status = st.selectbox(
            "Select Status",
            [
                "All",
                "Completed",
                "Ongoing"
            ]
        )


    filtered = projects.copy()


    if selected_state != "All":

        filtered = filtered[
            filtered["State"] == selected_state
        ]


    if selected_district != "All":

        filtered = filtered[
            filtered["District"] == selected_district
        ]


    if selected_status != "All":

        filtered = filtered[
            filtered["Status"] == selected_status
        ]


    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# FUNDS PAGE
# =========================================================

def funds_page():

    st.markdown(
        '<div class="section-title">Fund Monitoring</div>',
        unsafe_allow_html=True
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


    fund_data = pd.DataFrame(
        {
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
        }
    )


    fig = px.bar(
        fund_data,
        x="Category",
        y="Amount",
        text="Amount",
        title="Fund Position (Demo Data)"
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
            "State",
            "District",
            "Sanctioned Amount",
            "Utilized Amount"
        ]
    ].copy()


    fund_table["Remaining Amount"] = (
        fund_table["Sanctioned Amount"]
        -
        fund_table["Utilized Amount"]
    )


    st.dataframe(
        fund_table,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# RULES PAGE
# =========================================================

def rules_page():

    st.markdown(
        '<div class="section-title">Rules & Regulations</div>',
        unsafe_allow_html=True
    )

    rules = [
        (
            "MPLAD Guidelines",
            "Guidelines governing implementation and "
            "monitoring of MPLAD development projects."
        ),
        (
            "Fund Utilization",
            "Funds should be utilized only for eligible "
            "development works according to applicable "
            "government guidelines."
        ),
        (
            "Project Monitoring",
            "Development projects should be monitored "
            "at appropriate administrative levels."
        ),
        (
            "Transparency and Accountability",
            "Project information and fund utilization "
            "should be maintained for transparency and "
            "accountability."
        ),
        (
            "Inspection",
            "Authorized inspection authorities may verify "
            "the implementation and status of projects."
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


# =========================================================
# LOGIN PAGE
# =========================================================

def login_page():

    st.markdown(
        "<h1 style='text-align:center;'>Official Login</h1>",
        unsafe_allow_html=True
    )

    st.write(
        "Select your authorized user category."
    )


    col1, col2, col3 = st.columns(
        [1, 2, 1]
    )


    with col2:

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


        if st.button(
            "Login",
            use_container_width=True
        ):

            if username.strip() == "":
                st.error(
                    "Please enter User ID."
                )

            elif password.strip() == "":
                st.error(
                    "Please enter Password."
                )

            else:

                st.session_state.logged_in = True
                st.session_state.user_type = user_type
                st.session_state.username = username

                st.success(
                    "Login successful."
                )

                st.rerun()


# =========================================================
# DASHBOARD
# =========================================================

def dashboard_page():

    st.title(
        "Dashboard"
    )

    st.success(
        "Logged in as: "
        + st.session_state.user_type
    )


    if st.session_state.user_type == "Central Level":

        st.info(
            "Central Level: Access to nationwide "
            "development information."
        )

        home_page()


    elif st.session_state.user_type == "District Level":

        st.info(
            "District Level: Access to district "
            "and its associated talukas."
        )

        development_page()


    elif st.session_state.user_type == "Taluka Level":

        st.info(
            "Taluka Level: Access to projects "
            "within the assigned taluka."
        )

        development_page()


    elif st.session_state.user_type == "Inspection Authority":

        st.info(
            "Inspection Authority: Access to "
            "project inspection information."
        )

        inspection_page()


# =========================================================
# INSPECTION PAGE
# =========================================================

def inspection_page():

    st.markdown(
        '<div class="section-title">Project Inspection</div>',
        unsafe_allow_html=True
    )

    project_name = st.selectbox(
        "Select Project",
        projects["Project"].tolist()
    )


    selected_project = projects[
        projects["Project"] == project_name
    ].iloc[0]


    col1, col2 = st.columns(2)


    with col1:

        st.write(
            "**Project ID:**",
            selected_project["Project ID"]
        )

        st.write(
            "**State:**",
            selected_project["State"]
        )

        st.write(
            "**District:**",
            selected_project["District"]
        )

        st.write(
            "**Taluka:**",
            selected_project["Taluka"]
        )


    with col2:

        st.write(
            "**Status:**",
            selected_project["Status"]
        )

        st.write(
            "**Sanctioned Amount:** ₹"
            + format(
                selected_project["Sanctioned Amount"],
                ","
            )
        )

        st.write(
            "**Utilized Amount:** ₹"
            + format(
                selected_project["Utilized Amount"],
                ","
            )
        )


    st.subheader(
        "Inspection Report"
    )


    inspection_status = st.selectbox(
        "Inspection Status",
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


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title(
        "🇮🇳 MPLAD Portal"
    )

    st.divider()


    if not st.session_state.logged_in:

        page = st.radio(
            "Navigation",
            [
                "Home",
                "Development",
                "Funds",
                "Rules & Regulations",
                "Login"
            ]
        )


    else:

        st.success(
            st.session_state.user_type
        )


        page = st.radio(
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


# =========================================================
# PAGE ROUTING
# =========================================================

if page == "Home":

    home_page()


elif page == "Development":

    development_page()


elif page == "Funds":

    funds_page()


elif page == "Rules & Regulations":

    rules_page()


elif page == "Login":

    login_page()


elif page == "Dashboard":

    dashboard_page()


elif page == "Inspection":

    inspection_page()


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

    <b>MPLAD Development Monitoring System</b>

    <br><br>

    Development Monitoring |
    Fund Monitoring |
    Project Inspection

    <br><br>

    Demo Prototype

    </div>
    """,
    unsafe_allow_html=True
)