#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint, shuffle
class Question():
    def __init__(self, question, right_ans, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.right_ans = right_ans
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3

question_list = []
question_list.append(Question('Как на английском будет корова?', 'cow', 'dog', 'horse', 'whale'))
question_list.append(Question('На каком языке разговаривают в Мексике?', 'на испанском', 'на мексиканском', 'на итальянском', 'на японском'))
question_list.append(Question('На каком языке говорит больше всего людей на Земле?', 'китайский', 'русский','английский', 'арабский'))
question_list.append(Question('Сколько сердец у осьминога?', 'три', 'одно', 'четыре', 'два'))
question_list.append(Question('Какая планета в нашей Солнечной системе самая большая?', 'Юпитер', 'Марс', 'Земля', 'Нептун'))
question_list.append(Question('Какой океан самый большой на Земле?', 'Тихий', 'Атлантический', 'Индийский', 'Северный Ледовитый'))
question_list.append(Question('Какая река самая длинная в мире?', 'Амазонка', 'Нил', 'Конго', 'Лена'))
question_list.append(Question('Сколько дней в феврале в високосный год?', 'Двадцать девять', 'Двадцать восемь', 'Тридцать один', 'Тридцать'))
question_list.append(Question('Кто основал Microsoft?', 'Билл Гейтс', 'Марк Цукерберг', 'Стив Джобс', 'Билл Хейдер'))
question_list.append(Question('Как называется компания, выпустившая видеоигру Mario Kart?', 'Nintendo', 'Xbox', 'Playstation', 'Microsoft'))
question_list.append(Question('Какое животное можно увидеть на логотипе Porsche?', 'Конь', 'Бык', 'Ягуар', 'Олень'))
question_list.append(Question('Какой напиток потребляют больше всего в мире?', 'Кофе', 'Чай', 'Пиво', 'Вино'))
question_list.append(Question('Какое самое громкое животное на Земле?', 'Синий кит', 'Цикада', 'Бегемот', 'Человек'))


app = QApplication([])
win = QWidget()

question = QLabel('Вопрос')
button = QPushButton('Ответить')
groupBox = QGroupBox('Варианты ответов')
answer_var1 = QRadioButton('Вариант 1')
answer_var2 = QRadioButton('Вариант 2')
answer_var3 = QRadioButton('Вариант 3')
answer_var4 = QRadioButton('Вариант 4')

radioGroup = QButtonGroup()
radioGroup.addButton(answer_var1)
radioGroup.addButton(answer_var2)
radioGroup.addButton(answer_var3)
radioGroup.addButton(answer_var4)

ansGroupBox = QGroupBox('Результаты теста')
result = QLabel('Верно,неверно')
correct = QLabel('Правильный ответ')

ansLayout = QVBoxLayout()
ansLayout.addWidget(result, alignment = (Qt.AlignLeft | Qt.AlignTop))
ansLayout.addWidget(correct, alignment = Qt.AlignHCenter)
ansGroupBox.setLayout(ansLayout)

boxLayout = QHBoxLayout()
boxLayout1 = QVBoxLayout()
boxLayout2 = QVBoxLayout()
boxLayout1.addWidget(answer_var1)
boxLayout1.addWidget(answer_var2)
boxLayout2.addWidget(answer_var3)
boxLayout2.addWidget(answer_var4)
boxLayout.addLayout(boxLayout1)
boxLayout.addLayout(boxLayout2)
groupBox.setLayout(boxLayout)

mainLayout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout1.addWidget(question, alignment = Qt.AlignCenter)
layout2.addWidget(groupBox)
layout2.addWidget(ansGroupBox)
ansGroupBox.hide()
layout3.addWidget(button, stretch = 2)
mainLayout.addLayout(layout1, stretch = 2)
mainLayout.addLayout(layout2, stretch = 8)
mainLayout.addLayout(layout3, stretch = 1)
win.setLayout(mainLayout)

def show_result():
    groupBox.hide()
    ansGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    ansGroupBox.hide()
    groupBox.show()
    button.setText('Ответить')
    radioGroup.setExclusive(False)
    answer_var1.setChecked(False)
    answer_var2.setChecked(False)
    answer_var3.setChecked(False)
    answer_var4.setChecked(False)
    radioGroup.setExclusive(True)

answers = [answer_var1, answer_var2, answer_var3, answer_var4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong_ans1)
    answers[2].setText(q.wrong_ans2)
    answers[3].setText(q.wrong_ans3)
    question.setText(q.question)
    correct.setText(q.right_ans)
    show_question()

def check_answer():
    if answers[0].isChecked():
        result.setText('Правильно!')
        show_result()
        win.score += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        result.setText('Неверно!')
        show_result()
    print('Всего вопросов:', win.total, '\n-Всего правильных ответов:', win.score)

def next_question():
    win.total += 1
    print('Всего вопросов:', win.total, '\n-Всего правильных ответов:', win.score)

    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_ans():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

win.score = 0
win.total = 0
button.clicked.connect(click_ans)
next_question()
win.setWindowTitle('Memory card')
win.resize(600,300)
win.show()
app.exec()