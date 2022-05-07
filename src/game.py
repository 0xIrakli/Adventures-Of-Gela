import re
from src.parser import Parser
from rich import print


class Game:
    current_question = '1'

    def __init__(self, game_file_path: str):
        self.read_file(game_file_path)

        print(self.data['Intro'])

    def read_file(self, game_file_path: str):
        with open(game_file_path, 'r') as game_file:
            game_file_content: str = game_file.read()

            parser = Parser()
            self.data = parser.parse_game_file_content(game_file_content)

    def loop(self) -> bool:
        while 1:
            answers = self.data[self.current_question]['answers']

            possible_answers = [ans[0]
                                for ans in answers]

            print(self.data[self.current_question]['question'])

            if len(self.data[self.current_question]['answers']) == 0:
                break
            else:
                for i, answer in enumerate(possible_answers):
                    print(f'{str(i + 1).zfill(2).replace("0"," ")})   {answer}')

            while 1:
                ans = input("===> ")

                if ans.isnumeric():
                    if int(ans) > 0 and int(ans) <= len(possible_answers):
                        break

            ans = str(int(ans) - 1)

            self.current_question = answers[possible_answers.index(
                ans)][1]
