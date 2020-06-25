import unittest
from Acme import Product, BoxingGlove
from Acme_report2 import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    def test_default_product_price(self):
        prod = Product('Test Produc')
        self.assertEqual(prod.price, 10)
    
            
    def test_product_weight(self):
        prod = Product('Test Produc')
        self.assertEqual(prod.weight, 20)
                

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)
    def test_legal_names(self):
        products = generate_products()
        for product in products:
            adjective,noun = product.name.split()
            self.assertIn(adjective,ADJECTIVES)
            self.assertIn(noun,NOUNS)
    
        


     


if __name__ == "__main__":
    unittest.main()
