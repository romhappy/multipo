import random
import tkinter as tk
import tkinter.messagebox as messagebox

def generate_multiplication():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    result = num1 * num2
    multiplication = str(num1) + " X " + str(num2)+" ="
    label.config(text=multiplication)
    root.update()
    return result, multiplication


def show_multiplications():
    def show_next_multiplication():
        result, multiplication = generate_multiplication()
        multiplication_list.append(multiplication)
        show_result(result, multiplication)
        if len(multiplication_list) < 10:
            root.after(1000, show_next_multiplication)
        
    show_next_multiplication()


def show_result(result, multiplication):
    result_list.append(result)
    if len(result_list) == 10:
        print_results()


def print_results():
    print("Multiplication\tResult")
    for multiplication, result in zip(multiplication_list, result_list):
        print(f"{multiplication}\t\t{result}")

def print_results():
    results = []
    for multiplication, result in zip(multiplication_list, result_list):
        results.append(f"{multiplication}\t\t{result}")
    result_str = "\n".join(results)

    # Create a new top-level window for the message box
    msg_box = tk.Toplevel(root)
    msg_box.title("Résultats")
    msg_box.attributes('-fullscreen', True)
    msg_box.geometry("800x600")

    # Create a label widget to display the results
    label = tk.Label(msg_box, text=result_str, font=("Arial", 40), justify="left")
    label.pack(pady=20, padx=10)

    # Add a button to close the message box
    button = tk.Button(msg_box, text="Close", command=msg_box.destroy)
    button.pack(pady=10)

root = tk.Tk()
root.title("Multiplication Generator")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

label = tk.Label(root, font=("Arial", 100))
label.pack(pady=20)

button = tk.Button(root, text="C'est parti pour les multiplication!", command=show_multiplications)
button.pack(pady=10)

multiplication_list = []
result_list = []

root.mainloop()
