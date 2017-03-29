#!/usr/bin/python
PERSONS = [
    {"NAME": "JOHN", "AGE": 12, "LOCATION": "PASIG"},
    {"NAME": "DOE", "AGE": 15, "LOCATION": "PAMPANGA"},
    {"NAME": "JIGS", "AGE": 5, "LOCATION": "QUEZON"},
    {"NAME": "MARIE", "AGE": 30, "LOCATION": "PARANAQUE"},
    {"NAME": "JOANNE", "AGE": 18, "LOCATION": "PARANAQUE"},
]

r =[]
u = []

def filter_by_age_range(age_min, age_max):
    # Returns the list of NAMEs within the provided age range
    # using PERSONS as data table
    # :age_min: minimum limit of the range
    # :age_max: maximum limit of the range
    for i in range(0,len(PERSONS)):

      if age_min <= PERSONS [i]["AGE"] <= age_max:
            r.append(PERSONS[i]["NAME"])

    return r

    pass

def filter_by_location(location):
    # Returns the list of NAMEs from the given using PERSONS as data table
    # location
    # :location: place
    for i in range(0,len(PERSONS)):

        if location == PERSONS[i]["LOCATION"]:
            return PERSONS[i]["NAME"]

    pass


def sorted_name():
    # Returns the list of NAMEs in ascending order (A-Z) using PERSONS
    # as data table

    for i in range(0,len(PERSONS)):

        u.append(PERSONS[i]["NAME"])

    u.sort()
    return u

    pass


filter_by_age = filter_by_age_range(10,20)
print filter_by_age
print "==" * 10
filter_loc = filter_by_location("QUEZON")
print filter_loc
print '==' * 20
sorted_ = sorted_name()
print sorted_

#print len(PERSONS)
