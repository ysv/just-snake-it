


def sing_blank_line():
    print('single!')

class SingleBlank:
    pass


def two_blank():
    print('single!')


class TwoBlank:
    pass


def nested_two_blank():


    a = 1
    print(a)

def top_level_def():
    def nested_level_def():
        pass
    return nested_level_def()

class TopLevelClass:
    class NestedLevelClass:
        def nested_nested_level_def(self):
            def nested_nested_nested_level_def():
                pass
