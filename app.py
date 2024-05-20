import requests
import pandas as pd
from datetime import datetime

# Define the base URL for the Ergast API
base_url = "https://ergast.com/api/f1/2024.json"

# Fetch the data
response = requests.get(base_url)
data = response.json()

# Parse the race data
races = data['MRData']['RaceTable']['Races']

# Prepare lists to store race details
normal_race_details = []
sprint_race_details = []

# Convert time to UK format
def convert_to_uk_time(time_str):
    if time_str:
        return datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ").strftime("%H:%M")
    return ""

def convert_to_uk_date(time_str):
    if time_str:
        return datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
    return ""

# Iterate over each race to extract required details
for race in races:
    race_name = race['raceName']
    country = race['Circuit']['Location']['country']
    race_date = convert_to_uk_date(race['date'] + 'T' + race['time']) if 'time' in race else ""
    race_time = convert_to_uk_time(race['date'] + 'T' + race['time']) if 'time' in race else ""
    
    if 'Sprint' not in race:
        fp1_date = convert_to_uk_date(race['FirstPractice']['date'] + 'T' + race['FirstPractice']['time']) if 'FirstPractice' in race else ""
        fp1_time = convert_to_uk_time(race['FirstPractice']['date'] + 'T' + race['FirstPractice']['time']) if 'FirstPractice' in race else ""
        fp2_time = convert_to_uk_time(race['SecondPractice']['date'] + 'T' + race['SecondPractice']['time']) if 'SecondPractice' in race else ""
        fp3_date = convert_to_uk_date(race['ThirdPractice']['date'] + 'T' + race['ThirdPractice']['time']) if 'ThirdPractice' in race else ""
        fp3_time = convert_to_uk_time(race['ThirdPractice']['date'] + 'T' + race['ThirdPractice']['time']) if 'ThirdPractice' in race else ""
        quali_time = convert_to_uk_time(race['Qualifying']['date'] + 'T' + race['Qualifying']['time']) if 'Qualifying' in race else ""
        fp2_date = fp1_date if fp1_date == fp3_date else fp3_date
        
        normal_race_details.append([race_name, country, fp1_date, fp1_time, fp2_time, fp3_date, fp3_time, quali_time, race_date, race_time])
    else:
        fp1_date = convert_to_uk_date(race['FirstPractice']['date'] + 'T' + race['FirstPractice']['time']) if 'FirstPractice' in race else ""
        fp1_time = convert_to_uk_time(race['FirstPractice']['date'] + 'T' + race['FirstPractice']['time']) if 'FirstPractice' in race else ""
        sprint_quali_date = convert_to_uk_date(race['SprintQualifying']['date'] + 'T' + race['SprintQualifying']['time']) if 'SprintQualifying' in race else ""
        sprint_quali_time = convert_to_uk_time(race['SprintQualifying']['date'] + 'T' + race['SprintQualifying']['time']) if 'SprintQualifying' in race else ""
        sprint_date = convert_to_uk_date(race['Sprint']['date'] + 'T' + race['Sprint']['time']) if 'Sprint' in race else ""
        sprint_time = convert_to_uk_time(race['Sprint']['date'] + 'T' + race['Sprint']['time']) if 'Sprint' in race else ""
        quali_time = convert_to_uk_time(race['Qualifying']['date'] + 'T' + race['Qualifying']['time']) if 'Qualifying' in race else ""
        
        sprint_race_details.append([race_name, country, fp1_date, fp1_time, sprint_quali_date, sprint_quali_time, sprint_date, sprint_time, quali_time, race_date, race_time])

# Create DataFrames
normal_df = pd.DataFrame(normal_race_details, columns=[
    "Race Name", "Country", "FP1 and FP2 Date", "FP1 Time", "FP2 Time", "FP3 and Quali Date", "FP3 Time", "Quali Time", "Race Date", "Race Time"])

sprint_df = pd.DataFrame(sprint_race_details, columns=[
    "Race Name", "Country", "FP1 & Sprint Quali Date", "FP1 Time", "Sprint Quali Date", "Sprint Quali Time", "Sprint & Quali Date", "Sprint Time", "Quali Time", "Race Date", "Race Time"])

# Save to CSV
normal_df.to_csv('f1_2024_normal_race_schedule.csv', index=False)
sprint_df.to_csv('f1_2024_sprint_race_schedule.csv', index=False)

print("CSV files 'f1_2024_normal_race_schedule.csv' and 'f1_2024_sprint_race_schedule.csv' have been created.")
