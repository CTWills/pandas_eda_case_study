import pandas as pd


def find_genre(id, dct):
    return dct[id]


def create_from_json():
    json_data = pd.read_json("youtube_data/US_category_id.json")
    dct = {}
    json_data["items"].apply(lambda obj: dct.update(
        {obj["id"]: obj["snippet"]["title"]}))
    return dct
