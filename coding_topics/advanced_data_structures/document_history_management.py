class DocumentHistory:
    def __init__(self):
        self.changes_stack = []
        self.redo_stack = []

    def apply_change(self, change: str) -> None:
        self.changes_stack.append(change)
        self.redo_stack.clear()

    def undo(self) -> str | None:
        if not self.changes_stack:
            return None
        change = self.changes_stack.pop()
        self.redo_stack.append(change)
        return change

    def redo(self) -> str | None:
        if not self.redo_stack:
            return None
        change = self.redo_stack.pop()
        self.changes_stack.append(change)
        return change

    def get_changes(self) -> list[str]:
        return self.changes_stack[:]


if __name__ == "__main__":
    doc_hist = DocumentHistory()

    doc_hist.apply_change("Added header")
    doc_hist.apply_change("Added footer")
    print(doc_hist.get_changes())

    print(doc_hist.undo())
    print(doc_hist.get_changes())

    print(doc_hist.redo())
    print(doc_hist.get_changes())

    print(doc_hist.undo())
    print(doc_hist.undo())
    print(doc_hist.get_changes())

    print(doc_hist.undo())

    print(doc_hist.redo())
    print(doc_hist.redo())
    print(doc_hist.get_changes())

    print(doc_hist.redo())
