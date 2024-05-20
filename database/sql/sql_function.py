import json

class SQLfunction:
    """
    取得 FLOW、Connection、Uert 提供參數檔等資料，組成 SQLQuery 語法。
    """
    def __init__(self):
        self.flowJsonPath = './config/flow.json'
        self.variableJsonPath = './data/uploadFiles'
        self.sqlFilePath = './database/sql'

    def get_flow_variable(self,fileName):
        with open(f'{self.flowJsonPath}', 'r') as file:
            flowVariable = json.load(file)
        
        for flow_dict in flowVariable.get("flowList", []):
            if fileName == flow_dict["fileName"]:
                dbType = flow_dict["dbType"]
                dbName = flow_dict["dbName"]
        return dbType,dbName

    def get_sql_variable(self,fileName):
        with open(f'{self.variableJsonPath}/{fileName}.json', 'r') as file:
            dataVariable = json.load(file)
        return dataVariable

    def get_sql_query(self,fileName):

        with open(f'{self.sqlFilePath}/{fileName}.sql', 'r') as file:
            sql = file.read()
        return sql

    def get_sql_query_value(self,fileName):
        dbType,dbName = self.get_flow_variable(fileName)
        dataVariable = self.get_sql_variable(fileName)
        sqlQuery = self.get_sql_query(fileName)
        
        for key, value in dataVariable.items():
            sqlQuery = sqlQuery.replace(f"{{{key}}}", str(value))
        
        return sqlQuery,dbType,dbName

if __name__ == "__main__":
    sqlfunction = SQLfunction()
    fileName = 'testfile'
    result = sqlfunction.get_sql_query_value(fileName)
    print(result)

        

