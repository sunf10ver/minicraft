import requests
import base64
import json
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication,QButtonGroup, QTextEdit, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QMessageBox, QRadioButton, QGroupBox
from PyQt5.QtGui import QTextCursor


class LLMQuery(QThread):
    stream_chank = pyqtSignal(str)
    result_ready = pyqtSignal(str)
    def __init__(self, question):
        super().__init__()
        self.question = question
    def run(self):
        self.query_llm()
    def query_llm(self):
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": "Bearer ",  # Replace with your actual API key
            "Content-Type": "application/json"
        }

        # Define the request payload
        payload = {
            "model": "sonar-pro",
            "messages": [
                {"role": "user", "content": self.question}
            ],
            'stream': True
        }

        with requests.post(url, headers=headers, json=payload, stream=True, timeout=30) as response:
            print(payload)
            full_answer = ''
            for line in response.iter_lines():
                if line:
                    decode_line = line.decode('utf_8')
                    if decode_line.startswith('data:'):
                        data_str = decode_line[6:]
                        if data_str == "[DONE]":
                            break
                        try:
                            data_json = json.loads(data_str)
                            delta = data_json.get("choices", [{}])[0].get("delta", {}).get("content", "")
                            if delta:
                                print(delta)
                                full_answer += delta
                                self.stream_chank.emit(delta)
                        except json.JSONDecodeError: 
                            continue
            self.result_ready.emit(full_answer)

    
class LLMWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(700, 400)
        self.setWindowTitle('Query LLM')

        main_col = QVBoxLayout()

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Введите ваш вопрос...")
        self.input_text.setMaximumHeight(100)

        bt = QPushButton('Отправить')
        bt.clicked.connect(self.llm_question)

        self.ans = QTextEdit()
        self.ans.setReadOnly(True)
        self.ans.setPlaceholderText('здесь ответ от ЛЛМ')

        main_col.addWidget(QLabel('Ваш вопрос'))
        main_col.addWidget(self.input_text)
        main_col.addWidget(bt)
        main_col.addWidget(QLabel('Ответ'))
        main_col.addWidget(self.ans)
        self.setLayout(main_col)

    def llm_question(self):
        print('work')
        question = self.input_text.toPlainText().strip()
        self.ans.clear()
        self.worker = LLMQuery(question)
        print('work1')
        self.worker.stream_chank.connect(self.on_stream_chank)
        print('work2')
        self.worker.start()

    def on_stream_chank(self, chank):
        self.ans.insertPlainText(chank)
        self.ans.moveCursor(QTextCursor.End)

app = QApplication([])
main_win = LLMWidget()

main_win.show()
app.exec_()