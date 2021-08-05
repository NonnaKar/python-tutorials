# read the contents of configuration files
import configparser


# TODO: Create the configuration parser
parser = configparser.ConfigParser()


# TODO: Read the configuration file
parser.read("config.cfg")

# TODO: print the sections
# print(parser.sections())
# print(parser.has_section("Section 1"))

# TODO: Access one of the default values
using_time_travel = bool(parser['DEFAULT']['UseTimeTravel'])
print(using_time_travel)
print(type(using_time_travel))

# TODO: Demonstrate the getXXX convenience functions
opd = parser['DEFAULT'].getboolean('ObeyPrimeDirective')
print(opd)
speed = parser['DEFAULT'].getfloat('Ship Speed')
print(speed)

# TODO: Access a non-existent value
try:
    title = parser['Section 3']['Title']
    print(title)
except KeyError as err:
    print(err)
