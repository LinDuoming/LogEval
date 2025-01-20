import sys
import os
os.chdir(os.path.dirname(__file__))
import datetime

import pandas as pd
import json


def get_news():
    with open("news.json") as f:
        n = json.load(f)
        for i in range(len(n)):
            n[i]["time"] = datetime.datetime(**(n[i]["time"]))
    return n


def get_statistics():
    return {
        "updatetime": datetime.datetime(year=2024, month=7, day=24, hour=17, minute=24),
        "leaderboard": pd.read_csv("leaderboard.csv")
    }
