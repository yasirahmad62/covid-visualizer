import covid
import matplotlib.pylot as plt   

cov=covid.Covid()

name = input("ENTER the country name")
virusdata=covid.get_status_by_country
active=virusdata['active']
recover=virusdata['recovered']
deaths=virusdata['deaths']
plt.pie([active,recover,deaths]).labels
plt.title(name)
plt.legend()
plt.show
