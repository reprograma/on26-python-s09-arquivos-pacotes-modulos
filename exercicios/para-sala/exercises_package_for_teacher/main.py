from cintia_package import module1
from sum import sum_house
from sum.motorcycle import sum_motorcycle

info = module1.main()
print(info)

my_sum = module1.sum(1,2)
print(f'a + b is equal to: {my_sum}')

sum_house_cintia = sum_house.sum_house(4)
print(f'Cintia has: {sum_house_cintia} houses')

sum_motorcycle_cintia = sum_motorcycle.sum_motorcycle(1)
print(f'Cintia has: {sum_motorcycle_cintia} motorcycles')