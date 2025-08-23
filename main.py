#import library
from tabulate import tabulate

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

class User:
    def __init__(self, username, current_plant, 
                 duration_plan):
        self.username = username
        self.current_plant = current_plant
        self.duration_plan = duration_plan
    

    def check_all_plan(self):
        title= 'PacFlix Plan List'
        all_plan= {
            'Basic Plan': [True, True, True, 
                           False, False, 1,
                           '3rd party Movie only',
                           120000],
            'Standard Plan': [True, True, True, 
                           True, False, 2,
                           'Basic Plan Content + Sports',
                           160000],
            'Premium Plan': [True, True, True, 
                           True, True, 4,
                           'Basic Plan + Standard Plan + PacFlix Original Series',
                           200000],
            'Services': ['Bisa Stream', 'Bisa Download', 'Kualitas SD', 
                           'Kualitas HD', 'Number of Devices',
                           '3rd party Movie only',
                           'Jenis Konten', 'Harga']
        }

        tabel= tabulate(all_plan, headers= "keys")
        
        return title+'\n\n'+tabel
    

    def check_plan(self):
        pass

    
    def upgrade_plan(self):
        pass


    def pick_plan(self):
        pass


user_1= User("Shandy", 12, "Basic Plan")
print(user_1.check_all_plan())

