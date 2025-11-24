from PySide6 import QtWidgets
from agent import crew


class HackIaMockup(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initBody()
        self.initUserInput()
        self.initPushButton()
        self.initCrewAnswer()

    def initBody(self) -> None:
        self.body = QtWidgets.QVBoxLayout(self)

    def initUserInput(self) -> None:
        self.user_input = QtWidgets.QPlainTextEdit(
            self, placeholderText="Escreva sua mensagem aqui..."
        )
        self.input = ""
        # Gera um menu de botão direito.
        _ = self.user_input.createStandardContextMenu()
        self.body.addWidget(self.user_input)

    def initPushButton(self) -> None:
        push_button = QtWidgets.QPushButton("Send")
        _ = push_button.clicked.connect(self.pushButtonSend)
        self.body.addWidget(push_button)

    def initCrewAnswer(self) -> None:
        self.crew_answer = QtWidgets.QTextEdit(readOnly=True)
        self.body.addWidget(self.crew_answer)

    def setCrewAnswer(self, answer: str) -> None:
        self.crew_answer.setMarkdown(answer)

    def clearCrewAnswer(self):
        self.crew_answer.clear()

    def pushButtonSend(self) -> None:
        self.input = self.user_input.toPlainText()
        self.user_input.clear()
        self.user_input.setReadOnly(True)
        crew_answer = crew.kickoff(inputs={"input": self.input})
        self.setCrewAnswer(crew_answer.final_output)
        self.user_input.setReadOnly(False)
