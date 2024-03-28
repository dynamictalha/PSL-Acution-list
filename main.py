import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = "https://www.sportsadda.com/cricket/news/pakistan-super-league-psl-players-price-list-2024"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html")
table = soup.find("table")
# print(table)

table_row = table.find_all("tr")
# print(table_row)



table_list = []

for i in table_row:
    table_para = i.find_all("p")
    # print(table_para)
    row_list = [tr.text for tr in table_para]
    # print(row_list)
    table_list.append(row_list)
    

# print(table_list)

df = pd.DataFrame(table_list)

# print(df)
df.to_csv("Player Acution list.csv")


