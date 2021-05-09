from tracker_generator import TrackerGenerator
import streamlit as st
import os
import base64
import time
import pandas as pd

st.title("Automatic trcaker Generation :sunglasses:")


def main():

    obj1 = TrackerGenerator()

    def csv_exporter(data, flag):
        csvfile = data.to_csv(index=False)
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "{}_tracker.csv".format(flag)
        st.markdown("### Downloaf File ###")
        href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)

    def generate_weekly_trackers():
        st.header("Single Intern Tracker")
        col1, col2 = st.beta_columns(2)
        user_input = col1.text_input("Enter Name")
        try:
            uploaded_file = col2.file_uploader("Upload the Daily Trcakers as serially as Names", type=[
                                               'csv', 'xlsx', 'xlsm'], accept_multiple_files=False)
            uploaded_data_read = pd.read_excel(
                uploaded_file, engine='openpyxl')
            week_tracker = pd.DataFrame(
                obj1.weekly_tracker_generator(uploaded_data_read, [user_input]))
            month_tracker = pd.DataFrame(
                obj1.monthly_tracker_generator(uploaded_data_read, [user_input]))

        except Exception as e:
            st.warning("Please provide the CSV")

        if col1.button('Generate Weekly Tracker', key=3):
            try:
                st.dataframe(week_tracker)
                csv_exporter(week_tracker, 'week')
            except Exception as e:
                st.warning(e)
        if col1.button('Generate Monthly Tracker', key=4):
            try:
                st.dataframe(month_tracker)
                csv_exporter(month_tracker, 'month')
            except Exception as e:
                st.warning(e)

    def generate_weekly_trackers_multiuser():
        st.header("Group Tracker Of Interns")
        user_input = st.text_input("Enter Names separated by a comma")
        uploaded_files = st.file_uploader("Upload the Daily Trcakers as serially as Names", type=[
                                          'csv', 'xlsx', 'xlsm'], accept_multiple_files=True)

        if uploaded_files:
            for file in uploaded_files:
                file.seek(0)

            weekly_trackers = list()
            monthly_trackers = list()
            for file, usenames in zip(uploaded_files, user_input.split(',')):
                uploaded_data_read = pd.read_excel(file, engine='openpyxl')
                weekly_tracker = pd.DataFrame(
                    obj1.weekly_tracker_generator(uploaded_data_read, [usenames]))
                monthly_tracker = pd.DataFrame(
                    obj1.monthly_tracker_generator(uploaded_data_read, [usenames]))
                weekly_trackers.append(weekly_tracker)
                monthly_trackers.append(monthly_tracker)

            final_week_trcaker = pd.concat(data for data in weekly_trackers)
            final_month_trcaker = pd.concat(data for data in monthly_trackers)

            if st.button('Generate Weekly Tracker', key=1):
                st.dataframe(final_week_trcaker)
                csv_exporter(final_week_trcaker, 'week')

            if st.button('Generate Monthly Tracker', key=2):
                st.dataframe(final_month_trcaker)
                csv_exporter(final_month_trcaker, 'month')

    generate_weekly_trackers()
    generate_weekly_trackers_multiuser()


if __name__ == '__main__':
    main()
