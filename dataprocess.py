import pandas as pd
from database.engine import Engine
from datetime import datetime

class DataProcessing:
    """
    取得 SQL Engine、SQLQuery、DBType、DBName、FileName 後，執行：
    1. sql_to_dataframe 產生 DataFrame
    2. dataframe_to_csv 將 DataFrame 轉換成 CSV 檔案
    """
    def __init__(self):
        engine = Engine()
        self.mariaEngines,self.oracleEngines = engine.create_engine()

    def sql_to_dataframe(self,sql_query,dbtype,dbName):
        sql_query = sql_query
        if dbtype == "oracle":
            engineName = self.oracleEngines[f"{dbName}"]
        elif dbtype == "maria":
            engineName = self.mariaEngines[f"{dbName}"]
            
        # 使用 read_sql 方法從 SQL 表格中讀取數據並創建 DataFrame
        dataframe = pd.read_sql(sql_query, con=engineName)
        
        return dataframe
        
    def dataframe_to_csv(self,dataframe,fileName):
        csv_file_path = rf'.\data\generateFiles/{fileName}.csv'
        dataframe.to_csv(csv_file_path, index=False,encoding = 'utf-8')
        return True
    
    def data_processing(self,sql_query,dbtype,dbName,fileName):
        dataframe = self.sql_to_dataframe(sql_query,dbtype,dbName)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_file_name = f"{fileName}_{timestamp}"

        self.dataframe_to_csv(dataframe, new_file_name)
        
        return True