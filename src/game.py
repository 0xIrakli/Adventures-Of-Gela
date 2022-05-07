import re
from src.parser import Parser
from rich import print


class Game:
    # Current question key (the questions have keys instead of indicies)
    current_question = '1'

    def __init__(self, game_file_path: str):
        self.read_file(game_file_path)

        # Print the intro text at initialization
        print(self.data['Intro'])

    def read_file(self, game_file_path: str):
        with open(game_file_path, 'r') as game_file:
            game_file_content: str = game_file.read()

            # Create a parser object
            parser = Parser()
            # Parse the game file content
            self.data = parser.parse_game_file_content(game_file_content)

    def loop(self) -> bool:
        while 1:
            # Store the question object in a variable with a shorter name
            cq = self.data[self.current_question]

            # Store the answer tuples in a variable with a shorter name
            answers = cq['answers']

            # Collect all possible answers in an array for easy handling
            possible_answers = [ans[0] for ans in answers]

            # Print the question statement
            print(cq['question'])

            # If this question has no possible answers, end the loop
            if len(cq['answers']) == 0:
                break
            else:
                # Otherwise, print all the possible answers
                for i, answer in enumerate(possible_answers):
                    print(f' {str(i + 1).zfill(2).replace("0"," ")})   {answer}')

            # Prompt user until a valid answer is given
            while 1:
                ans = input("===> ")

                if ans.isnumeric():
                    if int(ans) > 0 and int(ans) <= len(possible_answers):
                        break

            ans = str(int(ans) - 1)

            self.current_question = answers[possible_answers.index(ans)][1]
