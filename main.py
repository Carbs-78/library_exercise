# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # TODO this function needs updated


# convert files to list
def myFuncFile():
    # fileobj = open("zen.txt")
    # lines = []
    # for line in fileobj:
    #     lines.append(line.strip())
    # print(lines)
    # OR
    # fileobj = open("zen.txt")
    # lines = fileobj.readlines()
    # lines = [line.strip() for line in lines]
    # print(lines)

    # OR
    #     fileobj=open("zen.txt")
    #     lines=fileobj.read().split('\n')
    #     print(lines)

    # OR - using try catch
    fileobj = open("zen.txt")
    # iter() function is used for obtaining an iterator over the file reader
    it = iter(fileobj)
    lines = []
    while True:
        try:
            line = next(it)
            line = line.strip()
            lines.append(line)
        except StopIteration:
            break
    print(lines)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('aws restart')
    myFuncFile()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
