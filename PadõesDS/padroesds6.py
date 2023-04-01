class Editor:
    def __init__(self):
        self.lines = []

    def insertLine(self, lineNumber, text):
        if lineNumber <= len(self.lines):
            self.lines.insert(lineNumber-1, text)
        else:
            self.lines.append(text)

    def removeLine(self, lineNumber):
        del self.lines[lineNumber-1]
        
class TextEditor(Editor):
    def open(self):
        while True:
            line = input()
            if line == "EOF":
                break
            self.insertLine(len(self.lines) + 1, line)
        self.notify("save")
        
class FileSaver:
    def __init__(self, filename):
        self.filename = filename

    def update(self, event, editor):
        if event == "save":
            with open(self.filename, "w") as f:
                f.write("\n".join(editor.lines))
                print("Conteúdo salvo no arquivo!")
                
class Observer:
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notify(self, event, editor=None):
        for observer in self.observers:
            observer.update(event, editor)
            
editor = TextEditor()
observer = Observer()
observer.addObserver(FileSaver("texto.txt"))
editor.addObserver(observer)

editor.open()