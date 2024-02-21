import configuration
import requests
import data


# Создаем новый заказ
def create_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставляем полный url
                         json=order_body,  # тело
                         headers=data.headers)  # заголовки


response = create_new_order(data.order_body)

# print(response.json())

# Получаем номер заказа (параметр track) из ответа на запрос создания нового заказа
order_track = response.json().get('track')

params = {
    't': order_track,
}


# Получаем заказ про его треку
def check_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
                        params=params)


response = check_order()

# print(response.json())
