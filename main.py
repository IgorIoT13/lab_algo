from models.ToTrip import Converter

test_patterns = [
    "afafaf",
    "afafa",
    "afafZ",
    "af1111",
    "Test",
    "test",
    "lab-5",
    "lab_6",
    "end"
]

test = Converter(test_patterns)
test.add("bsfaafa")
print(test.find_prefix(test.converter(), "af"))
print(test.find('lab_6'))




