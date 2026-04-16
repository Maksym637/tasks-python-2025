from collections import deque


class TextEditor:
    def __init__(self):
        # Last In, First Out (LIFO)
        self.stack = []
        # First In, First Out (FIFO)
        self.queue = deque([])

    def make_change(self, action):
        self.stack.append(action)

    def undo_change(self):
        if len(self.stack) == 0:
            return "No changes to undo!"

        return self.stack.pop()

    def add_to_print(self, doc):
        self.queue.append(doc)

    def print_doc(self):
        if len(self.queue) == 0:
            return "No documents in print queue!"

        return self.queue.popleft()


if __name__ == "__main__":
    editor = TextEditor()

    editor.make_change("Changed font size")
    editor.make_change("Inserted image")

    print("Undo: ", editor.undo_change())

    editor.add_to_print("Proposal.docx")
    editor.add_to_print("Report.xlsx")

    print("Print: ", editor.print_doc())
