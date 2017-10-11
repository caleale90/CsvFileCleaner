import os
import re
import sys
from shutil import copyfile


def write_to_file(file, text):
    file_to_write = open(file, "a")
    file_to_write.write(text + "\n")


class CsvFileCleaner:
    def __init__(self, file_to_process, separator):
        self.file_to_process = file_to_process
        self.separator = separator
        self.tmp_file = "/tmp/tmp_text_file.txt"
        if os.path.exists(self.tmp_file):
            os.remove(self.tmp_file)

    def process(self):
        file_to_process = open(self.file_to_process, 'r')
        for line in file_to_process.readlines():
            text_to_write = self.__clean(line)
            write_to_file(self.tmp_file, text_to_write)
        return copyfile(self.tmp_file, self.file_to_process)

    def __clean(self, text):
        result = ""
        for token in text.split(self.separator):
            token = token.lower().replace("\n","")
            text = re.sub('[^0-9a-zA-Z]+', ' ', token)
            result += text + self.separator
        return result[:-1]


def main():
    file_to_process = sys.argv[1]
    fc = CsvFileCleaner(file_to_process, '|')
    fc.process()


if __name__ == '__main__':
    main()
