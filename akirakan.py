import requests
import logging
from datetime import datetime, timedelta

today = datetime.today()
t = today.strftime("%d%m%y")
ym = today.strftime("%Y-%m")
ymd = today.strftime("%Y-%m-%d")

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d%m%Y %I:%M:%S%p', filename=f"C:/Users/DOUBLE33/PycharmProjects/akirakan/log/log {t}.txt", level=logging.DEBUG)
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

    # if line is empty
    # end of file is reached
    if not location:
        break
    with open(f"{filename}", "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            # writing one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)

    print("Line{}: {}".format(count, location.strip())+file_url)
    logging.debug('Reading line {} '.format(count, location.strip()) + file_url)

locations.close()



