# Ближайшие бары

Скрипт выводит информацию по барам Москвы.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
Для работы скрипта необходим файл в формате JSON загруженный с сайта https://data.mos.ru/opendata/7710881420-bary.
И указание координат относительно которых нужно найти ближайший бар.

Запуск на Linux:

```bash

$ python bars.py <path to file> <longitude> <latitude>

Самый большой бар: Спорт бар «Красная машина»
Самый маленький бар БАР. СОКИ
Самый близкий бар: БАР СПОРТКЛУБА

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
