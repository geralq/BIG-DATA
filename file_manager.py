import os


class FileManager:
    def __init__(self):
        pass

    def makedirs(self, directory):
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception as e:
            print(f"Error creating directory {directory}: {str(e)}")

    def join(self, *args):
        return os.path.join(*args)

    def listdir(self, directory):
        return os.listdir(directory)

    def rename(self, file_path, new_file_path):
        os.rename(file_path, new_file_path)