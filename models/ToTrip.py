from queue import Queue

from models.Trip import Trip


class Converter:
    def __init__(self, patterns):
        self.patterns = patterns
        self.trip = Trip()

    def converter(self):
        for pattern in self.patterns:
                self.add(pattern)
        return self.trip

    def add(self, symbols_G):
        symbols = symbols_G.lower()
        actual_element = self.trip
        for symbol in symbols:
            found = False
            for i in actual_element.urls:
                if i.param == symbol:
                    actual_element = i
                    found = True
                    break
            if not found:
                new_trip = Trip(symbol, actual_element)
                actual_element.urls.append(new_trip)
                actual_element = new_trip
        actual_element.words = True

    def find(self, prefix):
        prefix = prefix.lower()
        actual = self.trip
        curr_str = ''
        for symbol in prefix:
            find = False
            for i in actual.urls:
                if i.param == symbol:
                    find = True
                    curr_str += f'{i.param}'
                    actual = i
                    break
            if not find:
                return False
        if actual.words:
            return True
        else:
            return False

    def find_prefix(self, trip, prefix):
        prefix = prefix.lower()
        result = []
        curr_str = ''
        actual = trip

        for symbol in prefix:
            find = False
            for i in actual.urls:
                if i.param == symbol:
                    find = True
                    curr_str += f'{i.param}'
                    actual = i
            if not find:
                return None
            else:
                if actual.words:
                    result.append(prefix)

        ending = self.Searcher(actual)

        cur = ''
        while ending:
            last = ending.pop()
            while last.parent is not None:
                cur = f'{last.param}{cur}'
                last = last.parent
            result.append(cur)
            cur = ''
        return result




    def Searcher(self, trip ):
        curr = trip
        result = set()
        for url in curr.urls:
            if url.urls is None or url.words is True:
                result.add(url)
            cur = self.Searcher(url)
            if cur is not []:
                for i in cur:
                    result.add(i)

        return result



