import pandas as pd
import matplotlib.pyplot as plt

# Sample data (replace this with your actual DataFrame)
data = {
    'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'High': [13.055500, 16.591579, 16.459565, 15.790526, 16.789545, 24.121905, 23.664762, 19.827391, 12.269048, 9.207619, 11.894286, 11.836190],
    'Low': [12.078000, 15.340000, 15.215652, 14.846842, 15.710000, 22.703809, 22.176191, 18.222174, 11.256190, 8.225238, 10.872381, 10.916667]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Plotting the data
plt.figure(figsize=(10, 6))  # Set the figure size (width, height)

# Plotting 'High' and 'Low' values
plt.plot(df['Month'], df['High'], label='High', color='blue', marker='o')
plt.plot(df['Month'], df['Low'], label='Low', color='red', marker='o')

# Customize the plot
plt.title('Monthly Average High and Low Values')
plt.xlabel('Month')
plt.ylabel('Average Price')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()