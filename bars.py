import json
import math
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as json_data:
        try:
            json_data = json.load(json_data)
        except ValueError as e:
            print("Не удалось прочитать JSON-файл", e)
            return
        return json_data


def get_biggest_bar(json_data):
    return max_min_seats_count(json_data, max)


def get_smallest_bar(json_data):
    return max_min_seats_count(json_data, min)


def get_closest_bar(json_data, longitude, latitude):
    bars_coordinates = [[feature['properties']['Attributes']['Name'],
                         feature['geometry']['coordinates']]
                        for feature in json_data['features']]
    # Найдем расстояния точек
    bars_coordinates_distances = [
        [bar[0], bar[1],
         math.sqrt((bar[1][0]-longitude)**2 + (bar[1][1]-latitude)**2)]
        for bar in bars_coordinates]
    distances = [bar[2] for bar in bars_coordinates_distances]
    min_dist = min(distances)
    bars_coordinates_min_distances = [bar for bar in bars_coordinates_distances
                                      if bar[2] == min_dist]
    return bars_coordinates_min_distances[0][0]


def max_min_seats_count(json_data, func_max_min):
    bars_attributes = [
        feature['properties']['Attributes']
        for feature in json_data['features']]
    # создадим список всех размеров для поиска максимума/минимума
    seats_count = [
        bar_attributes['SeatsCount']
        for bar_attributes in bars_attributes]
    biggest_bars = [
        bar_attributes['Name']
        for bar_attributes in bars_attributes
        if bar_attributes['SeatsCount'] == func_max_min(seats_count)]
    return biggest_bars[0]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        json_data = load_data(sys.argv[1])
        print("Самый большой бар: " + get_biggest_bar(json_data))
        print("Самый маленький бар " + get_smallest_bar(json_data))
        print("Самый близкий бар: " +
              get_closest_bar(json_data, float(sys.argv[2]),
                              float(sys.argv[3])))
