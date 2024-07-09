# Create a function identify_file_type that takes a file name as input and returns the type of the file based on its extension: ".txt" files: "Text File"
# Use match case to implement this function.


def identify_file_type(file_name: str) -> str:
    new_list = file_name.split(".", 1)
    file_exten = new_list[-1]
    match file_exten:
        case "txt":
            return "Text File"
        case "csv":
            return "CSV File"
        case "png":
            return "Image File"
        case _:  #  Any other file types
            return "Unknown File"


if __name__ == "__main__":
    print(identify_file_type("main.py"))
    print(identify_file_type("main.txt"))
    print(identify_file_type("main.png"))
    print(identify_file_type("main.csv"))
