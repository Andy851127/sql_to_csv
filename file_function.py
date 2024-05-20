import os
import shutil
from datetime import datetime

class CheckFiles:
    """
    檢查 uploadFiles 路徑下，有無參數檔，有的話就會啟動後續程式。
    """
    def __init__(self):
        self.uploadFilesPath = r".\data\uploadFiles"

    def get_all_filename(self):
        # 使用 os.path.join() 构建完整路径
        full_path = os.path.join(os.getcwd(), self.uploadFilesPath)

        # 获取该路径下的所有 .json 文件，仅保存文件名不带扩展名
        allFileNames = [os.path.splitext(file)[0] for file in os.listdir(full_path) if file.endswith(".json")]
        
        return allFileNames

class FileMover:
    """
    程式執行完後，搬移檔案到 moveFileSpace 路徑。
    """
    def __init__(self):
        self.source_path = r".\data\uploadFiles"
        self.destination_path = r".\data\moveFileSpace"

    def move_file_with_timestamp(self, file_name):
        try:
            file_name = file_name+'.json'

            # 构建目标文件名，附加当前日期时间
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_file_name = f"{os.path.splitext(file_name)[0]}_{timestamp}{os.path.splitext(file_name)[1]}"

            # 构建完整的源文件路径和目标文件路径
            source_file_path = os.path.join(self.source_path, file_name)
            destination_file_path = os.path.join(self.destination_path, new_file_name)

            # 使用 shutil 进行文件移动
            shutil.move(source_file_path, destination_file_path)

            print(f"File moved successfully to: {destination_file_path}")
        except FileNotFoundError:
            print(f"Error: File {file_name} not found.")
        except Exception as e:
            print(f"Error moving file: {e}")


if __name__ == "__main__":
    readfiles = CheckFiles()
    result = readfiles.get_all_filename()
    print(result)