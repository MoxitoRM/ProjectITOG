import random
import time

words = [
    "Морковка",
    "Перец",
    "Полотно",
    "Матрас",
    "Красота",
    "Делая",
    "Экран",
    "Дерево",
    "Принцесса",
    "Хорошо",
    "Машина",
    "Автомобиль",
    "Вата",
    "Синергия",
    "Студент",
    "Треугольник",
    "Площадь",
    "Калькулятор",
    "Ромб",
    "Главный",
    "Красный",
    "Защита",
    "Четыре",
    "Стол",
    "Очки",
    "Волосы",
    "Ребра",
    "Нос",
    "Глаз",
    "Ухо",
    "Пузо",
    "Толстовка",
    "Рыжий",
    "Информация",
    "Кнопка",
    "Корабль",
    "Йод",
    "Игрушка",
    "Ребра",
    "Команда",
    "Писатель",
    "Пополам",
    "Членораздельный",
    "Яйцо",
    "Больше",
    "Найти",
    "Говориться",
    "Мучиться",
    "Умирать",
    "Данные",
    "Страдать",
    "Истекать",
    "Кровь",
    "Помогите",
    "Мне",
    "Пожалуйста",
    "Меня",
    "Держать",
    "Около",
    "Заложник",
    "Атака",
    "Страдая",
    "Держась",
    "Чернокожий",
    "Убить",
    "Зерно"
]
def random_word():
    random_w = random.choice(words)
    return random_w

def timer(n):
    for i in range(n):
        time.sleep(1)