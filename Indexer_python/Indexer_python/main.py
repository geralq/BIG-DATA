from controller import Controller

if __name__ == "__main__":
    content_path = 'datalake/content'
    json_file_path = 'index.json'

    controller = Controller(content_path, json_file_path)
    controller.run()