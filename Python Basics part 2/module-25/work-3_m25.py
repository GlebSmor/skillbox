class MyDict(dict):
    def get(self, key, default_return=0):
        if key in self:
            return self[key]
        else:
            return default_return


new_dict = MyDict()
normal_dict = {}
print(new_dict.get('a'))
print(normal_dict.get('a'))
