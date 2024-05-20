from scheduler.scheduler import Apscheduler
from database.sql.sql_function import SQLfunction
from dataprocess import DataProcessing
from file_function import CheckFiles,FileMover

class Main():
    def __init__(self):
        """
        實體化模組
        """
        self.apscheduler = Apscheduler()
        self.checkFiles = CheckFiles()
        self.dataprocess = DataProcessing()
        self.sql_function = SQLfunction()
        self.fileMover = FileMover()

    def process_job(self):
        """
        呼叫各模組程式
        """
        all_files = self.checkFiles.get_all_filename()

        for fileName in all_files:
            sqlQuery, dbType, dbName = self.sql_function.get_sql_query_value(fileName)
            self.dataprocess.data_processing(sqlQuery, dbType, dbName, fileName)
            self.fileMover.move_file_with_timestamp(fileName)

        return True

    def main_process(self):
        self.apscheduler.scheduler_process(self.process_job)
        return True


if __name__ == "__main__":
    main = Main()
    main.main_process()