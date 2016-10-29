import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_table('cleanedData.txt')
data['length'] = data.text.str.len()
data['timeSec'] = data.time.str.split(':').apply( lambda x: int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2]) )
data['numWords'] = data.text.str.split(' ').apply( lambda x: len(x))

#plt.scatter(data.timeSec[0:3000], data.length[0:3000], marker = '.', color='red', s=4, grid)
#plt.show()

sns.lmplot('timeSec', 'length',
            data = data,
            fit_reg = False,
            hue='speaker',
            scatter_kws={'s': 5})
            
sns.lmplot('timeSec', 'numWords',
            data = data,
            fit_reg = False,
            scatter_kws={'s': 5})
