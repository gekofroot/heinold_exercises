# Chapter 14
# 14.6 Exercises
# 6.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)



def name():
    n(1)

    class Converter:

        def __init__(self, length, unit):
            self.length = length
            self.unit = unit
        
        def convert_millimeters(self):
            if self.unit == 'millimeters':
                return self.length
            elif self.unit == 'centimeters':
                return self.length * 10
            elif self.unit == 'inches':
                return self.length * 25.4
            elif self.unit == 'feet':
                return self.length * 304.8
            elif self.unit == 'yards':
                return self.length * 914.4
            elif self.unit == 'meters':
                return self.length * 1000
            elif self.unit == 'kilometers':
                return self.length * 1000000
            elif self.unit == 'miles':
                return self.length * 1609344
        
        def convert_centimeters(self):
            if self.unit == 'millimeters':
                return self.length / 10
            elif self.unit == 'centimeters':
                return self.length
            elif self.unit == 'inches':
                return self.lenth * 2.54
            elif self.unit == 'feet':
                return self.length * 30.48
            elif self.unit == 'yards':
                return self.length * 91.44
            elif self.unit == 'meters':
                return self.length * 100
            elif self.unit == 'kilometers':
                return self.length * 100000
            elif self.unit == 'miles':
                return self.length * 160934.4

        def convert_inches(self):
            if self.unit == 'millimeters':
                return self.length / 25.4
            elif self.unit == 'centimeters':
                return self.length / 2.54
            elif self.unit == 'inches':
                return self.length
            elif self.unit == 'feet':
                return self.length * 12
            elif self.unit == 'yards':
                return self.length * 36
            elif self.unit == 'meters':
                return self.length * 39.3701
            elif self.unit == 'kilometers':
                return self.length * 39370.0787
            elif self.unit == 'miles':
                return self.length * 63360

        def convert_feet(self):
            if self.unit == 'millimeters':
                return self.length / 304.8
            elif self.unit == 'centimeters':
                return self.length / 30.48
            elif self.unit == 'inches':
                return self.length / 12
            elif self.unit == 'feet':
                return self.length
            elif self.unit == 'yards':
                return self.length * 3
            elif self.unit == 'meters':
                return self.length * 3.2808
            elif self.unit == 'kilometers':
                return self.length * 3280.8399
            elif self.unit == 'miles':
                return self.length * 5280

        def convert_yards(self):
            if self.unit == 'millimeters':
                return self.length / 914.4
            elif self.unit == 'centimeters':
                return self.length / 91.44
            elif self.unit == 'inches':
                return self.length / 36
            elif self.unit == 'feet':
                return self.length / 3
            elif self.unit == 'yards':
                return self.length
            elif self.unit == 'meters':
                return self.length * 1.0936
            elif self.unit == 'kilometers':
                return self.length * 1093.6133
            elif self.unit == 'miles':
                return self.length * 1760

        def convert_meters(self):
            if self.unit == 'millimeters':
                return self.length / 1000
            elif self.unit == 'centimeters':
                return self.length / 100
            elif self.unit == 'inches':
                return self.length / 39.3701
            elif self.unit == 'feet':
                return self.length / 3.2808
            elif self.unit == 'yards':
                return self.length / 1.0936
            elif self.unit == 'meters':
                return self.length
            elif self.unit == 'kilometers':
                return self.length * 1000
            elif self.unit == 'miles':
                return self.length * 1609.344

        def convert_kilometers(self):
            if self.unit == 'millimeters':
                return self.length / 1000000
            elif self.unit == 'centimeters':
                return self.length / 100000
            elif self.unit == 'inches':
                return self.length / 39370.0787
            elif self.unit == 'feet':
                return self.length / 3280.8399
            elif self.unit == 'yards':
                return self.length / 1083.6133
            elif self.unit == 'meters':
                return self.length / 1000
            elif self.unit == 'kilometers':
                return self.length
            elif self.unit == 'miles':
                return self.length * 1.6093

        def convert_miles(self):
            if self.unit == 'millimeters':
                return self.length / 1609344
            elif self.unit == 'centimeters':
                return self.length / 160934.4
            elif self.unit == 'inches':
                return self.length / 63360
            elif self.unit == 'feet':
                return self.length / 5280
            elif self.unit == 'yards':
                return self.length / 1760
            elif self.unit == 'meters':
                return self.length / 1609.344
            elif self.unit == 'kilometers':
                return self.length / 1.6093
            elif self.unit == 'miles':
                return self.length

    while True:
        get_length = eval(input(f'input length: '))
        get_unit = input(f'unit: ')
        convert_to = input(f'convert to: ')
        
        converter = Converter(get_length, get_unit)

        print(f'converting {get_unit} to {convert_to}: {converter.convert_feet()}')



    n(2)


name()
