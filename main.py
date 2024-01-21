import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")

        self.question_number = 0
        self.score = 0

        self.questions = [
            {
                'question': '1- What is the capital of France?',
                'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
                'correct_option': 'Paris'
            },
            {
                'question': '2- Which planet is known as the Red Planet?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Venus'],
                'correct_option': 'Mars'
            },
            {
                'question': '3- What is the largest mammal?',
                'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
                'correct_option': 'Blue Whale'
            }
            # Add more questions as needed
        ]

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", font=('Helvetica', 20,'bold'),fg='#5e17eb',bg='#FFEEEF')
        self.question_label.place(x=60, y=220)

        self.var_option = tk.StringVar()

        self.option_buttons = []

        for i in range(4):
            #option_button = tk.Radiobutton(self.master, text="", variable=self.var_option, value="")
            option_button = tk.Radiobutton(self.master, text="", variable=self.var_option, value="",
                                           command=self.check_answer,bg='#FFEEEF',font=('Helvetica', 14,'bold'))

            option_button.place(x=180, y=270 + i * 40)
            self.option_buttons.append(option_button)

        self.next_button = tk.Button(self.master, text="Next", height='1',width=17,
           bg='#F92592',fg='white',font='Calibri 15 bold',bd=0, command=self.next_question)
        self.next_button.place(x=180, y=450)

        self.load_question()

    def load_question(self):
        if self.question_number < len(self.questions):
            question_data = self.questions[self.question_number]
            self.question_label.config(text=question_data['question'])

            for i, option in enumerate(question_data['options']):
                self.option_buttons[i].config(text=option, value=option)

            self.var_option.set(None)
        else:
            messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(self.questions)}")
            self.master.destroy()

    def check_answer(self):
        selected_option = self.var_option.get()
        correct_option = self.questions[self.question_number]['correct_option']

        if selected_option == correct_option:
            self.score += 1

    def next_question(self):
        self.question_number += 1
        self.load_question()

def main():
    root = tk.Tk()
    app = QuizApp(root)

    #root.title("Pomodoro Timer")
    root.geometry('700x600')
    root.config(bg='#FFEEEF')
    root.resizable(False, False)

    logo = tk.PhotoImage(file='logo.png')
    tk.Label(root, image=logo, bg='#FFEEEF') \
        .place(x=185, y=-6)


    root.mainloop()

if __name__ == "__main__":
    main()
