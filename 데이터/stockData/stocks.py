import pandas as pd

#soxl 주식의 가격 기본 정보 구하기
df = pd.read_csv(r"C:\Users\ERC\Documents\GitHub\PythonBasic\데이터\stockData\SOXL.csv")

# 앞 부분만 출력해보기 
print(df.head())

#기초통계량 구하기
print(df['Low'].describe())
 
# 이 주식의 월별 통계를 구하기 
# Convert 'Date' column to datetime format (skip this step if 'Date' is already in datetime format)
df['Date'] = pd.to_datetime(df['Date'])

# Extracting the month from the 'Date' column and creating a new 'Month' column
df['Month'] = df['Date'].dt.month

# Grouping the data by month and calculating the mean for 'High' and 'Low'
monthly_average = df.groupby('Month')[['High', 'Low']].mean()
 
print(monthly_average)
 
#월별 차트 그리기 
import matplotlib.pyplot as plt
# Plotting the data
plt.figure(figsize=(10, 6))  # Set the figure size (width, height)

# Plotting 'High' and 'Low' values
plt.plot(monthly_average) 

# Customize the plot
plt.title('Monthly Average High and Low Values')
plt.xlabel('Month')
plt.ylabel('Average Price')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()