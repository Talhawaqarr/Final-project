# Barrick Gold Stock Analysis

This is my final data science project where I worked with historical Barrick Gold stock data and went through pretty much the whole basic data science workflow myself.

The main goal of this project was not just to make some graphs and train a model, but to actually understand what the data was saying, clean it properly, create useful features from it, analyze it statistically, visualize it and finally use machine learning to make a prediction.

The dataset contains historical daily stock market data including the opening price, highest price, lowest price, closing price and trading volume.

---

# The Dataset

The dataset I used came from Kaggle:

https://www.kaggle.com/datasets/shakhnoza12/gold-price-analysis-20002026

The main columns in the dataset were:

- `Date` - the trading date
- `Open` - the opening price
- `High` - the highest price during the day
- `Low` - the lowest price during the day
- `close` - the closing price
- `Vol.` - the trading volume

One thing I learned while working on this project was that I should never just assume what a column means because of the dataset title. At first I thought the values in the price columns were the actual price of gold, but after looking deeper into the data I realized that the dataset was actually representing the Barrick Gold stock price series. This made me realize how important it is to understand the data before starting the analysis.

---

# Project Workflow

The project was split into a few main parts:

1. Getting and understanding the raw data
2. Cleaning the data using a Python script
3. Loading the cleaned data into the analysis notebook
4. Exploratory data analysis
5. Creating derived columns
6. Statistical analysis
7. Creating and customizing visualizations
8. Building a machine learning model
9. Evaluating the model
10. Writing conclusions from the results

---

# Data Cleaning

For this project I made a separate `clean.py` script instead of doing all the cleaning directly inside my notebook.

This was something I had not really done before, since most of my previous cleaning work was done inside notebooks.

The raw dataset had some issues that needed to be handled before analysis.

The cleaning script:

- Loads the raw CSV file
- Removes unnecessary rows from the beginning of the dataset
- Fixes the column names
- Converts the `Date` column into a proper datetime format
- Converts the price columns into numeric values
- Converts the volume column into numeric values
- Handles invalid values using numeric conversion
- Removes missing values
- Saves the final cleaned dataset as a new CSV file

I also used functions for different cleaning steps instead of putting everything into one huge block of code.

For example, I made separate functions for fixing the columns, converting data types and removing missing values.

I also used `try` and `except` to handle errors when loading, cleaning and saving the data.

This made me realize that a cleaning script should not just work when everything goes perfectly. It should also be able to handle common problems like a missing file or invalid data.

The cleaned dataset is saved as:

`gold_stock_cleaned.csv`

---

# Analysis

After cleaning the data, I loaded the cleaned CSV into `analysis.ipynb`.

I also converted the Date column back into a datetime when loading the CSV and used it as the index so that working with the time series became easier.

The analysis was focused on understanding how the stock behaved over time instead of just making random graphs.

Some of the things I looked at included:

- How the closing price changed over time
- Price trends
- Daily price movements
- Returns
- Volatility
- Drawdowns
- Trading volume
- Yearly trends
- Relationships between different variables
- Moving averages
- The biggest positive and negative movements

---

# Derived Columns

One of the most useful parts of the project was creating new columns from the original data.

Instead of only working with:

`Open, High, Low, Close and Volume`

I created additional features that gave me a better statistical overview of the stock.

Some of the derived columns included:

### Daily Return

I calculated the percentage change between the current closing price and the previous closing price.

This helped me understand how much the stock moved from one trading day to another.

### Log Return

I also calculated log returns as another way of measuring price changes.

### MA50

A 50-day moving average was created to show the shorter-term trend of the stock.

### MA200

A 200-day moving average was created to show the longer-term trend.

### Volatility21d

I calculated rolling 21-day volatility using the standard deviation of daily returns and annualized it.

This gave me a better idea of how much the stock was fluctuating during different periods.

### RollingMax

I calculated the highest closing price reached up to each point in the dataset.

### Drawdown

Using the rolling maximum, I calculated how far the current price had fallen from its previous peak.

This was useful for seeing periods where the stock experienced large declines.

### Year and Month

I extracted the year and month from the Date column so I could group the data and compare different periods.

### DollarVolume

I also calculated the approximate value of shares traded by multiplying the closing price by the trading volume.

Creating these derived columns showed me how much more useful a dataset can become when you create features that actually describe the behavior you are trying to analyze.

---

# Statistical Analysis

One of the biggest things I learned from this project was how important statistics are in data science.

Before this project I mostly thought of data analysis as loading a dataset, cleaning it and making graphs.

Working with this dataset made me realize that statistics is what actually helps you understand what the graphs and numbers are telling you.

I used things like:

- Mean
- Standard deviation
- Correlation
- Percentage change
- Rolling averages
- Returns
- Volatility
- Drawdown
- Grouping by year and month

For example, instead of just looking at a graph and saying that the stock was "volatile", I could actually calculate volatility and compare different periods.

Instead of just saying that two variables looked related, I could calculate their correlation.

This made the analysis much more meaningful because I was able to support observations with actual numbers instead of just guessing from a graph.

---

# Data Visualization

I used both Matplotlib and Plotly to visualize the data.

I created different types of graphs depending on what I was trying to understand.

Some of the visualizations included:

- Line charts for price trends
- Bar charts for comparisons between different periods
- Histograms for distributions
- Scatter plots for relationships between variables
- Moving average charts
- Other visualizations for returns, volatility and stock behavior

I also spent time customizing the graphs instead of leaving them with the default Python appearance.

I changed things like:

- Graph colors
- Background themes
- Titles
- Axis labels
- Figure sizes
- Legends
- Line styles
- Layouts
- Plot themes

For some of the Plotly graphs I used Plotly's documentation to understand how different themes, colors, layouts and graph settings worked.

This was actually useful because I learned that visualization is not only about making a graph exist. The way the graph is designed can make the information much easier to understand.

I also experimented with different graph types instead of forcing every question into a simple line chart.

---

# Machine Learning

For the machine learning part of the project I used Linear Regression.

The goal was to make a simple prediction of the next trading day's closing price.

I created a target column using the next day's closing price.

The model used features such as:

- Open
- High
- Low
- Close
- Volume
- Daily Return
- MA50
- MA200
- Volatility

Since this is time-series data, I did not randomly shuffle the data for the train/test split.

Instead, I trained the model on the earlier part of the dataset and tested it on the later part.

This is important because using future data to train a model that is supposed to predict the future would give an unrealistic evaluation.

---

# Model Evaluation

I evaluated the Linear Regression model using:

- R-squared
- Mean Absolute Error

R-squared helped me understand how much of the variation in the target could be explained by the model.

Mean Absolute Error helped me understand how far the predictions were from the actual closing prices on average.

I wanted to use an evaluation method that actually made sense for a regression problem instead of using classification metrics like accuracy or a confusion matrix.

---

# Things I Learned

This project taught me way more than I expected.

A lot of the learning came from mistakes I made while building it. At first I was confused about what the price values in the dataset actually represented because I assumed they were the direct price of gold. I learned that understanding the dataset and its columns has to come before analysis.

I also learned the difference between raw data and useful features. The original dataset only had a few columns, but by creating things like daily returns, moving averages, volatility, drawdown and dollar volume, I was able to get a much better statistical view of what was happening.

I ran into problems with data types, missing values and NaNs created by functions like `pct_change()` and `rolling()`. I learned that even when the original dataset has no missing values, the calculations you perform can create them. For example, a 200-day moving average cannot exist for the first 199 rows, and predicting the next day's price creates a missing target for the final row.

I also learned an important lesson about Pandas when I accidentally used `inplace=True` while assigning the result back to the DataFrame. This caused my DataFrame to become `None`, which gave me a `NoneType` error later.

Another mistake I ran into was using Logistic Regression with a continuous stock-price target. That taught me the difference between classification and regression properly. Logistic Regression expects categories such as 0 and 1, while Linear Regression is used when the target is a continuous number such as a stock price.

I also learned that checking for NaN values in one part of the dataset does not automatically mean the data going into the model has no NaNs. I had to learn to check the actual `X_train`, `X_test`, `y_train` and `y_test` being passed into the model.

The biggest thing I learned from the project is that data science is not just about knowing Python or knowing machine learning algorithms. A lot of the work is understanding the data, asking the right questions, cleaning it correctly, creating useful features, using statistics to support your conclusions and then choosing a model that actually matches the problem.

This project also made me realize how important statistics is to data science. Machine learning is only one part of the process. Without statistics and proper analysis, you can make a model and generate predictions without really understanding the data behind them.

---

# Project Files

```text
gold-stock-project/
│
├── clean.py
├── analysis.ipynb
├── gold_stock.csv
├── gold_stock_cleaned.csv
├── gold_stock_cleaned_2ndtry.csv
├── requirements.txt
└── README.md
