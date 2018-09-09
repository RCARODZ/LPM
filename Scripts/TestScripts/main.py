from inherit import *

def main():
    test = B(name="som", account="acc", length=10)
    test.display()
    test.someFunct()

if __name__ == '__main__':
    main()