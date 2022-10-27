import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd
import numpy as np

# create the root window
root = tk.Tk()
root.title('EWARS-Rain')
root.resizable(False, False)
root.geometry('300x150')


global filename_1
filename_1 = 0

def close():
   #win.destroy()
   root.quit()

def select_file_1():
    filetypes = (
        ('CSV', '*.csv'),
        ('All files', '*.*'),
        
    )
    global filename_1
    filename_1 = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

def process_data():
    if filename_1 == 0:
        showinfo(
        title='มีข้อผิดพลาดเกิดขึ้น',
        message='กรุณาเลือกไฟล์ก่อน'
        )
    else:
        try:
            if filename_1[-4:] == ".csv":
                df_1 = pd.read_csv(filename_1)
                remainder = df_1.shape[0] % 7
                max_value_result = []

                for i in range(df_1.shape[0] - remainder):
                    if i%7 == 0:
                        temp = []
                        temp.append(df_1.iloc[i]['rain'])
                    elif (i+1) % 7 == 0:
                        temp.append(df_1.iloc[i]['rain'])
                        max_value = max(temp)
                        max_value_result.append(max_value)
                    else:
                        temp.append(df_1.iloc[i]['rain'])
                        

                if remainder != 0:
                    temp = []
                    for i in range(df_1.shape[0] - remainder, df_1.shape[0]):
                        temp.append(df_1.iloc[i]['rain'])
                    max_value = max(temp)
                    max_value_result.append(max_value)

                
                dict_result = {'max_rain_7day': max_value_result}
                df_result = pd.DataFrame(dict_result) 
                df_result.to_csv('rain_max_7day_result.csv') 
                showinfo(
                title='ดำเนินการสำเร็จ',
                message='ไฟล์ผลลัพธ์จะถูกจัดเก็บในโฟลเดอร์เดียวกันกับโปรแกรมในชื่อ rain_max_7day_result.csv'
                )
            else:
                showinfo(
                title='มีข้อผิดพลาดเกิดขึ้น',
                message='กรุณาเลือกไฟล์ .csv'
                )
        except:
            showinfo(
            title='มีข้อผิดพลาดเกิดขึ้น',
            message='กรุณาเลือกไฟล์ใหม่ และกดปุ่ม process อีกครั้ง'
            )
        

# open button 1
open_button_1 = ttk.Button(
    root,
    text='Open a File 1',
    command=select_file_1
)

# process button
process_button = ttk.Button(
    root,
    text='process',
    command=process_data
)

# exit button
exit_button = ttk.Button(
    root,
    text='exit',
    command=close
)

open_button_1.pack(expand=True)
process_button.pack(expand=True)
exit_button.pack(expand=True)

# run the application
root.mainloop()
