from datetime import datetime


class SimpleReport:
    @classmethod
    def get_oldest_manufacture_date(cls, products):
        oldest_manufacture_date = [
            date["data_de_fabricacao"] for date in products
        ]
        oldest_manufacture_date.sort()
        return oldest_manufacture_date[0]

    @classmethod
    def get_closet_date(cls, products):
        current_date = datetime.now().strftime("%Y-%m-%d")
        closest_date = [
          date['data_de_validade']for date in products
          if current_date < date['data_de_validade']
        ]
        closest_date.sort()
        return closest_date[0]

    @classmethod
    def company_biggest_stock_products(cls, products):
        companies = [company["nome_da_empresa"] for company in products]
        return max(companies)

    @classmethod
    def generate(cls, products):
        # variaveis para não exceder quantidade de caracter em linha no return
        oldest_date = cls.get_oldest_manufacture_date(products)
        closest_date = cls.get_closet_date(products)
        company = cls.company_biggest_stock_products(products)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
