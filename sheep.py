def main():
    n = int(input("What's the n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑"*(i+1)  # return one value one at a time

if __name__ == "__main__":
    main()