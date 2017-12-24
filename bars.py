import json
import math
import argparse


def load_data(filepath):
    with open(filepath, encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        return json_data


def get_biggest_bar(bars):
    return max_min_seats_count(bars, max)


def get_smallest_bar(bars):
    return max_min_seats_count(bars, min)


def get_closest_bar(bars, longitude, latitude):
    bars_coordinates = [[bar['properties']['Attributes']['Name'],
                         bar['geometry']['coordinates']]
                        for bar in bars]

    bars_coordinates_dist = [
        [bar_coorinates[0], bar_coorinates[1],
         get_distance_between_points(bar_coorinates, longitude, latitude)]
        for bar_coorinates in bars_coordinates]

    min_dist = min(bars_coordinates_dist,
                   key=lambda bars_coordinates_list: bars_coordinates_list[2])
    return min_dist[0]


def get_distance_between_points(coorinates, longitude, latitude):
    return math.sqrt(
        (coorinates[1][0]-longitude)**2 + (coorinates[1][1]-latitude)**2)


def max_min_seats_count(bars, func_max_min):
    bars_attributes = [
        bar['properties']['Attributes']
        for bar in bars]

    seats_count = [
        [bar_attributes['Name'], bar_attributes['SeatsCount']]
        for bar_attributes in bars_attributes]

    bar_seats_count =\
        func_max_min(seats_count,
                     key=lambda list_seats_count: list_seats_count[1])
    return bar_seats_count[0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    parser.add_argument("longitude")
    parser.add_argument("latitude")
    args = parser.parse_args()

    try:
        json_data = load_data(args.filepath)
        bars = json_data['features']
    except (FileNotFoundError, ValueError) as e:
        print("Не удалось прочитать JSON-файл", e)
    else:
        print("Самый большой бар: %s" % get_biggest_bar(bars))
        print("Самый маленький бар: %s" % get_smallest_bar(bars))
        print("Самый близкий бар: %s" %
              get_closest_bar(bars, float(args.longitude),
                              float(args.latitude)))
