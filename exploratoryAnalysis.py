import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

data = pd.read_table('cleanedData.txt')
data['length'] = data.text.str.len()
data['timeSec'] = data.time.str.split(':').apply( lambda x: int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2]) )
data['numWords'] = data.text.str.split(' ').apply( lambda x: len(x))
data['hour'] = data.time.str.split(':').apply( lambda x: int(x[0]))
data['sentiment'] = data.text.apply( lambda x: TextBlob(x).polarity )


print data[data.sentiment > 0.95]


sns.lmplot('timeSec', 'sentiment',
           data = data,
           fit_reg = True,
           scatter_kws={'s': 5})

plt.show()

#plt.scatter(data.timeSec[0:3000], data.length[0:3000], marker = '.', color='red', s=4, grid)
#plt.show()

#sns.lmplot('timeSec', 'length',
#            data = data,
#            fit_reg = False,
#            hue='speaker',
#            scatter_kws={'s': 5})
            
#sns.lmplot('timeSec', 'numWords',
#            data = data,
#            fit_reg = False,
#            scatter_kws={'s': 5})


# meanLngByHour = data.groupby('hour').length.mean()
# newIndex = [x for x in range(data.hour.min(),data.hour.max()+1)]
# meanLngByHour = meanLngByHour.reindex(newIndex,fill_value=0)

# stackedBarChartData = data.groupby('hour').speaker.value_counts()
# stackedBarChartData = stackedBarChartData.unstack(level=-1, fill_value=0).reindex(newIndex, fill_value=0)

# f,ax = plt.subplots()
# barWidth = 0.75
# barX = [i+1 for i in range(len(stackedBarChartData))]

# tick_pos = [i+(barWidth/2) for i in barX] 

# ax.bar(barX, stackedBarChartData.CC, width = barWidth, label = 'CC', color='red')
# ax.bar(barX, stackedBarChartData.CDR, width = barWidth, label = 'CDR', color='blue', bottom = stackedBarChartData.CC)
# ax.bar(barX, stackedBarChartData.CMP, width = barWidth, label = 'CMP', color='green', bottom = stackedBarChartData.CDR + stackedBarChartData.CC)
# ax.bar(barX, stackedBarChartData.LMP, width = barWidth, label = 'LMP', color='purple', bottom = stackedBarChartData.CMP + stackedBarChartData.CDR + stackedBarChartData.CC)
# plt.xticks(tick_pos, stackedBarChartData.index)
# plt.legend(loc='upper left')
# plt.show()