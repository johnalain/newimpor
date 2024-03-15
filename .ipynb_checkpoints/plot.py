#https://youtu.be/UO98lJQ3QGI?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_
from matplotlib import pyplot as plt
#print(plt.style.available)#print in terminal available options
plt.style.use('seaborn-v0_8-darkgrid')
ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [34900,35900,35980,45123,60780,62450,63345,64500,65670,78080,79400]
plt.plot(ages_x, dev_y,color='#444444',linestyle=':', label='all devs')#'k--' =black -- dashed line or we can use color='b',linestyle='--',

# py_dev_x = [25,26,27,28,29,30,31,32,33,34,35]
py_dev_y = [45372,48876,53850,75276,63016,65998,70003,70000,71400,75370,83640]
plt.plot(ages_x, py_dev_y,color='#5a7b9a',linewidth=3,label='python')#'b' -> blue line color
js_dev_y =[37810,43615,46623,49293,53437,56373,62375,66674,68745,68746,74583]
plt.plot(ages_x, js_dev_y,color='#adad3b',linewidth=3,label='javascript')
dev_y = [34900,35900,35980,45123,60780,62450,63345,64500,65670,78080,79400]
plt.plot(ages_x, py_dev_y,color='#5a7b9a',linewidth=3,label='python')


#https://youtu.be/UO98lJQ3QGI?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&t=688
#https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog github code for this video

plt.xlabel('ages')
plt.ylabel('median salary(USD)')
plt.title('Median salary(USD)by age')
# plt.legend(['all devs','python'])
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html library link
#https://youtu.be/UO98lJQ3QGI?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&t=1606
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()