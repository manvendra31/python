from Question1 import square
def main():
    test_Square()


    
def test_Square():
    try:
        assert square(2)==4
    except AssertionError:
        print("The square of 2 is 4 not found")
    try:        
        assert square(3)==9
    except AssertionError:
        print("The square of 3 is not found 9")

if __name__=="__main__":

    main()
