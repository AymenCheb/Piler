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
    def __init__(self, save_file: str = "entries.csv"):
        self.save_file = save_file

    def add_entry(self, entry: Entry):
        with open(self.save_file, "a", newline='') as outuput_file:
            csv_writer = csv.writer(outuput_file)
            csv_writer.writerow(entry.to_json())

    def get_achievements(self, time_group: str = "week", date: datetime.date = None):
        achievements = pd.read_csv(self.save_file, parse_dates=["date"])
        if not date:
            date = datetime.today()
        year, week, week_day = date.isocalendar()
        current_year_achievements = achievements[achievements["year"] == year]
        match time_group:
            case "year":
                return current_year_achievements
            case "week":
                return current_year_achievements[achievements["week"] == week]
            case "week_day":
                current_week_achievements = current_year_achievements[achievements["week"] == week]
                return current_week_achievements[achievements["week_day"] == week_day]


def main():
    manager = AchievementManager()
    achievement = input("Hello, what achievement do you want to record?\n")
    while True:
        if achievement == "q":
            break
        entry = Entry(datetime.today().date(), achievement)
        manager.add_entry(entry)
        achievement = input("Anything else? Enter q to quit!\n")
    print(manager.get_achievements(""))


if __name__ == '__main__':
    main()

