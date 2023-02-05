require 'daru'
df = Daru::DataFrame.new(
    country: ["China", "India", "USA"],
    population: [1433, 1366, 329] # in millions
)

puts df.where(df[:population]>1000) 