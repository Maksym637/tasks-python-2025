class FileSystem:
    def __init__(self):
        self.file_system = {}

    def __parse_path(self, path: str) -> list[str]:
        return [p for p in path.split("/") if p]

    def __traverse(self, parts: list[str]) -> dict | None:
        current = self.file_system

        for p in parts:
            if p not in current or not isinstance(current[p], dict):
                return None
            current = current[p]

        return current

    def add_directory(self, path: str) -> bool:
        created = False

        parts = self.__parse_path(path)
        current = self.file_system

        for p in parts:
            if p not in current:
                current[p] = {}
                created = True
            elif not isinstance(current[p], dict):
                return False
            current = current[p]

        return created

    def add_file(self, path: str, content: str) -> bool:
        parts = self.__parse_path(path)

        if not parts:
            return False

        *dirs, file_name = parts
        current = self.__traverse(dirs) if dirs else self.file_system

        if current is None:
            return False

        if file_name in current:
            return False

        current[file_name] = content

        return True

    def get_content(self, path: str) -> str | None:
        parts = self.__parse_path(path)

        if not parts:
            return None

        *dirs, file_name = parts
        current = self.__traverse(dirs) if dirs else self.file_system

        if current is None:
            return None

        value = current.get(file_name)

        return value if isinstance(value, str) else None

    def delete(self, path: str) -> bool:
        parts = self.__parse_path(path)

        if not parts:
            return False

        *dirs, name = parts
        current = self.__traverse(dirs) if dirs else self.file_system

        if current is None or name not in current:
            return False

        del current[name]

        return True
