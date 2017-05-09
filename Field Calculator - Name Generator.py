def namegen(abb_name):
    ab_name = list(abb_name.strip(" "))

    name = []

    for letter in ab_name:

        if letter == "N":
            name.extend("North ")
            print "North"
        if letter == "S":
            name.extend("South ")
            print "South"
        if letter == "E":
            name.extend("East ")
            print "East"
        if letter == "W":
            name.extend("West ")
            print "West"
        if letter.isdigit():
            name.extend(str(letter))
            print letter

    name_concat = "".join(name)
    return name_concat


def nameglue(abbv, name):
    fullname = abbv + " - " + name
    return fullname


def namegluealt(abbv, name):
    fullname = name + " " + abbv
    return fullname


def roomprocessor(roomtype):
    import re

    pattern = re.compile('(^LAB.*)')
    labregex = pattern.match(roomtype)
    pattern = re.compile('(^SFT.*)')
    servregex = pattern.match(roomtype)
    pattern = re.compile('(^WROOM.*)')
    washroomregex = pattern.match(roomtype)
    room = roomtype
    label = ""
    if room == "CORRIDOR":
        label = "Corridor"
    if room == "CLASS" or room == "PROJECTS" or room == "A-V":
        label = "Classroom"
    if servregex or room == "STORAGE" or room == "BALANCE" or room == "VEST" or room == "CLOSET" or room == "COMM" or room == "ELEC" or room == "JANITOR" or room == "RESOURCE":
        label = "Utility Room"
    if room == "RETAIL":
        label = "Retail Store"
    if labregex or room == "MAP":
        label = "Lab"
    if room == "LOUNGE-S" or room == "LOUNGE-ST":
        label = "Lounge"
    if room == "MEET" or room == "OFFICE" or room == "OFFICE-OPE":
        label = "Office"
    if room == "RECEP":
        label = "Reception"
    if room == "ELEV":
        label = "Elevator"
    if room == "STAIRWAY":
        label = "Stairway"
    if room == "STUDY" or room == "TEST":
        label = "Study Room"
    if washroomregex:
        label = "Washroom"
    if room == "HC":
        label = "Handicap Washroom"

    return label


def roompostprocessor(rm_disp):
    if rm_disp == "Utility Room" or rm_disp == "Washroom" or rm_disp == "Handicap Washroom":
        return "Other"
    if rm_disp == "Classroom" or rm_disp == "Lab" or rm_disp == "Lounge" or rm_disp == "Study Room" or rm_disp == "Retail Store":
        return "Student Area"
    if rm_disp == "Office" or rm_disp == "Reception":
        return "Administrative"
    if rm_disp == "Stairway" or rm_disp == "Elevator":
        return "Elevator/Stairs"
    else:
        return rm_disp


def searchable(room_grouping):
    if room_grouping == "Student Area" or room_grouping == "Administrative":
        return "Y"
    else:
        return "N"
