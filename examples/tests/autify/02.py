from collections import Counter

def featuredProduct(products):
    counter = Counter(products)
    count = 0
    ans = []

    for key, value in counter.items():
        if value > count:
            count = value
            ans = []
            ans.append(key)
        elif value == count:
            ans.append(key)

    return sorted(ans)[-1]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    products_count = int(input().strip())

    products = []

    for _ in range(products_count):
        products_item = input()
        products.append(products_item)

    result = featuredProduct(products)
    print(result)

    # fptr.write(result + '\n')
    #
    # fptr.close()
