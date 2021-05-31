from tracker_generator import TrackerGenerator
import streamlit as st
import os
import base64
import time
import pandas as pd




def main():

    obj1 = TrackerGenerator()

    def csv_exporter(data, flag):
        csvfile = data.to_csv(index=False)
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "{}_tracker.csv".format(flag)
        st.markdown("### Downloaf File ###")
        href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)

    def generate_weekly_trackers_multiuser():
        st.header("Group Tracker Of Interns")
        number = st.number_input("Enetr no of users", 1)
        weekly_trackers = list()
        monthly_trackers = list()

        for i in range(number):
            col1, col2 = st.beta_columns(2)
            user_input = col1.text_input("Enter Name", key=i)
            try:
                uploaded_file = col2.file_uploader("Upload the Daily Trcakers as serially as Names", key=i, type=[
                    'csv', 'xlsx', 'xlsm'], accept_multiple_files=False)
                uploaded_data_read = pd.read_excel(
                    uploaded_file, engine='openpyxl')
                week_tracker = pd.DataFrame(
                    obj1.weekly_tracker_generator(uploaded_data_read, user_input))
                month_tracker = pd.DataFrame(
                    obj1.monthly_tracker_generator(uploaded_data_read, user_input))

                weekly_trackers.append(week_tracker)
                monthly_trackers.append(month_tracker)
            except Exception as e:
                st.warning("Please provide the CSV")

        if st.button('Generate Weekly Tracker', key=1):
            final_week_trcaker = pd.concat(data for data in weekly_trackers)
            st.dataframe(final_week_trcaker)
            csv_exporter(final_week_trcaker, 'week')

        if st.button('Generate Monthly Tracker', key=2):
            final_month_trcaker = pd.concat(data for data in monthly_trackers)
            st.dataframe(final_month_trcaker)
            csv_exporter(final_month_trcaker, 'month')

    generate_weekly_trackers_multiuser()


if __name__ == '__main__':
    main()
