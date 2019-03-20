# Experiment: Is there a way to dynamically register classes so that when you add new class in the mix, some registry
# will automatically pick up the change?

# Conclusion: Yes!


class Registry(object):
    entries = set()

    def print_entries(self):
        print(self.entries)


def register(class_):
    def wrapper():
        for entry in class_.entries:
            Registry.entries.add(entry)
        return class_

    return wrapper()


@register
class SpanishBinary(object):
    entries = {'uno', 'dos', 'quatro'}


class SpanishTres(object):
    entries = {'tres'}


@register
class EnglishBinary(object):
    entries = {'one', 'two', 'four'}


class EnglishThree(object):
    entries = {'three'}


if __name__ == '__main__':
    expected_entries = {
        'uno',
        'dos',
        'quatro',
        'one',
        'two',
        'four'
    }

    registry = Registry()
    registry.print_entries()

    assert expected_entries == registry.entries
