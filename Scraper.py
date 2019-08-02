import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://musicboxtheatre.com/films/calendar"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

calendar = {}

show_times = soup.find_all(class_='showtime-list-item')
for show_time in show_times:
    date_and_time = show_time.find('span').attrs['content'].split('T')
    day = date_and_time[0]
    time = datetime.strptime(date_and_time[1].split('-')[0], '%H:%M:%S')
    if day not in calendar:
        calendar[day] = {}

    title = show_time.find('a').text
    if title not in calendar[day]:
        calendar[day][title] = []

    calendar[day][title].append(datetime.strftime(time, '%I:%M %p'))

for day, show in calendar.items():
    print(day)
    for title, times in show.items():
        print(title)
        print(times)
        print()

