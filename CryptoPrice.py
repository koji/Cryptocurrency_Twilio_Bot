import cryptocompare


class Crypto():
    def __init__(self, crypto_symbol):
        self.crypto_symbol = crypto_symbol

    def get_crypto_price(self):
        result = cryptocompare.get_price(self.crypto_symbol, currency='USD')
        try:
            return float(result[self.crypto_symbol]['USD'])
        except TypeError as error:
            return 'There is not a coin pair for {}-USD.'.format(self.crypto_symbol)


def main():
    test = 'KOJI'
    cc = Crypto(test)

    val = cc.get_crypto_price()
    print(val)


if __name__ == '__main__':
    main()
