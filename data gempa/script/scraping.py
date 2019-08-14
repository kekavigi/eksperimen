import requests
import pandas as pd
from bs4 import BeautifulSoup

def downloader(session_id, year, total_halaman):
    for halaman in range(1,2+total_halaman):
        page = "http://repogempa.bmkg.go.id/proses_query2.php?halaman=" + str(halaman) + "&id=101&session_id=" + session_id +\
               "&output_format=origin&start_day=1&end_day=31&start_month=01&end_month=12&" + "start_year=" + year +\
               "&end_year=" + year + "&top_lat=6&bot_lat=-11&left_long=94&right_long=142&min_mag=1&max_mag=10&min_depth=1&max_depth=1000"
        # ambil table
        page = requests.get(page)
        soup = BeautifulSoup(page.content, 'html.parser')
        html = soup.find_all('pre')[0]
        table= html.find_all('table')[0]


        # Finding number of rows
        n_columns, n_rows = 13,0
        for row in table.find_all('tr'):
            # Determine the number of rows in the table
            td_tags = row.find_all('td')
            if len(td_tags) > 0:
                n_rows+=1

        df = pd.DataFrame(columns = range(0,n_columns),
                          index   = range(0,n_rows))
        row_marker = 0
        for row in table.find_all('tr'):
            column_marker = 0
            columns = row.find_all('td')
            for column in columns:
                df.iat[row_marker,column_marker] = column.get_text()
                column_marker += 1
            if len(columns) > 0:
                row_marker += 1
                
        # fixing header
        #new_header = df.iloc[0]
        df = df[1:]
        #df.columns = new_header

        # saving files
        filename = '~/aaaBMKG/' + year + '.ods'
        df.to_csv(filename, header=None, index=None, sep='|', mode='a')
