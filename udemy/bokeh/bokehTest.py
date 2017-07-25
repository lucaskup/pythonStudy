from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

start = datetime.datetime(2017,1,15)
end = datetime.datetime(2017,1,30)
df = data.DataReader(name='GOOG',data_source='yahoo',start=start,end=end)
#df

def inc_dec(c,o):
    return 'Increase' if c>=o else 'Decrease'

df['Status'] = [inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df['Middle'] = (df.Open+df.Close)/2
df['Height'] = abs(df.Open-df.Close)


p=figure(x_axis_type='datetime',width=1000,height=300,responsive=True)
p.title.text = 'Candle'
p.grid.grid_line_alpha=0.3

hours_12 = 12*60*60*1000

p.segment(df.index,df.High,df.index,df.Low,color='Black')
p.rect(df.index[df.Status=='Increase'],df.Middle[df.Status=='Increase'],
hours_12,df.Height[df.Status=='Increase'],fill_color='#CCCFFF',line_color='black')
p.rect(df.index[df.Status=='Decrease'],df.Middle[df.Status=='Decrease'],
           hours_12,df.Height[df.Status=='Decrease'],fill_color='#FF3333',line_color='black')


output_file('cs.html')
show(p)
