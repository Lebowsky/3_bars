import json
import math
import argparse


def load_data(filepath):
    with open(filepath, encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        return json_data


def get_biggest_bar(bars):
    return max(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount'],
    )


def get_smallest_bar(bars):
    return min(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount'],
    )


def get_closest_bar(bars, longitude, latitude):
    return min(
        bars,
        key=lambda bar: get_distance_between_points(bar, longitude, latitude),
    )


def get_distance_between_points(bars, longitude, latitude):
    return math.sqrt(
        (bars['geometry']['coordinates'][0]-longitude)**2 +
        (bars['geometry']['coordinates'][1]-latitude)**2)


def create_argument_parcer():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str)
    parser.add_argument("longitude", type=float)
    parser.add_argument("latitude", type=float)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = create_argument_parcer()

    try:
        json_data = load_data(args.filepath)
        bars = json_data['features']
    except (FileNotFoundError, ValueError) as e:
        print("Не удалось прочитать JSON-файл", e)
    else:
        print("Самый большой бар: {}".format(
            get_biggest_bar(bars)['properties']['Attributes']['Name']))
        print("Самый маленький бар: {}".format(
            get_smallest_bar(bars)['properties']['Attributes']['Name']))
        print("Самый близкий бар: {}".format(
              get_closest_bar(bars, args.longitude, args.latitude)
              ['properties']['Attributes']['Name']))
