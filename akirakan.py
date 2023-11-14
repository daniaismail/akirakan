import os

import requests
from datetime import datetime, timedelta

today = datetime.today() - timedelta(days=1)
ym = today.strftime("%Y-%m")
ymd = today.strftime("%Y-%m-%d")
download_dir = "C:/Users/mvmwe/PycharmProjects/akirakan/files"
locations = open('locations.txt', 'r')
count = 0

while True:
    count += 1

    # Get next line from file
    line = locations.readline()
    location = line.rstrip('\n')
    file_url = f"https://petronas:viewreport@weather.akirakan.com/archive/forecast_report/{ym}/{location}-{ymd}_issue_at_05:00_LT.pdf"
    filename = f"{location}-{ymd}_issue_at_05_00_LT.pdf"
    r = requests.get(file_url, stream=True)
    file_path = os.path.join(download_dir,filename)

    if not location:
        break
    with open(f"{file_path}", "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            # writing one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)

    print(filename)

locations.close()



