# def shout(text):
#     return text.upper()
# print(shout("aanya"))
# yell=shout
# print(yell("aanya"))
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greeting(func):
    greet=func("hi,this is python prigram to pass function as a argument.")
    print(greet)
greeting(shout)
greeting(whisper)

