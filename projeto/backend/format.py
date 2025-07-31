
class FormatedString:

    def __init__(self, text):
        self.text = text

def format_output(response: str) -> FormatedString:
    formatted_output = response.replace("\n", "<br />")
    formatted_output = f"<div>{formatted_output}</div>"

    return FormatedString(text=formatted_output)
