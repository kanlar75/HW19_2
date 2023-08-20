from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.truncate()
        Product.truncate()

        categories_list = [
            {'pk': 1, 'name': 'рассылки', 'description': 'отправка одного сообщения большому количеству получателей'},
            {'pk': 2, 'name': 'телеграм боты', 'description': 'мини-программы внутри мессенджера, которые управляются '
                                                              'текстовыми командами в чате по принципу вопрос  ответ'},
            {'pk': 3, 'name': 'полезные утилиты', 'description': 'вспомогательная компьютерная программа в составе '
                                                                 'общего программного обеспечения для выполнения '
                                                                 'специализированных типовых задач'},
            {'pk': 4, 'name': 'веб-приложения', 'description': 'программное обеспечение, которое запускается в '
                                                               'веб-браузере'},
            {'pk': 5, 'name': 'микросервисы', 'description': 'веб-сервис, отвечающий за один элемент логики в '
                                                             'определенной предметной области'},
        ]

        categories_for_create = []
        for category in categories_list:
            categories_for_create.append(
                Category(**category)
            )
        Category.objects.bulk_create(categories_for_create)

        products_for_create = []
        products_list = [
            {"name": "Рассылка 150",
             "description": "Рассылка 150 получателям.",
             "image": "",
             "category": categories_for_create[0],
             "price": 1500},
            {"name": "Телеграм бот курс валют",
             "description": "Бот получает курсы валют и извещает об изменении курса.",
             "image": "",
             "category": categories_for_create[1],
             "price": 5000
             },
            {"name": "Деинсталлятор ПО",
             "description": "Помогает удалить ПО и очистить реестр.",
             "image": "",
             "category": categories_for_create[2],
             "price": 10000
             },
            {"name": "Веб-приложение 'интернет-магазин'",
             "description": "Продажа товаров через интернет-магазин",
             "image": "",
             "category": categories_for_create[3],
             "price": 15500
             },

            {"name": "Микросервис системы оплаты по QR коду.",
             "description": "Обрабатывает транзакции и взаимодействует с платежными системами.",
             "image": "",
             "category": categories_for_create[4],
             "price": 9000
             }
        ]
        for product in products_list:
            products_for_create.append(Product(**product))

        Product.objects.bulk_create(products_for_create)
