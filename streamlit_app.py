import streamlit as st
import pandas as pd
import plotly.express as px

from backend.scheduler import Scheduler
from backend.analytics import Analytics
from backend.gantt import create_gantt
from backend.report_generator import ReportGenerator
from backend.notification import NotificationEngine
from backend.audit_log import AuditLog

st.set_page_config(
    page_title="Industry-Level Task Scheduler",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Industry-Level Task Scheduler System")

# ==================================
# SESSION STATE
# ==================================

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ==================================
# SIDEBAR
# ==================================

st.sidebar.header("➕ Add New Task")

task_id = st.sidebar.text_input(
    "Task ID"
)

task_name = st.sidebar.text_input(
    "Task Name"
)

duration = st.sidebar.number_input(
    "Duration (Hours)",
    min_value=1,
    value=1
)

deadline = st.sidebar.number_input(
    "Deadline",
    min_value=1,
    value=10
)

priority = st.sidebar.slider(
    "Priority",
    1,
    10,
    5
)

profit = st.sidebar.number_input(
    "Profit",
    min_value=0,
    value=100
)

skill_required = st.sidebar.selectbox(
    "Required Skill",
    [
        "general",
        "python",
        "frontend",
        "backend",
        "database",
        "testing"
    ]
)

assigned_resource = st.sidebar.text_input(
    "Assigned Resource (Optional)"
)

if st.sidebar.button("Add Task"):

    if task_id and task_name:

        st.session_state.tasks.append({

            "task_id": task_id,

            "task_name": task_name,

            "duration": int(duration),

            "deadline": int(deadline),

            "priority": int(priority),

            "profit": int(profit),

            "skill_required": skill_required,

            "assigned_resource":
                assigned_resource

        })

        st.sidebar.success(
            "Task Added Successfully"
        )

# ==================================
# TABS
# ==================================

tab1, tab2, tab3 = st.tabs(
    [
        "📋 Tasks",
        "⚙ Scheduler",
        "📊 Analytics"
    ]
)

# ==================================
# TASK TAB
# ==================================

with tab1:

    st.subheader("Task List")

    if len(st.session_state.tasks) > 0:

        df = pd.DataFrame(
            st.session_state.tasks
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No tasks added yet."
        )

# ==================================
# SCHEDULER TAB
# ==================================

with tab3:

    st.subheader(
        "Generate Optimized Schedule"
    )

    if st.button(
        "🚀 Generate Schedule"
    ):

        resources = [

            {
                "resource_name":
                    "Python Developer",

                "skill":
                    "python",

                "capacity":
                    8
            },

            {
                "resource_name":
                    "Frontend Developer",

                "skill":
                    "frontend",

                "capacity":
                    8
            },

            {
                "resource_name":
                    "Backend Developer",

                "skill":
                    "backend",

                "capacity":
                    8
            },

            {
                "resource_name":
                    "Database Engineer",

                "skill":
                    "database",

                "capacity":
                    8
            },

            {
                "resource_name":
                    "QA Engineer",

                "skill":
                    "testing",

                "capacity":
                    8
            },

            {
                "resource_name":
                    "General Resource",

                "skill":
                    "general",

                "capacity":
                    8
            }

        ]

        scheduler = Scheduler(
            st.session_state.tasks,
            resources
        )

        completed, missed, total_profit = (
            scheduler.optimize()
        )

        analytics = Analytics()

        kpis = analytics.compute_kpis(
            completed,
            missed
        )

        usage = (
            analytics.resource_utilization(
                completed
            )
        )

        reporter = ReportGenerator()

        csv_path = reporter.export_csv(
            completed,
            missed
        )

        excel_path = (
            reporter.export_excel(
                completed,
                missed
            )
        )

        txt_path = (
            reporter.export_txt(
                kpis
            )
        )

        alert = (
            NotificationEngine()
            .notify(
                missed
            )
        )

        AuditLog().log(
            "Schedule Generated"
        )

        st.success(
            "Schedule Generated Successfully"
        )

        st.info(alert)

        # KPIs

        st.subheader(
            "KPI Dashboard"
        )

        c1, c2, c3, c4 = (
            st.columns(4)
        )

        c1.metric(
            "Total Tasks",
            kpis["total_tasks"]
        )

        c2.metric(
            "Completed",
            kpis["completed"]
        )

        c3.metric(
            "Missed",
            kpis["missed"]
        )

        c4.metric(
            "Success %",
            kpis["success_rate"]
        )

        # Resource Usage

        st.subheader(
            "Resource Utilization"
        )

        st.bar_chart(
            usage
        )

        # Gantt Chart

        st.subheader(
            "Gantt Chart"
        )

        try:

            fig = create_gantt(
                completed
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        except Exception:

            st.warning(
                "Gantt chart unavailable."
            )

        # Completed Tasks

        st.subheader(
            "Completed Tasks"
        )

        st.dataframe(
            pd.DataFrame(
                completed
            )
        )

        # Missed Tasks

        st.subheader(
            "Missed Tasks"
        )

        st.dataframe(
            pd.DataFrame(
                missed
            )
        )

        # Downloads

        st.subheader(
            "Export Reports"
        )

        with open(
            csv_path,
            "rb"
        ) as f:

            st.download_button(
                "Download CSV",
                f,
                "report.csv"
            )

        with open(
            excel_path,
            "rb"
        ) as f:

            st.download_button(
                "Download Excel",
                f,
                "report.xlsx"
            )

        with open(
            txt_path,
            "rb"
        ) as f:

            st.download_button(
                "Download TXT",
                f,
                "report.txt"
            )

# ==================================
# ANALYTICS TAB
# ==================================

with tab2:

    st.subheader(
        "Analytics Dashboard"
    )

    if len(st.session_state.tasks) > 0:

        df = pd.DataFrame(
            st.session_state.tasks
        )

        col1, col2, col3 = (
            st.columns(3)
        )

        col1.metric(
            "Tasks",
            len(df)
        )

        col2.metric(
            "Average Priority",
            round(
                df["priority"].mean(),
                2
            )
        )

        col3.metric(
            "Expected Profit",
            int(
                df["profit"].sum()
            )
        )

        fig = px.bar(

            df,

            x="task_name",

            y="profit",

            color="priority",

            title="Profit Analysis"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "Add tasks to see analytics."
        )