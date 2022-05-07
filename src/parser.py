import re


class Parser:
    def __init__(self):
        ...

    def parse_game_file_content(self, game_file_content: str) -> None:
        gfc = game_file_content.split('---')

        data = dict()

        data['Intro'] = gfc[0]

        for question in re.findall(r'^(\d+.*(\n^(\s\s+.*))*)', gfc[1], re.MULTILINE):
            key, text, answers = self.parse_question(question[0])

            data[key] = {
                'question': text,
                'answers': answers
            }

        return data

    def parse_question(self, question: str):
        q_lines = question.split('\n')

        answers = map(lambda string: string.strip(), q_lines[1:])

        answers = [
            self.parse_answer(ans) for ans in answers
        ]

        return re.findall(r'^(\d+)', q_lines[0])[0], re.sub(r'^(\d+\.\s)', '', q_lines[0]), answers

    def parse_answer(self, answer):
        ans = answer.strip()

        ans = ans.replace('-', '', 1).strip()

        text = re.findall(r'\[(.*)\]', ans)
        ref = re.findall(r'\((.*)\)', ans)

        return (text[0], ref[0])
