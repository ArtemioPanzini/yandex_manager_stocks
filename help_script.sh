#!/bin/bash

# Активировать виртуальную среду Poetry
poetry shell

echo "all good"

# Путь к вашему основному скрипту
path_to_script="/home/scrapping/Beauty_light/main_stock.py"

# Запустить ваш основной скрипт
python "$path_to_script"
