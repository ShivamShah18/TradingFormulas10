from pandas import DataFrame
import pandas as pd 


def calcPivots(df:DataFrame):
    daily_data = df.resample('D').last()
    daily_data=daily_data.dropna(subset="Open")

    pp=((daily_data['High']+daily_data['Low']+daily_data['Close'])/3)
    s1=(2*pp)-daily_data['High']
    r1=(2*pp)-daily_data['Low']
    s2=(pp-(daily_data['High']-daily_data['Low']))
    r2=(pp+(daily_data['High']-daily_data['Low']))
    s3=pp-(2*(daily_data['High']-daily_data['Low']))
    r3=pp+(2*(daily_data['High']-daily_data['Low']))

    df_daily=pd.DataFrame()
    df_daily["R3"]=r3.shift(1)
    df_daily["R2"]=r2.shift(1)
    df_daily["R1"]=r1.shift(1)
    df_daily["Pivot Point"]=pp.shift(1)
    df_daily["S1"]=s1.shift(1)
    df_daily["S2"]=s2.shift(1)
    df_daily["S3"]=s3.shift(1)
    #df_daily=df_daily.dropna()
    count_pp_pos=0
    count_pp_pos_array=[]

    count_r1=0
    count_r1_array=[]

    count_r2=0
    count_r2_array=[]

    count_r3=0
    count_r3_array=[]

    count_pp_neg=0
    count_pp_neg_array=[]

    count_s1=0
    count_s1_array=[]

    count_s2=0
    count_s2_array=[]

    count_s3=0
    count_s3_array=[]

    for i,curr_date in enumerate(df_daily.index, start=0):
        data_for_specific_date = df[df.index.date == pd.to_datetime(curr_date).date()]
        
        
    # PP and R1
        for j in range(len(data_for_specific_date)):
            if data_for_specific_date["Close"].iloc[j]>=df_daily["Pivot Point"].iloc[i] and data_for_specific_date["Close"].iloc[j]<=df_daily["R1"].iloc[i]:
                if count_pp_pos==10:
                    count_pp_pos_array.append(count_pp_pos)
                else:
                    count_pp_pos+=1
                    count_pp_pos_array.append(count_pp_pos)
            else:
                count_pp_pos=0
                count_pp_pos_array.append(count_pp_pos)
                
    # R1 R2          
        for j in range(len(data_for_specific_date)):
            if data_for_specific_date["Close"].iloc[j]>df_daily["R1"].iloc[i] and data_for_specific_date["Close"].iloc[j]<=df_daily["R2"].iloc[i]:
                if count_r1==10:
                    count_r1_array.append(count_r1)
                else:
                    count_r1+=1
                    count_r1_array.append(count_r1)
            else:
                count_r1=0
                count_r1_array.append(count_r1)
                
        # R2 R3
        for j in range(len(data_for_specific_date)):
            if data_for_specific_date["Close"].iloc[j]>df_daily["R2"].iloc[i] and data_for_specific_date["Close"].iloc[j]<=df_daily["R3"].iloc[i]:
                if count_r2==10:
                    count_r2_array.append(count_r2)
                else:
                    count_r2+=1
                    count_r2_array.append(count_r2)
            else:
                count_r2=0
                count_r2_array.append(count_r2)
                
                
        # R3
                
        for j in range(len(data_for_specific_date)):
            if data_for_specific_date["Close"].iloc[j]>df_daily["R3"].iloc[i]:
                if count_r3==10:
                    count_r3_array.append(count_r3)
                else:
                    count_r3+=1
                    count_r3_array.append(count_r3)
            else:
                count_r3=0
                count_r3_array.append(count_r3)
                
            
                
                
        # PP and S1
        for j in range(len(data_for_specific_date)):
            if data_for_specific_date["Close"].iloc[j]<df_daily["Pivot Point"].iloc[i] and data_for_specific_date["Close"].iloc[j]>=df_daily["S1"].iloc[i]:
                if count_pp_neg==10:
                    count_pp_neg_array.append(count_pp_neg)
                else:
                    count_pp_neg+=1
                    count_pp_neg_array.append(count_pp_neg)
            else:
                count_pp_neg=0
                count_pp_neg_array.append(count_pp_neg)
                
        
        # S1 and S2
        for j in range(len(data_for_specific_date)):
            if data_for_specific_date["Close"].iloc[j]<df_daily["S1"].iloc[i] and data_for_specific_date["Close"].iloc[j]>=df_daily["S2"].iloc[i]:
                if count_s1==10:
                    count_s1_array.append(count_s1)
                else:
                    count_s1+=1
                    count_s1_array.append(count_s1)
            else:
                count_s1=0
                count_s1_array.append(count_s1)
                
                
        # S2 and S3
        for j in range(len(data_for_specific_date)):
            if data_for_specific_date["Close"].iloc[j]<df_daily["S2"].iloc[i] and data_for_specific_date["Close"].iloc[j]>=df_daily["S3"].iloc[i]:
                if count_s2==10:
                    count_s2_array.append(count_s2)
                else:
                    count_s2+=1
                    count_s2_array.append(count_s2)
            else:
                count_s2=0
                count_s2_array.append(count_s2)
                
        
        # S3
        for j in range(len(data_for_specific_date)):
            if data_for_specific_date["Close"].iloc[j]<df_daily["S3"].iloc[i]:
                if count_s3==10:
                    count_s3_array.append(count_s3)
                else:
                    count_s3+=1
                    count_s3_array.append(count_s3)
            else:
                count_s3=0
                count_s3_array.append(count_s3)
                
        
        
        
        

    df["PP R1 Count"]=count_pp_pos_array
    df["R1 R2 Count"]=count_r1_array
    df["R2 R3 Count"]=count_r2_array
    df["R3 Count"]=count_r3_array

    df["PP S1 Count"]=count_pp_neg_array
    df["S1 S2 Count"]=count_s1_array
    df["S2 S2 Count"]=count_s2_array
    df["S3 Count"]=count_s3_array

    len(count_pp_pos_array)
    
    seven_level_count_array=[]
    for i in range(len(count_pp_pos_array)):
        # R1 Cross
        if count_r1_array[i]>0:
            if count_r1_array[i]>=0 and count_r1_array[i]<2:
                seven_level_count_array.append(0)
            
            elif count_r1_array[i]>=2 and count_r1_array[i]<=6:
                seven_level_count_array.append((-2*count_r1_array[i]) +14)
                
            else:
                seven_level_count_array.append(1)
        # S1 Cross   
        elif count_s1_array[i]>0:
            if count_s1_array[i]>=0 and count_s1_array[i]<2:
                seven_level_count_array.append(0)
            
            elif count_s1_array[i]>=2 and count_s1_array[i]<=6:
                seven_level_count_array.append((2*count_s1_array[i]) -14)
                
            else:
                seven_level_count_array.append(-1)
        
        # R2 Cross
        
        elif count_r2_array[i]>0:
            if count_r2_array[i]>=0 and count_r2_array[i]<1:
                seven_level_count_array.append(0)
                
            elif count_r2_array[i]>=1 and count_r2_array[i]<2:
                seven_level_count_array.append(5)
                
            elif count_r2_array[i]>=2 and count_r2_array[i]<=5:
                seven_level_count_array.append((-2*count_r2_array[i]) +11)
            
            else:
                seven_level_count_array.append(1)
        
        # S2 Cross
                
        elif count_s2_array[i]>0:
            if count_s2_array[i]>=0 and count_s2_array[i]<1:
                seven_level_count_array.append(0)
                
            elif count_s2_array[i]>=1 and count_s2_array[i]<2:
                seven_level_count_array.append(-5)
                
            elif count_s2_array[i]>=2 and count_s2_array[i]<=5:
                seven_level_count_array.append((2*count_s2_array[i]) -11)
            
            else:
                seven_level_count_array.append(-1)
                
                
        # R3 Cross
        
        elif count_r3_array[i]>0:
            if count_r3_array[i]>=0 and count_r3_array[i]<1:
                seven_level_count_array.append(0)
                
            elif count_r3_array[i]>=1 and count_r3_array[i]<2:
                seven_level_count_array.append(4)
                
            elif count_r3_array[i]>=2 and count_r3_array[i]<=4:
                seven_level_count_array.append((-2*count_r3_array[i]) +9)
            
            else:
                seven_level_count_array.append(1)
                
        # S3 Cross
        
        elif count_s3_array[i]>0:
            if count_s3_array[i]>=0 and count_s3_array[i]<1:
                seven_level_count_array.append(0)
                
            elif count_s3_array[i]>=1 and count_s3_array[i]<2:
                seven_level_count_array.append(-4)
                
            elif count_s3_array[i]>=2 and count_s3_array[i]<=4:
                seven_level_count_array.append((2*count_s3_array[i]) -9)
            
            else:
                seven_level_count_array.append(-1)
        

        else:
            seven_level_count_array.append(0)
                            

    df["Seven Levels Indicator"]=seven_level_count_array


    sum(seven_level_count_array)


    df.iloc[360:370]

    # df["Seven Levels Indicator"].to_excel("7leveltesting.xlsx",sheet_name='Sheet 1')  
    print(df.head(30))


df = pd.read_excel('/Users/manas/Downloads/Python Files and Dependancies/1 hour data with new formulas.xlsx')
df['Time'] = pd.to_datetime(df['Time'])
df.set_index('Time', inplace=True)
calcPivots(df)
