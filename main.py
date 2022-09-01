import csv
import pandas as pd
import os
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Entry:
    full_date: datetime.date
    achievement: str

    def to_json(self):
        year, week, week_day = self.full_date.isocalendar()
        return [self.full_date, year, week, week_day, self.achievement]


class AchievementManager:
    save_file = "entries.csv"

    def add_entry(self, entry: Entry):
        with open(self.save_file, "a", newline='') as outuput_file:
            csv_writer = csv.writer(outuput_file)
            csv_writer.writerow(entry.to_json())

    def get_achievements(self, time_group: str = "week"):
        achievements = pd.read_csv(self.save_file, parse_dates=["date"])
        year, week, week_day = datetime.today().isocalendar()
        time_groups = {"year": year, "week": week, "week_day": week_day}
        return achievements[achievements[time_group] == time_groups[time_group]]


def main():
    manager = AchievementManager()
    achievement = input("Hello, what achievement do you want to record?\n")
    while True:
        if achievement == "q":
            break
        entry = Entry(datetime.today().date(), achievement)
        manager.add_entry(entry)
        achievement = input("Anything else? Enter q to quit!\n")
    print(manager.get_achievements("week"))


if __name__ == '__main__':
    main()

