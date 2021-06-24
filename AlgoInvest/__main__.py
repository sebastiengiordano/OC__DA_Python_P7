from AlgoInvest.brutal_force.brutal_force import brutal_force
from time import time

if __name__ == '__main__':
    start = int(time())
    brutal_force()
    print(f"\n\tAlgo duration: {int(time()) - start}s")