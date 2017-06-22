from subprocess import check_output

class BitcoinWallet():
    def __init__(self):
        # Bitcoind should already be started
        # Otherwise exception will be raised
        tmp_address = check_output(['bitcoin-cli', 'getnewaddress'])

    def get_private_key(self, address):
        """Get private key for address with bitcoin-cli"""
        private_key = check_output(['bitcoin-cli', 'dumpprivkey', address])
        private_key = private_key.rstrip() # Remove end line symbol

        return private_key.decode('utf-8')

    def get_address(self):
        """Generate new address with bitcoin-cli"""
        address = check_output(['bitcoin-cli', 'getnewaddress'])
        address = address.rstrip() # Remove end line symbol

        return address.decode('utf-8')
