# import converters_modules
# from converters_modules import kg_to_lbs

# # print(converters_modules.kg_to_lbs(70))

# print(kg_to_lbs(100))
# print(converters_modules.kg_to_lbs(70))

# import utils
# utils.find_max()

from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
# print(max(numbers))
# print(maximum)

# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping, calc_tax
# calc_shipping()
# calc_tax()

from ecommerce import shipping
shipping.calc_shipping()
shipping.calc_tax()