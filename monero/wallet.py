from . import address
from . import prio
from . import account

class Wallet(object):
    accounts = None

    def __init__(self, backend):
        self._backend = backend
        self.refresh()

    def refresh(self):
        self.accounts = self.accounts or []
        idx = 0
        for _acc in self._backend.get_accounts():
            try:
                if self.accounts[idx]:
                    continue
            except IndexError:
                pass
            self.accounts.append(_acc)
            idx += 1

    # Following methods operate on default account (index=0)
    def get_balances(self):
        return self.accounts[0].get_balances()

    def get_balance(self, unlocked=False):
        return self.accounts[0].get_balance(unlocked=unlocked)

    def get_address(self, index=0):
        return self.accounts[0].get_addresses()[0]

    def get_payments_in(self):
        return self.accounts[0].get_payments_in()

    def get_payments_out(self):
        return self.accounts[0].get_payments_out()

    def transfer(self, address, amount, priority=prio.NORMAL, mixin=5, unlock_time=0):
        return self.accounts[0].transfer(
                address,
                amount,
                priority=priority,
                mixin=mixin,
                unlock_time=unlock_time)

    def transfer_multiple(self, destinations, priority=prio.NORMAL, mixin=5, unlock_time=0):
        """
        destinations = [(address, amount), ...]
        """
        return self.accounts[0].transfer_multiple(
                destinations,
                priority=priority,
                mixin=mixin,
                unlock_time=unlock_time)
