# def phone_book_list():
#      with open("phone_book.txt", "r", encoding="utf8") as file:
#         phone_book_list = []
#         for data in phone_book_list():
#             data.append(data.split())
#             return phone_book_list



def add_contact(name, phone_number):
#    date =  data.split()
#    file = open("file.txt", "a", encoding="utf8")
#    file.write(data)
#    file.close()
    with open("phone_book.txt", "a", encoding="utf8") as file:
        file.write(f"{name}, {phone_number} \n")
        
    # return None

    if __name__== "__main__":
            add_contact(f" {name}, {phone_number} ")


def del_contact(data):
    with open("phone_book.txt", "a", encoding="utf8") as file:
        for data in file:
            data_del = " ".join(data) + "\n"
            file.write(f"{data_del} \n")
    if __name__== "__main__":
            del_contact(f" {data} ")

def find(data):
    with open("phone_book.txt", "r", encoding="utf8") as file:
        if data_find in file:
            data_find = " ".join(data) + "\n"
            file.write(f"{data_find} \n")
    if __name__== "__main__":
            find(f" {data} ")


def edit(data):
    with open("phone_book.txt", "w", encoding="utf8") as file:
        if data_edit in file:
            data_edit = " ".join(data) + "\n"
            file.write(f"{data_edit} \n")
    if __name__== "__main__":
            edit(f" {data} ")
