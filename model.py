def add_contact(name, phone_number):
    with open("phone_book.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}, {phone_number} \n")

    if __name__== "__main__":
        add_contact(f" {name}, {phone_number} \n")

def del_contact(data):    
    with open("phone_book.txt", encoding="utf-8") as file:
        del_cotnact = file.readlines()
    del del_cotnact[0]
    with open("phone_book.txt", "w", encoding="utf-8") as file:
        file.writelines(del_cotnact)
  

# def del_contact(data):
#     with open("phone_book.txt", encoding="utf-8") as file:
#         data = file.read().split("\n")
#         data = data[1]
#     with open("phone_book.txt", "w", encoding="utf-8") as file:
#             data = "\n".join(data)
#             file.write(f"{data} \n")
#     if __name__== "__main__":
#             del_contact(f" {data} \n")

def find(data):
    with open("phone_book.txt", "r", encoding="utf8") as file:
        if data_find in file:
            data_find = " ".join(data) + "\n"
            # file.write(f"{data_find} \n")
    # if __name__== "__main__":
            # find(f" {data} ")


def edit(data):
    with open("phone_book.txt", "w", encoding="utf8") as file:
        if data_edit in file:
            data_edit = " ".join(data) + "\n"
            file.write(f"{data_edit} \n")
    # if __name__== "__main__":
            edit(f" {data} ")

# def error(data):
#     with open("phone_book.txt", "r", encoding="utf8") as file:
#         if data not in file:
#             return None