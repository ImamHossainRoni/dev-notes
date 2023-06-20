"""
    Higher order function:
                        1. accepts a function as an argument
                        2. returns a function(In python, functions are also treated as an objects)
"""


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def voice(func):
    voice_context = func("Hello...what's up?")
    return voice_context


print(voice(loud))
print(voice(quiet))

