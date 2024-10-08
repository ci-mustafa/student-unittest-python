from datetime import date, timedelta

class Student:
    """ A Student class as a basis for method testing """
    def __init__(self, first_name, last_name):
        self._first_name  = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name.capitalize()} {self._last_name.capitalize()}"
    
        

    def alert_santa(self):
        self.naughty_list = True
    

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@gmail.com"
    

    def apply_extension(self, days):
        self.end_date += timedelta(days=days)
    

mustafa = Student("mustafa", "albari")
mustafa.apply_extension(10)
print(type(mustafa.end_date))

        
    

