import pandas as pd
import matplotlib.pyplot as plt

from textblob import TextBlob

data = pd.read_table('cleanedData.txt')
data['length'] = data.text.str.len()
data['timeSec'] = data.time.str.split(':').apply( lambda x: int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2]) )
data['numWords'] = data.text.str.split(' ').apply( lambda x: len(x))
data['hour'] = data.time.str.split(':').apply( lambda x: int(x[0]))
# data['sentiment'] = data.text.apply( lambda x: TextBlob(x).polarity 
# sns.lmplot('timeSec', 'sentiment',
#            data = data,
#            fit_reg = True,
#            scatter_kws={'s': 5})

# plt.show()

# plt.scatter(data.timeSec, data.length, marker = '.', color='red', s=4)
# plt.show()
newIndex = [x for x in range(data.hour.min(),data.hour.max()+1)]
dataByHour = pd.DataFrame(data.groupby('hour').size(), columns=['totalMess'])
dataByHour = dataByHour.reindex(newIndex, fill_value=0)


########## BAR PLOT   TOTAL MESSAGES BY HOUR ##############################
# nasa red : FC3D21  blue:  0B3D91

plt.bar(dataByHour.index, dataByHour.totalMess,
        color='#FC3D21',
        alpha=1.0,
        linewidth=0,
        width=1.0)
# remove tickmarks and borders
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="on", right="off", labelleft="on") 
ax = plt.gca()
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)  
ax.yaxis.grid()

# labels
font = {'fontname':'kalinga'}
plt.title('Messages per hour', **font)
plt.ylabel('Total messages sent', **font)
plt.xlabel('Hour')
plt.show()
##########################################################################

########### BAR PLOT TOTAL MESSAGES PER SPEAKER #########################

speakerCounts = data.groupby('speaker').size().sort_values(ascending=False).iloc[0:4]

xPos = range(len(speakerCounts))

plt.bar(xPos, speakerCounts,
        color='#0B3D91',
        alpha=1.0,
        align='center',
        linewidth=0,
        width=0.6,
        zorder=2)
        
font = 'kalinga'
names = ['Cap Com', 'Jim Lovell', 'John Swigert', 'Fred Haise']
plt.xticks(xPos, names,fontname=font)
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on") 

plt.title('Total Messages per Speaker', fontname=font)
plt.xlabel('Speaker', fontname=font, fontsize=15)


ax = plt.gca()
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)  

rects = ax.patches
labels = speakerCounts

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height-50, label, ha='center', va='top', color='white', fontname=font)

plt.show()
##############################################################






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
