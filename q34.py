# You are designing a simple logging system in Python. Implement a Logger class that has a method log(message) to print messages to the console. Additionally, create two different classes FileWriter and DatabaseWriter. Both should implement a write(data) method. Implement a function write_data(writer, data) that accepts an instance of FileWriter or DatabaseWriter and calls its write(data) method to demonstrate duck typing.


class Logger:
    def log(self, message):
        self.message = message


class FileWriter:
    def write(self, data):
        self.data = data
        print(f"Writing to file: {self.data}")


class DatabaseWriter:
    def write(self, data):
        self.data = data
        print(f"Writing to database: {self.data}")


def write_data(writer, data):
    writer.write(data)


f = FileWriter()
d = DatabaseWriter()
# The write_data function does not explicitly check the type of writer. It relies on the presence of the write(data) method
write_data(f, "ABCCC")
write_data(d, "XCCC")
