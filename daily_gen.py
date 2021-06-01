from tracker_generator import TrackerGenerator
import streamlit as st
import os
import base64
import time
import pandas as pd
import datetime
import sqlite3
import smtplib


st.title("Automatic trcaker Generation :sunglasses:")


def main():

    obj1 = TrackerGenerator()
    database_path = "users.db"

    def send_mail(email, massage="you have not submitted in last 2 days"):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("daily.tracker.plus@gmail.com", "Abcd@1234")
        server.sendmail("codegeeks.kalna@gmail.com", email, massage)
        server.quit()

    def check_and_send():
        curr_date = pd.to_datetime(datetime.date.today())
            
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor() 
        
        cursor.execute("SELECT * FROM USERS")
        users_fetched = cursor.fetchall()
        

        for email_i,date_i,day_i in users_fetched:

            last_update_date = pd.to_datetime(date_i)
            day_gap_user = (curr_date - last_update_date).days
            st.write(last_update_date, email_i, day_gap_user)
            if day_gap_user >= day_i:
                send_mail(email_i)
                st.write("mail sent to ", email_i)

        cursor2 = conn.cursor()

        tuple1 = ['checker@checcker', datetime.date.today(), 1]
        insert_query = """REPLACE INTO USERS (EMAIL,UPDATE_DATE,DAY_GAP) VALUES (? , ? , ?)"""
        cursor2.execute(insert_query, tuple1)
        conn.commit()

        conn.close()

    def create_user(email, last_date, days=1):

        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        tuple1 = [email, last_date, days]
        insert_query = """REPLACE INTO USERS (EMAIL,UPDATE_DATE,DAY_GAP) VALUES (? , ? , ?)"""
        cursor.execute(insert_query, tuple1)
        conn.commit()

        conn.close()

    def csv_exporter(data, flag):
        csvfile = data.to_csv(index=False)
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "{}_tracker.csv".format(flag)
        st.markdown("### Downloaf File ###")
        href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)

    def generate_weekly_trackers_multiuser():
        data = pd.DataFrame(columns=['Name', 'Date', 'Task'])

        st.header("Daily Task Uploader")
        name_user = st.text_input("Your Name")
        email = st.text_input("Enter Email")

        if not name_user:
            st.warning("please enter your name")
        else:
            st.text(name_user)

        col1, col2 = st.beta_columns(2)

        today = datetime.date.today()
        start_date = col1.date_input("Start Date", today)
        end_date = col2.date_input("end Date", today)
        
        st.markdown("""---""")  #---------------------------------

        number = end_date - start_date
        number = number.days + 1

        dates = list()
        tasks = list()

        for i in range(number):
            col1, col2 = st.beta_columns(2)

            date_task  =  col1.date_input("Date", (start_date + datetime.timedelta(i)))
            task       =  col2.text_input("tasks", key=i)

            dates.append(start_date + datetime.timedelta(i))
            tasks.append(task)

            if not tasks:
                st.warning("please enter a task")

        c1, c2, c3, c4, c5, c6, c7 = st.beta_columns(7)  # just to make the button stick to right

        data = dict(zip(dates, tasks))
        # st.write(data)

        dataset = pd.DataFrame(data.items(), columns=['Start Date', 'Tasks'])
        st.dataframe(dataset)

        if c7.button("Submit"):
            csv_exporter(dataset, name_user)

            create_user(email, dates[-1])   #dates[-1] contains the last element of the list of the dates. i.e, the last date or the end date.

            curr_date = pd.to_datetime(datetime.date.today())
            
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor() 
            
            cursor.execute("SELECT UPDATE_DATE FROM USERS WHERE EMAIL = 'checker@checcker'")
            fetched = cursor.fetchall()
            # st.write(fetched)
            updated_date = pd.to_datetime(fetched[0][0])

            if curr_date == updated_date:
                st.write("Updated today already")
            else:
                check_and_send()

    generate_weekly_trackers_multiuser()


if __name__ == '__main__':
    main()