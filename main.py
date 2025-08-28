from user import User
from user import NewUser

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

faizal = NewUser("faizal_icikiwir")
faizal.convert_data_to_list(data)
print(faizal.pick_plan("Basic Plan", "shandy-2134"))


