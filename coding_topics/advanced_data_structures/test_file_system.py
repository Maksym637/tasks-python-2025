import unittest

from file_system import FileSystem


class FileSystemTests(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test1(self):
        self.assertTrue(self.fs.add_directory("/dirA"))
        self.assertTrue(self.fs.add_file("/dirA/file1.txt", "Hello, World!"))
        self.assertEqual(self.fs.get_content("/dirA/file1.txt"), "Hello, World!")

    def test2(self):
        self.assertTrue(self.fs.add_directory("/dirB"))
        self.assertFalse(self.fs.add_directory("/dirB"))
        self.assertTrue(self.fs.add_file("/dirB/file2.txt", "Content"))
        self.assertFalse(self.fs.add_file("/dirB/file2.txt", "New Content"))

    def test3(self):
        self.assertTrue(self.fs.add_directory("/dirC"))
        self.assertTrue(self.fs.add_file("/dirC/file3.txt", "Important Data"))
        self.assertTrue(self.fs.delete("/dirC/file3.txt"))
        self.assertIsNone(self.fs.get_content("/dirC/file3.txt"))

    def test4(self):
        self.assertTrue(self.fs.add_directory("/dirD"))
        self.assertTrue(self.fs.add_directory("/dirD/subdir1"))
        self.assertTrue(self.fs.add_file("/dirD/subdir1/file4.txt", "Nested File"))
        self.assertEqual(self.fs.get_content("/dirD/subdir1/file4.txt"), "Nested File")

    def test5(self):
        self.assertTrue(self.fs.add_directory("/dirE"))
        self.assertTrue(self.fs.add_directory("/dirE/subdir2"))
        self.assertTrue(self.fs.add_file("/dirE/subdir2/file5.txt", "Another File"))
        self.assertTrue(self.fs.delete("/dirE"))
        self.assertIsNone(self.fs.get_content("/dirE/subdir2/file5.txt"))

    def test6(self):
        self.assertFalse(self.fs.delete("/dirF/nonexistentfile.txt"))

    def test7(self):
        self.assertTrue(self.fs.add_directory("/dirG"))
        self.assertTrue(self.fs.add_directory("/dirG/subdir3"))
        self.assertTrue(self.fs.add_directory("/dirG/subdir3/subdir4"))
        self.assertTrue(
            self.fs.add_file("/dirG/subdir3/subdir4/file7.txt", "Deep Content")
        )
        self.assertEqual(
            self.fs.get_content("/dirG/subdir3/subdir4/file7.txt"), "Deep Content"
        )

    def test8(self):
        self.assertTrue(self.fs.add_directory("/dirH"))
        self.assertTrue(self.fs.add_directory("/dirH1"))
        self.assertTrue(self.fs.add_file("/dirH/file8.txt", "Similar Path"))
        self.assertEqual(self.fs.get_content("/dirH/file8.txt"), "Similar Path")

    def test9(self):
        self.assertTrue(self.fs.add_directory("/dirI"))
        self.assertTrue(self.fs.add_directory("/dirI/subdir5"))
        self.assertTrue(self.fs.add_directory("/dirI/subdir5/subdir6"))
        self.assertFalse(self.fs.add_directory("/dirI/subdir5"))
        self.assertTrue(self.fs.delete("/dirI/subdir5"))

    def test10(self):
        self.assertTrue(self.fs.add_directory("/dirJ"))
        self.assertTrue(self.fs.add_file("/dirJ/rootfile.txt", "Root File"))
        self.assertTrue(self.fs.add_directory("/dirJ/subdir7"))
        self.assertTrue(self.fs.add_file("/dirJ/subdir7/subfile.txt", "Sub File"))
        self.assertEqual(self.fs.get_content("/dirJ/rootfile.txt"), "Root File")
        self.assertTrue(self.fs.delete("/dirJ/rootfile.txt"))
        self.assertIsNone(self.fs.get_content("/dirJ/rootfile.txt"))


if __name__ == "__main__":
    unittest.main()
