import pandas as pd

def highlight_high_percent(s, thr=50):
    is_high = s > thr
    return ['background-color: lightcoral' if v else '' for v in is_high]

def missing_data(df):
    total = df.isnull().sum().sort_values(ascending = False)
    percent = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending = False)
    missing_data  = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])    
    styled_df = missing_data.style.apply(highlight_high_percent, subset=['Percent'])
    
    display(styled_df)