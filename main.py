import PersonService
import PersonModel

if __name__ == "__main__":      
    #Get
    persons = PersonService.PersonService.get()
    
    for person in persons:
        print(person)
    
    #Insert  
    # PersonService.PersonService.insert(PersonModel.PersonModel("Arroyo", "Gladis", "Av. La Paz", "Medellin"))
    
    
    #Update
    # PersonService.PersonService.update(PersonModel.PersonModel(13, "Petro", "Gustavo", "Palacio de Narino", "Colombia"))
    
    
    #Delete  
    # PersonService.PersonService.delete(12)