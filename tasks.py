import utils

def generate_100_sums():
    for i in range(100):
        print utils.add(i, i+1)

if __name__ == '__main__':
    generate_100_sums()
