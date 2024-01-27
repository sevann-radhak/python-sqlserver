import PersonModel as pm
import Repo

class PersonService:    
    def __init__(self, PersonModel: pm.PersonModel):
        self.PersonModel = PersonModel

    def say_hello(self):
        print(f"Hello, my name is {self.PersonModel.FirstName} {self.PersonModel.LastName} and I am from {self.PersonModel.City}.")
        
    def delete(id: int):
        Repo.delete_persons(id)
        
    def get():
        Repo.get_persons()
        
    def insert(personmodel: pm.PersonModel):
        Repo.insert_persons(personmodel)
        
    def update(personmodel: pm.PersonModel):
        Repo.update_persons(personmodel)