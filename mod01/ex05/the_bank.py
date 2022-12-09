# in the_bank.py
class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
        
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    def __init__(self):
        self.account = []

    def add(self, account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(account, Account):
            return False
        if len([x for x in self.account if x.name == account.name]) > 0:
            return False
        self.account.append(account)
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        o = [x for x in self.account if x.name == origin]
        d = [x for x in self.account if x.name == dest]
        if len(o) != 1 or len(d) != 1:
            return False
        o, d = o[0], d[0]
        if not isinstance(o, Account) or not isinstance(d, Account):
            return False
        if not hasattr(o, 'value') or not hasattr(d, 'value'):
            return False
        if o.value < amount or amount < 0:
            return False
        d.transfer(amount)
        o.transfer(-amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        fix = [x for x in self.account if x.name == name]
        print(fix)
        if len(fix) != 1:
            return False
        fix = fix[0]
        valid_attrs = {
            "name" : None,
            "id"   : None,
            "value": 0
            }
        attrs = fix.__dict__.keys()
        tattrs = fix.__dict__.copy().keys()
        fix_attrs = {"name" : fix.name, "id" : fix.id, "value" : fix.value}
        for x in valid_attrs.keys():
            if x in attrs:
                valid_attrs[x] = fix_attrs[x]
        if 'id' not in attrs:
            valid_attrs['id'] = Account.ID_COUNT
            Account.ID_COUNT += 1
        elif not isinstance(valid_attrs['id'], int):
            valid_attrs['id'] = int(valid_attrs['id']) if isinstance(valid_attrs['id'], float) else 0
        if not (isinstance(valid_attrs['value'], int) or isinstance(valid_attrs['value'], float)):
                valid_attrs['value'] = 0
        for attr in tattrs:
            if attr.startswith('b'):
                delattr(fix, attr)
        if len([x for x in attrs if attr.startswith('zip')]) == 0:
            valid_attrs['zip'] = 42
        if len([x for x in attrs if attr.startswith('addr')]) == 0:
            valid_attrs['addr'] = 42           
        fix.__dict__.update(valid_attrs)
        attrs = fix.__dict__.keys()
        if len(attrs) % 2 == 0:
            for attr in attrs:
                if attr not in {'name', 'id', 'value'} and not attr.startswith('zip') and not attr.startswith('addr'):
                    delattr(fix, attr)
                    break
        return True
                
        
        
if __name__ == '__main__':
    b = Bank()
    a1 = Account("hola", value=42)
    a2 = Account("hola2", value=50)
    b.add(a1)
    b.add(a2)
    print(b.transfer('hola', 'hola', 42), a1.value)
    print(Account.ID_COUNT)
    print(b.fix_account('hola'))
