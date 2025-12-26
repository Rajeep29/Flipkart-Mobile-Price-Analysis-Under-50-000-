📌 Project Overview

This project focuses on web scraping, data cleaning, analysis, and visualization of mobile phones priced under ₹50,000 listed on Flipkart.
The goal is to extract meaningful insights such as top brands, pricing trends, and best-rated phones using Python.

🎯 Objectives

Scrape mobile phone data from Flipkart

Clean and preprocess raw web data

Perform exploratory data analysis (EDA)

Identify top brands and best-value phones

Visualize brand popularity

🛠️ Tools & Libraries Used

Python

Requests – for HTTP requests

BeautifulSoup – for web scraping

Pandas – data cleaning & analysis

NumPy – numerical operations

Matplotlib & Seaborn – data visualization

📂 Data Collected

The following attributes were extracted:

product_name

price

description

reviews (ratings)

brand (derived from product name)

🧹 Data Cleaning & Processing

Removed duplicate products

Converted price from string (₹, commas) to integer

Handled missing review values using median

Extracted brand names from product titles

📊 Analysis Performed

Top 10 mobile brands by number of products

Average price of mobiles by brand

Best phones based on highest rating & lowest price

Brand-wise popularity analysis

📈 Visualization

Bar chart showing Top 10 Mobile Brands on Flipkart

Used Seaborn and Matplotlib for clear insights

Key Insights

Certain brands dominate the under ₹50K segment

High-rated phones are not always the most expensive

Brand popularity varies significantly across listings
