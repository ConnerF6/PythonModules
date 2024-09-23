from datetime import datetime
import random
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random
from decimal import Decimal
from library import always_three

print(always_three())

two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
print(numbers_b)
plt.plot(numbers_a, numbers_b)
plt.show()

current_time = datetime.now()
print(current_time)

random_list = []
for i in range(101):
  random_list.append(random.randint(1, 101))
print(random_list)

randomer_number = random.choice(random_list)
print(randomer_number)
