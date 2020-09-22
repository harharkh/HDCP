import pandas as pd
from google.colab import data_table

def import_database(n_disks):
  filename = 'https://raw.githubusercontent.com/harharkh/HDCP/master/' + str(n_disks) + 'disk.csv'
  crit_database = pd.read_csv(filename)
  data_table.DataTable(crit_database, include_index=False, num_rows_per_page=10, max_columns=3, min_width='100')
  return crit_database
