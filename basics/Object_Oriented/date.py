class Date:
    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'

d1=Date()
d1.day=15
d1.month=12
d1.year=2019
print(d1)