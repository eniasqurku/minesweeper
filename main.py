from client import Client


def play():
    dimension = int(input('Supply the dimension: '))
    client = Client(dimension=dimension)

    while not client.is_cleared():
        print(client)
        coordinates = input('Supply the coordinates (seperated by comma):').split(',')
        x, y = int(coordinates[0]), int(coordinates[1])
        result = client.check(x, y)
        if result == -1:
            print('Boom')
            print(client.m)
            break

    if client.is_cleared():
        print('You Won')


if __name__ == '__main__':
    play()
