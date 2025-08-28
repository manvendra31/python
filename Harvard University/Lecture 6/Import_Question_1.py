from Question1 import square
def main():
    test_Square()


    
def test_Square():
    if square(2)!=4:
        print("2 square is not found in 4")
    if square(3)!=9:
        print("3 square is not found in 9")


if __name__=="__main__":

    main()
