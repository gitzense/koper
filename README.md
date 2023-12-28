# Автоматизация работы копра при помощи машинного зрения

За начало координат принята низшая точка прохождения копра.

![nulls](https://github.com/gitzense/koper/assets/114235388/9dc17757-961d-414e-923b-061353ae6edf)

Данные, которые необходимо получить: начальная высота, максимальная высота поднятия после удара

![start_height](https://github.com/gitzense/koper/assets/114235388/6db95678-2c1e-4fae-b83e-152e48c2bce2) 

![max_height](https://github.com/gitzense/koper/assets/114235388/24026a61-16a6-4f58-aaf5-c552b0bce04d)

## Обработка изображения

Начальная высота

![processing_image](https://github.com/gitzense/koper/assets/114235388/d5244162-45be-402b-bf5c-79bd39056400)

В терминале выводится высота от начала координат

![terminal_image](https://github.com/gitzense/koper/assets/114235388/eec33bab-dbb2-4100-a7dc-4edba590499d)

Максимальная высота

![processing2_image](https://github.com/gitzense/koper/assets/114235388/a7036d82-3efe-4b96-ab0f-1f026ee6aa30)

![terminal_1_image](https://github.com/gitzense/koper/assets/114235388/2cfa554d-ec3b-4e07-a355-4316f1bbf1be)

## Обработка видео

https://github.com/gitzense/koper/assets/114235388/8c3a5e0a-65a6-4f20-84ed-d2bf66ac30bd

В терминале выводятся наивысшие точки, зафиксированные слева и справа от начала координат

![terminal_1_video](https://github.com/gitzense/koper/assets/114235388/845b9620-54b5-4e80-8105-c4120c4b0dd9)

## Расчет ударной вязкости 

Высота маятника до испытания h1 = 0,76 м;

Высота маятника после испытания h2 = 0,65 м;

Вес маятника G = 1,255 кг;

Сторона карандаша а = 0,4 см.

K = G*(h1 – h2) = 1,255*(0,76 – 0,65) = 0,138 Дж – работа, затраченная на ударный излом образца

F = (3√3 * a2)/2 = 0,416 см2 – площадь поперечного сечения шестиугольного карандаша

KC = K/F = 0,138/0,416 = 0,332 Дж/см2



