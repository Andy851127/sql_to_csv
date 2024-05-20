from sqlalchemy import create_engine
import json

class Engine:
    """
    建立所有 FLOW 各自的引擎。
    """
    def __init__(self):
        self.json_path = r'.\config\connection.json'
    
    def createMariadbEngine(self,connectionDatas):
        # 設定資料庫連線字串
        mariaEngines = {}
        dbConfigs = connectionDatas["mariaDBconnectionList"]
        for dbConfig in dbConfigs:
            maria_connection = f'mysql+pymysql://{dbConfig["user"]}:{dbConfig["password"]}@{dbConfig["host"]}:3306/{dbConfig["dbname"]}'
            mariaEngine = create_engine(maria_connection)
            mariaEngines[dbConfig["dbname"]] = mariaEngine
        return mariaEngines
    
    def createOracledbEngine(self,connectionDatas):
        oracleEngines = {}
        dbConfigs = connectionDatas["oracleDBconnectionList"]
        for dbConfig in dbConfigs:
            oracle_connection = f'oracle+cx_oracle://{dbConfig["user"]}:{dbConfig["password"]}@{dbConfig["host"]}:{dbConfig["port"]}/{dbConfig["serviceName"]}'
            oracleEngine = create_engine(oracle_connection)
            oracleEngines[dbConfig["serviceName"]] = oracleEngine
        return oracleEngines
    
    def create_engine(self):
        with open(self.json_path, 'r') as file:
            connectionDatas = json.load(file)
            
        mariaEngines = self.createMariadbEngine(connectionDatas)
        oracleEngines = self.createOracledbEngine(connectionDatas)
        return mariaEngines,oracleEngines
        
if __name__ == "__main__":
    engine = Engine()
    mariaEngines,oracleEngines = engine.create_engine()
    print(mariaEngines)
    print(oracleEngines)