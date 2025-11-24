import sys
def add(a,b):
    return a + b
if __name__ == "__main__":
    x=(sys.argv[1])
    y=(sys.argv[2])
    print("sum:", add(x, y))
