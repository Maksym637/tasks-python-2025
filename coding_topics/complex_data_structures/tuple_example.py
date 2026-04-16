class TupleExample:
    def create_tuples(self):
        packed_tuple = ("apple", "banana", "cherry")
        signleton_tuple = ("apple",)
        from_list = tuple(["apple", "banana", "cherry"])
        return packed_tuple, signleton_tuple, from_list


if __name__ == "__main__":
    tuple_example = TupleExample()
    print(tuple_example.create_tuples())
