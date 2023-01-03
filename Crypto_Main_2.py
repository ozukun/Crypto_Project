# %% [code] {"datalore":{"node_id":"CPSZUCm8TRfQma38N7JcXZ","type":"CODE","hide_input_from_viewers":false,"hide_output_from_viewers":false,"report_properties":{"y":0}},"execution":{"iopub.status.busy":"2023-01-02T23:02:39.487545Z","iopub.execute_input":"2023-01-02T23:02:39.488284Z","iopub.status.idle":"2023-01-02T23:02:50.972552Z","shell.execute_reply.started":"2023-01-02T23:02:39.488246Z","shell.execute_reply":"2023-01-02T23:02:50.971334Z"}}
pip3  install yfinance


# %% [code] {"datalore":{"node_id":"FoatVDOrLGP6laGjnwlfnR","type":"CODE","hide_input_from_viewers":false,"hide_output_from_viewers":false,"report_properties":{"y":13}},"execution":{"iopub.status.busy":"2023-01-02T23:02:50.975465Z","iopub.execute_input":"2023-01-02T23:02:50.975850Z","iopub.status.idle":"2023-01-02T23:03:02.394709Z","shell.execute_reply.started":"2023-01-02T23:02:50.975802Z","shell.execute_reply":"2023-01-02T23:03:02.393590Z"}}
#pip install yahooquery

# %% [code] {"datalore":{"node_id":"H3ui50NDi4fJriFxYilYKo","type":"CODE","hide_input_from_viewers":false,"hide_output_from_viewers":false,"report_properties":{"y":26}},"execution":{"iopub.status.busy":"2023-01-02T23:03:02.396915Z","iopub.execute_input":"2023-01-02T23:03:02.397848Z","iopub.status.idle":"2023-01-02T23:03:02.403788Z","shell.execute_reply.started":"2023-01-02T23:03:02.397787Z","shell.execute_reply":"2023-01-02T23:03:02.402940Z"}}
# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

from re import search
from yahooquery import Screener

# %% [code] {"datalore":{"node_id":"6JxajwzPWnMFZS2d1OrNBW","type":"CODE","hide_input_from_viewers":false,"hide_output_from_viewers":false,"report_properties":{"y":34}},"execution":{"iopub.status.busy":"2023-01-02T23:03:02.407720Z","iopub.execute_input":"2023-01-02T23:03:02.408994Z","iopub.status.idle":"2023-01-02T23:03:02.441134Z","shell.execute_reply.started":"2023-01-02T23:03:02.408944Z","shell.execute_reply":"2023-01-02T23:03:02.439427Z"}}
def getRates(ticker_input ,period_input  ,interval_input ):
    print(ticker_input+" "+period_input+" "+interval_input )
    data = yf.download(tickers=ticker_input, period = period_input, interval = interval_input)
    return data["Close"] 

# %% [code] {"datalore":{"node_id":"4mQddsK6Kn1E80GMFpl6Tp","type":"CODE","hide_input_from_viewers":false,"hide_output_from_viewers":false,"report_properties":{"y":38}},"execution":{"iopub.status.busy":"2023-01-02T23:03:02.443144Z","iopub.execute_input":"2023-01-02T23:03:02.443615Z","iopub.status.idle":"2023-01-02T23:03:02.455387Z","shell.execute_reply.started":"2023-01-02T23:03:02.443573Z","shell.execute_reply":"2023-01-02T23:03:02.454283Z"}}
def getPercChange(d):
    x=round(d.head(1),6).values
    y=round(d.tail(1),6).values
    perc_chg= np.round( (  (y-x) / abs(x)  ) *100  , 4)
    return perc_chg

# %% [code] {"datalore":{"node_id":"vhw7l8XSmGyXSpej3qhdOU","type":"CODE","hide_input_from_viewers":false,"hide_output_from_viewers":false,"report_properties":{"y":43}},"execution":{"iopub.status.busy":"2023-01-02T23:03:02.457127Z","iopub.execute_input":"2023-01-02T23:03:02.457562Z","iopub.status.idle":"2023-01-02T23:03:02.469424Z","shell.execute_reply.started":"2023-01-02T23:03:02.457523Z","shell.execute_reply":"2023-01-02T23:03:02.468328Z"}}
def mail2me(pair_text,message_text):
    from email.message import EmailMessage
    import smtplib
    from pretty_html_table import build_table

    sender = "ozukun83@gmail.com"
    recipient = "ozukun83@gmail.com"
    message = "Crypto Info all"

    password = input("Type your password and press enter: ")
    
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = "Crypto Rates Python!"+"  "+pair_text
    email.set_content(message_text)

    
    
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(sender, password)
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()
    print("Mail succeed !!")

# %% [code] {"datalore":{"node_id":"1jlMSBDnUItaxbloN7Pl1j","type":"CODE","hide_input_from_viewers":false,"hide_output_from_viewers":false,"report_properties":{"y":55}},"execution":{"iopub.status.busy":"2023-01-02T23:03:02.471051Z","iopub.execute_input":"2023-01-02T23:03:02.471606Z","iopub.status.idle":"2023-01-02T23:03:03.337697Z","shell.execute_reply.started":"2023-01-02T23:03:02.471570Z","shell.execute_reply":"2023-01-02T23:03:03.336079Z"}}
# get all crypto pairs with USD
def getCryptoPairs():
    s = Screener()
    tickers=[]
    data = s.get_screeners('all_cryptocurrencies_us', count=10)

    # data is in the quotes key
    dicts = data['all_cryptocurrencies_us']['quotes']
    symbols = [d['symbol'] for d in dicts]
    symbols[0]

    for s in symbols:
        if  search("USD", s) and not search("USDT", s) and not search("USDC", s): #\
        #and ( search("ETH",s) or search("DOGE",s) ):
            #print(s+"\n")
            tickers.append(s)
             
    return tickers
        

for cp in getCryptoPairs():
    print(cp)

# %% [code] {"datalore":{"node_id":"8AquFUAnVwuDujCl6UdcpJ","type":"CODE","hide_input_from_viewers":true,"hide_output_from_viewers":true},"execution":{"iopub.status.busy":"2023-01-02T23:03:04.387539Z","iopub.execute_input":"2023-01-02T23:03:04.388127Z","iopub.status.idle":"2023-01-02T23:03:12.950734Z","shell.execute_reply.started":"2023-01-02T23:03:04.388093Z","shell.execute_reply":"2023-01-02T23:03:12.949233Z"}}
Crypto_Pairs=["BTC-USD","ETH-USD"]

message_input=""
final_message=""
for cp in Crypto_Pairs:
    print(cp)
    df_tmp=getRates(cp,  '3mo',  '1h')
    message_input=cp+"   First: "+str( round( df_tmp.head(1)[0] ,6 ) )+"  "+"Last: "+str( round(df_tmp.tail(1)[0] ,6)  )
    df3mo=getRates(cp,  '3mo',  '1h')
    message_input0=cp+"  '3mo',  '1h' CHANGE % " +str( getPercChange(df3mo)[0])
    
    df1mo=getRates(cp,  '1mo',  '1h')
    message_input1=cp+"  '1mo',  '1h' CHANGE % " +str( getPercChange(df1mo)[0])
    
    dfwk=getRates(cp,'1wk',  '1h')
    message_input2=cp+"  '1wk',  '1h' CHANGE % " +str( getPercChange(dfwk)[0])
    
    message_input=message_input+"\n"+message_input0+"\n"+message_input1+"\n"+message_input2+"\n"+"\n"
    final_message=final_message+message_input
    print(final_message)
    
    
#mail2me("All Crypto Pairs",final_message) 

# %% [code] {"execution":{"iopub.status.busy":"2023-01-02T23:03:12.954714Z","iopub.execute_input":"2023-01-02T23:03:12.955234Z","iopub.status.idle":"2023-01-02T23:04:28.496511Z","shell.execute_reply.started":"2023-01-02T23:03:12.955186Z","shell.execute_reply":"2023-01-02T23:04:28.494749Z"}}
def getRatesTable(*args):
    df_table = pd.DataFrame()
    for cp in args:
        df10yr=getRates(cp, '10y',  '1d')
        df5yr=getRates(cp,  '5y',  '1d')
        df3yr=getRates(cp,  '3y',  '1d')
        df1yr=getRates(cp,  '1y',  '1d')
        df3mo=getRates(cp,  '3mo',  '1h')
        df1mo=getRates(cp,  '1mo',  '1h')
        df1wk=getRates(cp,  '1wk',  '1h')
        df1dy=getRates(cp,  '1dy',  '1h')
        new_row = pd.Series(data={
                                   'Crypto_Pair':cp,
                                   '10yr_d_CHG%':getPercChange(df10yr)[0],
                                   '5yr_d_CHG%':getPercChange(df5yr)[0],
                                   '3yr_d_CHG%':getPercChange(df3yr)[0],
                                   '1yr_d_CHG%':getPercChange(df1yr)[0], 
                                   '3mo_h_CHG%':getPercChange(df3mo)[0], 
                                   '1mo_h_CHG%':getPercChange(df1mo)[0] ,
                                   '1wk_h_CHG%':getPercChange(df1wk)[0],
                                   '1dy_h_CHG%':getPercChange(df1dy)[0], 
                                 } 
                           )
        
        df_table = df_table.append(new_row, ignore_index=True)
    return df_table

#--------------------------------------------------------------------


Crypto_Pairs=["BTC-USD","ETH-USD","ALGO-USD","SOL-USD","LUNC-USD","ROSE-USD","SHIB-USD","XRP-USD","ADA-USD"]

dfx=getRatesTable(*Crypto_Pairs)

dfx



# %% [code] {"execution":{"iopub.status.busy":"2023-01-02T23:40:02.987655Z","iopub.execute_input":"2023-01-02T23:40:02.988191Z","iopub.status.idle":"2023-01-02T23:40:02.999320Z","shell.execute_reply.started":"2023-01-02T23:40:02.988154Z","shell.execute_reply":"2023-01-02T23:40:02.997745Z"}}
def mail2me_v2(df,mail_subject,message_text):
    
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from smtplib import SMTP
    import smtplib
    import sys


    recipients = ['ozukun83@gmail.com'] 
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = mail_subject
    msg['From'] = 'ozukun83@gmail.com'

    password = input("Type your password and press enter: ")
    

    html = """\
    <html>
      <head></head>
      <body>
        {0}
      </body>
    </html>
    """.format(df.to_html())

    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    body = message_text
    body = MIMEText(body) # convert the body to a MIME compatible string
    msg.attach(body)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("ozukun83@gmail.com",password)
    server.sendmail(msg['From'], emaillist , msg.as_string())
    print("Mail succeed !!")
    
#---------------------------------------------------------------------------
#mail2me_v2(dfx,"Crypto Rate changes","")

# %% [code] {"execution":{"iopub.status.busy":"2023-01-02T23:47:02.927751Z","iopub.execute_input":"2023-01-02T23:47:02.928234Z","iopub.status.idle":"2023-01-02T23:47:11.705509Z","shell.execute_reply.started":"2023-01-02T23:47:02.928199Z","shell.execute_reply":"2023-01-02T23:47:11.704154Z"}}
# moving average
def get_ma(prices, rate):
    return prices.rolling(rate).mean()



def get_bollinger_bands(prices, rate=7):
    sma = get_ma(prices, rate)
    std = prices.rolling(rate).std()
    bollinger_up = sma + std * 2 # Calculate top band
    bollinger_down = sma - std * 2 # Calculate bottom band
    return bollinger_up, bollinger_down

#---------------------------------------------------------------


df_tmp_f = pd.DataFrame()
final_text=""
Crypto_Pairs=["ALGO-USD","LUNC-USD"]


for cp in Crypto_Pairs:

    df_tmp_0 = pd.DataFrame(getRates(cp,  '1y',  '1d'))

    bollinger_up, bollinger_down = get_bollinger_bands(df_tmp_0)


    df_tmp = pd.DataFrame(data=np.column_stack((df_tmp_0.values,bollinger_up,bollinger_down)),columns=['Price','Bol_Up','Bol_Down'])
    df_tmp.insert(0,'Crypto_Pair',cp)
    df_tmp.index=df_tmp_0.index


    display( df_tmp.iloc[-7:] )
    x=round( df_tmp["Bol_Up"].iloc[-7:].mean() ,6 )
    
    print("Bol_Up__Mean_for_last_7days   : " + str( x ) )
    x1="Bol_Up__Mean_for_last_7days   : " + str( x ) 
    
    y=round( df_tmp["Bol_Down"].iloc[-7:].mean() ,6 )
    print("Bol_Down__Mean_for_last_7days : " + str( y ) )
    
    x1="Bol_Up__Mean_for_last_7days   : " + str( x )
    y1="Bol_Down__Mean_for_last_7days : " + str( y )
    
    df_tmp_f = df_tmp_f.append(df_tmp.iloc[-7:])
    final_text=final_text+"\n"+cp+"\n"+str(x1)+"\n"+str(y1)
#---------------------------------------------------------------------------
#mail2me_v2(df_tmp_f,"Crypto Bollinger bands",final_text)

# %% [code] {"datalore":{"node_id":"fZ2kqufKWGqwFW2e0HZX0c","type":"CODE","hide_input_from_viewers":true,"hide_output_from_viewers":true},"execution":{"iopub.status.busy":"2023-01-02T23:04:28.510983Z","iopub.execute_input":"2023-01-02T23:04:28.511543Z","iopub.status.idle":"2023-01-02T23:04:28.594093Z","shell.execute_reply.started":"2023-01-02T23:04:28.511495Z","shell.execute_reply":"2023-01-02T23:04:28.592893Z"}}
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)

def getLine(df_input):
    x = df_input.index
    y = df_input.values
    fig = go.Figure(data=go.Scatter(x = x, y = y))
    fig.show()

# %% [code] {"execution":{"iopub.status.busy":"2023-01-02T23:04:28.595641Z","iopub.execute_input":"2023-01-02T23:04:28.596097Z","iopub.status.idle":"2023-01-02T23:04:32.775446Z","shell.execute_reply.started":"2023-01-02T23:04:28.596052Z","shell.execute_reply":"2023-01-02T23:04:32.774305Z"}}
( getLine(getRates('ETH-USD',  '1d',  '1h')) )
( getLine(getRates('ETH-USD',  '1wk',  '1h')) )
( getLine(getRates('ETH-USD',  '3mo',  '1h')) )
( getLine(getRates('ETH-USD',  '3y',  '1d')) )
