import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns
import numpy as np


def create_box_plot(data, name, title):
    fig = sns.boxplot(data["Time Difference"].dt.days) \
        .set_title(title)
    plt.ylabel("Days till trending")
    fig.get_figure().savefig(f"images/{name}.png")


def create_histogram_plot(data, name, title):
    fig, ax = plt.subplots()
    fig = data["Time Difference"].dt.days.plot.hist(
        bins=20, xlabel="days", title=title)
    fig.get_figure().savefig(f"images/{name}.png")


def create_bar_plot(data, name, title):
    fig, ax = plt.subplots()
    data.plot(kind="bar", ylabel="Views (10s billions)",
              title=title)
    plt.tight_layout()
    fig.get_figure().savefig(f"images/{name}.png")


def create_bar_plots(data, name):
    data.plot.bar(subplots=True, layout=(
        1, 2), title="Views per Amount of Videos")
    plt.tight_layout()
    plt.savefig(f"images/{name}.png")


def create_heatmap(data, name):
    fig, ax = plt.subplots(figsize=(10, 6))
    numeric_columns = data.select_dtypes(include=np.number).columns
    correlation_matrix = data[numeric_columns].corr()
    sns.heatmap(data=correlation_matrix, ax=ax)
    plt.title("Correlation of youtube data")
    plt.tight_layout()
    plt.savefig(f"images/{name}.png")
