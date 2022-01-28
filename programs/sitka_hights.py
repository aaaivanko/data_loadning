import csv
import matplotlib.pyplot as plt

from datetime import datetime


filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            low = int(row[5])
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[4])
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
        except ValueError:
            print(f"Missing data for {current_date}")


# create graphic with big temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format graphic
plt.title('Daily high and low temperatures  walley', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

