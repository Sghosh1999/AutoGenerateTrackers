import pandas as pd
import numpy as np
from datetime import timedelta, date
import string
import os,re


class TrackerGenerator:
    def __init__(self):
        pass

    # Monthly Tracker Generator
    def monthly_tracker_generator(self, daily_tracker, user_name):
        # Converting the timestamp with proper date formatting
        daily_tracker['Start Date'] = pd.to_datetime(
            daily_tracker['Start Date'])

        # Creating a task dictionary based on daily goals
        task_list = dict(
            zip(daily_tracker['Start Date'], daily_tracker['Task']))

        # maintaing a dictionary for the weekly tasks
        monthly_task = dict()

        # Selecting 3 days earlier than the maximum date for handling NuLL
        start_date = daily_tracker['Start Date'].min()
        end_date = daily_tracker['Start Date'].max()

        # Flag for tracking Month index
        a = 1

        while(start_date < end_date):
            month_task_list = []
            field_val = ""
            line = 1

            # Creating a string for excluding the Holidays from Tracker
            holiday_ind = 'Holiday'

            # Month Start and End Day
            month_start = start_date
            month_end = start_date+timedelta(30)

            day_count = (month_end - month_start).days

            # print(day_count)
            for i in (start_date + timedelta(n) for n in range(day_count)):
                try:
                    task_name = (
                        daily_tracker[daily_tracker['Start Date'] == i].Task.values[0]).replace("\n", "")
                    
                    pattern = r'\d.'
                    for ij in re.findall(pattern,task_name):
                        task_name = task_name.replace(ij,'')
                    month_task_list.append(task_name)
                except:
                    pass

            while(holiday_ind in month_task_list):
                month_task_list.remove(holiday_ind)
            while('Leave' in month_task_list):
                month_task_list.remove('Leave')

            monthly_task['Month'+str(a)] = month_task_list

            for vals in monthly_task['Month'+str(a)]:
                field_val = field_val + str(line) + '. ' + str(vals) + '\n'
                line = line+1

            # print(field_val)
            monthly_task['Month'+str(a)] = field_val
            a = a+1
            start_date = month_end

        # Creating a Dataframe for maintaing the Names
        df = pd.DataFrame(monthly_task, index=[user_name])
        df.insert(0, "Name", [user_name], True)
        return df.to_dict()

    def weekly_tracker_generator(self, daily_tracker, user_name):
        # Converting the timestamp with proper date formatting
        daily_tracker['Start Date'] = pd.to_datetime(
            daily_tracker['Start Date'])

        # Creating a task dictionary based on daily goals
        task_list = dict(
            zip(daily_tracker['Start Date'], daily_tracker['Task']))

        # maintaing a dictionary for the weekly tasks
        weekly_task = dict()

        start_date = daily_tracker['Start Date'].min()
        end_date = daily_tracker['Start Date'].max()
        # -timedelta(3)

        a = 1

        while(start_date < end_date):
            week_task_list = []
            field_val = ""
            line = 1
            holiday_ind = 'Holiday'

            week_start = start_date
            week_end = start_date+timedelta(7)
            day_count = (week_end - week_start).days
            for i in (start_date + timedelta(n) for n in range(day_count)):
                try:
                    task_name = (
                        daily_tracker[daily_tracker['Start Date'] == i].Task.values[0]).replace("\n", "")
                    pattern = r'\d.'
                    for ij in re.findall(pattern,task_name):
                        task_name = task_name.replace(ij,'')

                    week_task_list.append(task_name)

                except:
                    pass

            while(holiday_ind in week_task_list):
                week_task_list.remove(holiday_ind)
            while('Leave' in week_task_list):
                week_task_list.remove('Leave')

            weekly_task['Week'+str(a)] = week_task_list

            for vals in weekly_task['Week'+str(a)]:
                field_val = field_val + str(line) + '.' + str(vals) + '\n'
                line = line+1

            #print(field_val)
            weekly_task['Week'+str(a)] = field_val
            a = a+1
            start_date = week_end

        # Creating a Dataframe for maintaing the Names
        df = pd.DataFrame(weekly_task, index=[user_name])
        df.insert(0, "Name", [user_name], True)
        return df.to_dict()

    def generator_file(self, df, flag):

        # Writing the final monthly tracker in Excel file
        cols_for_wrap = list(df.columns)
        writer = pd.ExcelWriter(flag+'ly_trcaker.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)

        # modifyng output by style - wrap
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        wrap_format = workbook.add_format({'text_wrap': True,'bold': True})

        # dictionary for map position of selected columns to excel headers
        d = dict(zip(range(26), list(string.ascii_uppercase)))

        {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
         9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
         17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

        # get positions of columns
        #print(cols_for_wrap)
        #print(df.columns.get_indexer(cols_for_wrap))
        for col in df.columns.get_indexer(cols_for_wrap):
            # map by dict to format like "A:A"
            excel_header = d[col] + ':' + d[col]
            # None means not set with
            #worksheet.set_column(excel_header, None, wrap_format)
            # for with = 20
            #worksheet.set_row(excel_header, 150, wrap_format)
            worksheet.set_column(excel_header, 550, wrap_format)
        # writer.Columns.AutoFit()
        
        writer.save()
