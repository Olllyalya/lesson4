from lesson_4.website_alive import make_request


url_name = input("Enter URL")

def response(addres):
    answer = make_request.get_response(addres)
    if answer == 200:
        print("True")
    else:
        False

response(url_name)
