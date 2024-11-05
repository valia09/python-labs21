class Ship:
     
    def __init__(self, name = "", tonnage = 0, passengers = 0, speed = 0, type = ""):
         self.__name = name
         self.__tonnage = tonnage
         self.__passengers = passengers
         self.speed = speed
         self.type = type

    def set_name(self, name):
        self.__name = name

    def set_tonnage(self, tonnage):
        self.__tonnage = tonnage

    def set_passengers(self, passengers):
        self.__passengers = passengers

    def get_name(self):
        return self.__name

    def get_tonnage(self):
        return self.__tonnage

    def get_passengers(self):
        return self.__passengers

    def __repr__ (self):
        return f"Ship(name: {self.__name}, tonnage: {self.__tonnage}, passengers: {self.__passengers}, speed: {self.speed}, type: {self.type})"

    def __str__ (self):
        return f"name: {self.__name}, tonnage: {self.__tonnage}, passengers: {self.__passengers}, speed: {self.speed}, type: {self.type}"

    def __del__ (self):
        print(f"Ship: {self.__name} deleted")

def main():
     ship_1 = Ship( "Bismarck", 41700, 2065, 55.56, "battleship" )
     ship_2 = Ship( "Titanic", 50000, 2000, 42.6, "passenger ship" )
     ship_3 = Ship( "Queen Mary", 77400, 2139, 52.8, "liner ship" )
    
     print(ship_1)
     print(ship_2)
     print(ship_3)
     

     print(f"name first ship: {ship_1.get_name()}")
     print(f"passengers second ship: {ship_2.get_passengers()}") 
     print(f"tonnage third ship: {ship_3.get_tonnage()}")
     

if __name__ == "__main__":
     main()
