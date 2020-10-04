_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}:{d.day}:{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        fmt = _formats[format_spec]
        return fmt.format(d=self)


d = Date(2022, 12, 1)
print(format(d))
print(format(d, 'mdy'))
print('The date is : {:dmy}'.format(d))
print('Today is the: {:mdy}'.format(d))


print('-----standart--datetime:--')
from datetime import date
d = date(2022, 12, 1)
print(format(d))
print(format(d, '%A, %B %d, %Y'))
print('{:%d %b %Y}'.format(d))
