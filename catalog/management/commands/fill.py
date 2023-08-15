from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    pass

    def handle(self, *args, **options):
        products_for_create = []
        products_list = [
            {"name": "Рассылка 150",
             "description": "Рассылка 150 получателям.",
             "image": "",
             "category": 1,
             "price": 1500},
            {"name": "Веб-приложение 'интернет-магазин'",
             "description": "Продажа товаров через интернет-магазин",
             "image": "",
             "category": 4,
             "price": 15500
             },
            {"name": "Микросервис системы оплаты по QR коду.",
             "description": "Обрабатывает транзакции и взаимодействует с платежными системами.",
             "image": "",
             "category": 5,
             "price": 9000
             }
        ]
        for product in products_list:
            products_for_create.append(Product(**product))

        Product.objects.bulk_create(products_for_create)
