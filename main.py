import base64
from consolemenu import SelectionMenu

def encode():
    text = input("Enter text to encode: ")
    encoded_text = base64.b64encode(text.encode('utf-8'))
    print(f"Encoded text: {encoded_text.decode('utf-8')}")
    input("Press Enter to return to the main menu.")

def decode():
    text = input("Enter text to decode: ")
    decoded_text = base64.b64decode(text.encode('utf-8'))
    print(f"Decoded text: {decoded_text.decode('utf-8')}")
    input("Press Enter to return to the main menu.")

menu_items = [
    "Encode",
    "Decode"
]

menu = SelectionMenu(menu_items, title="Select an option:")
while True:
    menu.show()

    menu_item = menu.selected_option
    if menu_item == 0:
        encode()
    elif menu_item == 1:
        decode()
    else:
        break
