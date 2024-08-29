class WordsFinder:
    def __init__(self, *args):
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}
        for i in range(len(self.file_names)):
            name = self.file_names[i]
            with open(name, encoding='utf-8') as file:
                file_info = file.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file_info = file_info.replace(sym, '')
                all_words[name] = file_info.split()
        return all_words

    def find(self, word):
        find_res = {}
        for i in range(len(self.file_names)):
            if word.casefold() not in self.get_all_words()[self.file_names[i]]:
                continue
            else:
                find_res[self.file_names[i]] = self.get_all_words()[self.file_names[i]].index(word.casefold()) + 1
        return find_res

    def count(self, word):
        count_res = {}
        for i in range(len(self.file_names)):
            count_res[self.file_names[i]] = self.get_all_words()[self.file_names[i]].count(word.casefold())
        return count_res



