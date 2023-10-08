from file_manager import FileManager


class BookManager:

    fm = FileManager()

    def __init__(self, datalake_dir, metadata_dir, content_dir):
        self.datalake_dir = datalake_dir
        self.metadata_dir = metadata_dir
        self.content_dir = content_dir

    def book_manager(self):
        for file_name in self.fm.listdir(self.datalake_dir):
            if file_name.endswith('.txt'):
                file_path = self.fm.join(self.datalake_dir, file_name)
                with open(file_path, 'r', encoding='utf-8') as book_file:
                    lines = book_file.readlines()
                metadata, content, title = self.__metadata_content_divider(lines=lines)
                title = self.__sanitize_file_name(title) + '.txt'
                new_file_path = self.fm.join(self.datalake_dir, title)
                self.fm.rename(file_path, new_file_path)
                self.__add_metadata(metadata, title)
                self.__add_content(content, title)

    def makedirs(self):
        self.fm.makedirs(self.fm.join(self.datalake_dir, self.metadata_dir))
        self.fm.makedirs(self.fm.join(self.datalake_dir, self.content_dir))

    def __metadata_content_divider(self, lines):
        for idx, line in enumerate(lines):
            if line.startswith('***'):
                metadata = lines[:idx]
                content = lines[idx+1:]
            if line.startswith('Title: '):
                title = line[len('Title: '):].strip()
        return metadata, content, title
    
    def __sanitize_file_name(self, file_name):
        invalid_chars = '\\/:*?"<>|'
        for char in invalid_chars:
            file_name = file_name.replace(char, '-')
        file_name = file_name.strip().rstrip('.')
        return file_name

    def __add_metadata(self, metadata, file_name):
        metadata_file_path = self.fm.join(self.datalake_dir ,self.metadata_dir, file_name)
        self.__writter(metadata_file_path, metadata)

    def __add_content(self, content, file_name):
        content_file_path = self.fm.join(self.datalake_dir, self.content_dir, file_name)
        self.__writter(content_file_path, content)

    def __writter(self, file_path, lines):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(lines))