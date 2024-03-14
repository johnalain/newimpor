#https://youtu.be/UO98lJQ3QGI?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_
from matplotlib import pyplot as plt
ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [34900,35900,35980,45123,60780,62450,63345,64500,65670,78080,79400]
plt.plot(ages_x, dev_y)

# py_dev_x = [25,26,27,28,29,30,31,32,33,34,35]
py_dev_y = [45372,48876,53850,75276,63016,65998,70003,70000,71400,75370,83640]
plt.plot(ages_x, py_dev_y)
#https://youtu.be/UO98lJQ3QGI?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&t=688

plt.xlabel('ages')
plt.ylabel('median salary(USD)')
plt.title('Median salary(USD)by age')
plt.show()