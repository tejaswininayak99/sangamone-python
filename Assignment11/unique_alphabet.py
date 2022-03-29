
def sorted_words_file(fileName):

    f=open("uni.txt", 'r')
    a=f.read()
    f.close()
    word=a.split()
    word_s = sorted(list(set(word)))
    print("Aphabetical order are:",word_s)
def main():  
    fileName = input("Enter the file name: ")
    sorted_words_file(fileName)

if __name__ == "__main__":
    main()
