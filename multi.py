import random
import tkinter as tk
import tkinter.messagebox as messagebox
import time

root = tk.Tk()
root.title("Multipo")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

label_set_timer = tk.Label(root, text="Délai entre chaque multiplication (en sec.)", font=("Arial", 10))
label_set_timer.pack()
label_set_timer.place(x = 50, y = 50)

user_input = tk.Entry(root)
user_input.insert(0, "10")
user_input.pack()
user_input.place(x = 300, y = 50)

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
            root.after(int(user_input.get())*1000, show_next_multiplication)
        
    show_next_multiplication()


def show_result(result, multiplication):
    result_list.append(result)
    if len(result_list) == 10:
        time.sleep(int(user_input.get()))
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
    button = tk.Button(msg_box, text="Fermer", command=msg_box.destroy)
    button.pack(pady=10)

    
button = tk.Button(root, text="C'est parti pour les multiplications!", font=("Arial", 25), command=show_multiplications)
button.pack()
button.place(relx=0.5, rely=0.5, anchor="center")

label = tk.Label(root, font=("Arial", 200))
label.pack(pady=20)

# Create a user input to set timer

multiplication_list = []
result_list = []

root.mainloop()
