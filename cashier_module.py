class Transaction:

    def __init__(self):
        self.dict = {}
        self.keys = []
        self.customer = ''

    def add_data(self, name, qty, price):
        dict_container = {}
        self.keys.append(name)
        dict_container[name] = [qty,price]
        self.dict.update(dict_container)

    def update_item_name(self, old_key, new_key):        
        index_selected = self.keys.index(old_key)
        self.keys[index_selected] = new_key
        dict_container = {}
        dict_container[new_key] = self.dict[old_key]
        self.dict.update(dict_container)
        del self.dict[old_key]

    def update_item_qty(self,key,new_qty):
        self.dict[key][0] = new_qty
        
    def update_item_price(self,key,new_price):
        self.dict[key][1] = new_price    

    def delete_data(self, key):
        if key in self.dict :
            del self.dict[key]
            self.keys.remove(key)

    def reset_transaction(self):
        self.dict = {}
        self.keys = []

    def total_price(self):
        total = 0
        total_pay = 0
        for key in self.keys :
            total += self.dict[key][0]*self.dict[key][1] 
        if total >= 500_000 :
            total_pay = total * 0.90
            disc = '10%'
        elif total >= 300_000 :
            total_pay = total * 0.92
            disc = '8%'
        elif total >= 200_000 :
            total_pay = total * 0.95
            disc = '5%'
        else :
            total_pay = total
        output = f'Anda perlu membayar sejumlah Rp. {total_pay} \n Terima kasih sudah belanja disini'
        if total >= 200_000 :        
            return f'Total belanja anda adalah Rp. {total}, anda mendapat diskon sebesar {disc}. \n {output}'                   
        else :
            return output

    def __str__(self):
        output = ','.join(f'{key} : {values}' for key, values in self.dict.items())
        return '{' + output + '}'
'''
x = Transaction()
x.add_data('name', 1, 2)
x.add_data('any', 2, 3)
print(x)
'''

