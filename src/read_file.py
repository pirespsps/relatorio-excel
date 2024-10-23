import pandas as pd
import os

class ReadFile:
    
    def read_coffeesales(self):

        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.dirname(path)
        
        path_file =  os.path.join(path,'planilhas','coffeeshopsales.xlsx')

        table_sales = pd.read_excel(path_file)

        print(table_sales.loc[0,:])
        print(table_sales.shape)