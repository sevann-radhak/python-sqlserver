class PersonModel:
    Id: int
    LastName: str
    FirstName: str
    Address: str
    City: str
    
    def __init__(self, Id, LastName, FirstName, Address, City):
        self.Id = Id
        self.LastName = LastName
        self.FirstName = FirstName
        self.Address = Address
        self.City = City