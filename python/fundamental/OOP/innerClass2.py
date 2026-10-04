class JavaScript:
    def __init__(self,author):
        self.author = author
    def show(self):
        print("Js created by "+self.author)

    class Vue:
        def __init__(self):
            self.author = "Evan You"
        def show(self):
            print("Vue is created by "+self.author)

js = JavaScript("Brendan Eich")
js.show()
vue = JavaScript.Vue()
vue.show()