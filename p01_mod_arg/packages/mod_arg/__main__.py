import argparse
import inspect


def main(my_args):
    print(f'--- In {inspect.currentframe().f_code.co_name}')
    print(f'my_args: {my_args}')
    print(f'--- Exit {inspect.currentframe().f_code.co_name}')


if __name__ == '__main__':
    # Define input argument
    print(f'--- In {__file__}')
    parser = argparse.ArgumentParser(
            description='Show how to use argparse package.')
    parser.add_argument('cfg',nargs='?', help='the config file')
    parser.add_argument('-n','--name', type=str, help='input name')
    parser.add_argument('-m','--ismale', dest='ismale',
            action = 'store_true', help='default is not male')
    parser.add_argument('-a','--age', type=int, help='Input age')
    parser.add_argument('-l',
            choices=['0','1','2'], default='0',
            help='Input grade, default is 0')
    args = parser.parse_args()

    # call main
    main(args)
    print(f'--- Exit {__file__}\n')



