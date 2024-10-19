from datetime import datetime
import pandas as pd
import re
import pytz

#prompt function
def get_string(prompt, cast_type=str):
    while True:
        try:
            user_input = input(prompt)
            if cast_type == str and not re.match(r'^[A-Za-z\s]+$', user_input):
                raise ValueError("input should not contain numbers or special character!")
            return user_input
        except ValueError as e:
            print(f"invalid input: {e}, enter a valid {cast_type.__name__}")

def get_int(prompt, cast_type=int):
    while True:
        try:
            return cast_type(input(prompt))
        except ValueError:
            print(f"invalid input, enter a valid {cast_type.__name__}")

def get_birthday(prompt, casetype=str):
    while True:
        user_input = input(prompt)
        try:
            birthday = datetime.strptime(user_input, "%Y-%m-%d")
            return birthday.date()
        except ValueError:
            print("incorrect date format! Only use YYYY-MM-DD")

#auto-add csv function
def csv_function(path, new_df):
    try:
        df = pd.read_csv(path, sep=';')
        return pd.concat([df, new_df], ignore_index=True)
    except FileNotFoundError:
        return new_df
    
#defining timestamp
timezone = pytz.timezone('Asia/Jakarta')
timestamp = datetime.now(timezone)

#prompt field
name_input = get_string("Nama: ")
kedudukan_input = get_string("Kedudukan: ")
birthday_input = get_birthday("Tanggal lahir (YYYY-MM-DD): ")
kota_input = get_string("Tempat Lahir: ")
status_input = get_string("Status: ")
pekerjaan_input = get_string("Pekerjaan: ")
domisili_input = get_string("Kota Domisili: ")

#convert the inputted datas into a dictionary
record = {
    'timestamp':timestamp,
    'nama':name_input,
    'kedudukan':kedudukan_input,
    'tanggal_lahir':birthday_input,
    'kota_lahir':kota_input,
    'status':status_input,
    'pekerjaan':pekerjaan_input,
    'kota_domisili':domisili_input
}

record_df = pd.DataFrame([record])

#adding a feature to auto-add to a csv file
csv_path = 'data_keluarga.csv'
df = csv_function(csv_path, record_df)
df.to_csv(csv_path, sep=';', index=False)