#import library
from tabulate import tabulate

class User:
    def __init__(self, username, duration_plan, 
                 current_plan):
        self.data = {
            "Shandy": ["Basic Plan", 12, "shandy-2134"],
            "Cahya": ["Standard Plan", 24, "cahya-abcd"],
            "Ana": ["Premium Plan", 5, "ana-2f9g"],
            "Bagus": ["Basic Plan", 11, "bagus-9f92"]
        }
        
        self.username = username
        self.current_plan = current_plan
        self.duration_plan = duration_plan
        self.all_plan= {
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
    

    def convert_to_tabulate(self, data):
        return tabulate(data, headers= "keys")


    def check_all_plan(self):
        return 'PacFlix Plan List\n\n'+self.convert_to_tabulate(self.all_plan)
    

    def check_plan(self):
        plan_benefit= {}
        
        for plan in self.all_plan:
            if plan==self.current_plan or plan=="Services":
                plan_benefit.update({plan:self.all_plan.get(plan)})
        
        return self.current_plan+'\n\n'+str(self.duration_plan)+' Bulan\n\n'\
                +self.current_plan+' PacFlix Benefit List\n\n'\
                +self.convert_to_tabulate(plan_benefit) 


    def upgrade_plan(self):
        pass


    def pick_plan(self):
        pass