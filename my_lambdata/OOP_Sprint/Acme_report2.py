
from random import randint, sample, uniform
from Acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for num_product in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price =  randint(5,100) 
        weight = randint(5,100)
        flammability = uniform(0,2.5)
        product = Product(name =name,price = price,weight= weight,flammability=flammability)
        products.append(product)            
    
    return products


def inventory_report(products):
    sum_price = 0
    sum_weight = 0
    sum_flammability = 0
    names = []
    for product in products:
        sum_price += product.price
        sum_weight += product.weight
        sum_flammability += product.flammability
        names.append(product.name)
    num_products = len(products)
    num_unique_produt_names = len(set(names))
    avg_price = sum_price/num_products
    avg_weight = sum_weight/num_products
    avg_flammability = sum_flammability/num_products
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:",num_unique_produt_names) 
    print("Average price:",avg_price)
    print("Average weight:",avg_weight)
    print("Average flammability:",avg_flammability)

    

if __name__ == '__main__':
    inventory_report(generate_products())

