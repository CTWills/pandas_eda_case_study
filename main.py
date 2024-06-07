import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns
from src import create_plots as cp
from src import clean


if __name__ == "__main__":
    youtube_data = pd.read_csv("youtube_data/USvideos.csv",
                               parse_dates=["publish_time"])

    youtube_data["trending_date"] = youtube_data["trending_date"].apply(
        lambda date_string: datetime.strptime(date_string, "%y.%d.%m"))

    dct = clean.create_from_json()

    youtube_data["genre"] = youtube_data["category_id"].apply(
        lambda id: dct[str(id)])

    youtube_data["publish_time"] = youtube_data["publish_time"].apply(
        lambda x: x.tz_localize(None))

    youtube_data["publish_time"] = youtube_data["publish_time"].dt.floor("D")

    youtube_data["Time Difference"] = (
        youtube_data["trending_date"] - youtube_data["publish_time"])

    removed_outlier_df = youtube_data[youtube_data["Time Difference"] < timedelta(
        days=25)]

    genre_views = youtube_data.groupby("genre")["views"].sum()
    videos_per_genre = youtube_data.groupby("genre")["video_id"].count()

    videos_per_genre = pd.concat([genre_views, videos_per_genre], axis=1)

    cp.create_box_plot(removed_outlier_df, "without_outliers",
                       "Distribution without outliers")
    cp.create_box_plot(youtube_data, "with_outliers",
                       "Distribution with outliers")
    cp.create_histogram_plot(
        removed_outlier_df, title="Distribution of days till trending", name="histogram")

    cp.create_bar_plot(genre_views, "bar_plot_views", "Views per genre")

    cp.create_bar_plots(videos_per_genre, "bar_plots_compare")
