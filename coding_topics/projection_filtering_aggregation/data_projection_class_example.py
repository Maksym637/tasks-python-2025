class DataProjector:
    def __init__(self, data):
        self.data = data

    def project(self, func):
        return list(map(func, self.data))

    def filter_and_project(self, filter_func, project_func):
        filtered_data = filter(filter_func, self.data)
        return list(map(project_func, filtered_data))


if __name__ == "__main__":
    sentences = ["HELLO WORLD", "PYTHON IS FUN", "I LIKE PROGRAMMING"]
    projector = DataProjector(sentences)

    lower_filtered_sentences_list = projector.filter_and_project(
        lambda sentence: "PYTHON" in sentence,
        lambda sentence: sentence.lower(),
    )
    print(lower_filtered_sentences_list)
