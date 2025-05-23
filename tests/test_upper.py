from upper_py import make_uppercase

def test_upper_is_working():

    word = "hello world"
   
    assert make_uppercase(word) == word.upper()