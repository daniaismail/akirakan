import glob
import os
import glob
import requests
from datetime import datetime

today = datetime.today()
ym = today.strftime("%Y-%m")
ymd = today.strftime("%Y-%m-%d")
download_dir = "C:/Users/vtso_/Dropbox/MVMCC/VTSO ELCC/SKA WEATHER"
locations = open('C:/Users/vtso_/Dropbox/MVMCC/VTSO ELCC/SKA WEATHER/locations.txt', 'r')
pdfFiles = glob.glob(os.path.join(download_dir, "*.pdf"))
count = 0

# Remove existing pdf files
for pdfFile in pdfFiles:
    try:
        os.remove(pdfFile)
    except Exception as e:
        print(f"Error deleting {pdfFile}: {e}")

while True:
    line = locations.readline()
    if not line:
        break

    # Get next line from file
    location = line.rstrip('\n')
    if not location:
        continue

    file_url = f"https://petronas:viewreport@weather.amtmetocean.com/archive/forecast_report/{ym}/{location}-{ymd}_issue_at_05:00_LT.pdf"
    filename = f"{location}-{ymd}_issue_at_05_00_LT.pdf"
    file_path = os.path.join(download_dir, filename)
    r = requests.get(file_url, stream=True)

    # Skip file not found
    if r.status_code == 404:
        print(f"{filename} Not Found")
        continue

    with open(f"{file_path}", "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            # writing one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)
    count += 1
    print(filename)

locations.close()



