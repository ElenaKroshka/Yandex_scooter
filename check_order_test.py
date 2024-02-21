# Елена Крошка, 13-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


# Функция для проверки кода ответа
def code_assert():

    # В переменную check_order_response сохраняется результат ответа на проверку заказа по треку
    check_order_response = sender_stand_request.check_order()

    # Проверяется, что код ответа равен 200
    assert check_order_response.status_code == 200


# Тест 1. Проверяем, что по треку заказа можно получить данные о заказе.
def test_check_order_by_track():
    code_assert()

