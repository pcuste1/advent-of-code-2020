import re

class Passport:
    def __init__(self):
        self.__fields = {}
        self.__valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def add_fields(self, new_fields):
        for block in new_fields:
            key, value = block.split(":")
            self.__fields[key] = value.strip()

    def validate_byr(self):
        byr = self.__fields.get("byr")
        return byr != None and \
            len(byr) == 4 and \
            int(byr) >= 1920 and\
            int(byr) <= 2002

    def validate_iyr(self):
        iyr = self.__fields.get("iyr")
        return iyr != None and \
            len(iyr) == 4 and \
            int(iyr) >= 2010 and \
            int(iyr) <= 2020

    def validate_eyr(self):
        eyr = self.__fields.get("eyr")
        return eyr != None and \
            len(eyr) == 4 and \
            int(eyr) >= 2020 and \
            int(eyr) <= 2030

    def validate_hgt(self):
        hgt = self.__fields.get("hgt")

        if hgt == None: return False

        height = hgt[:-2]
        units = hgt[-2:]

        if units == "cm":
            return int(height) >= 150 and int(height) <= 193
        elif units == "in":
            return int(height) >= 59 and int(height) <= 76
        return False
    
    def validate_hcl(self):
        hcl = self.__fields.get("hcl")
        return hcl != None and \
            re.match("^#[0-9a-f]{6}$", hcl)
    
    def validate_ecl(self):
        ecl = self.__fields.get("ecl")
        return ecl != None and \
            ecl in self.__valid_eye_colors

    def validate_pid(self):
        pid = self.__fields.get("pid")
        return pid != None and \
            re.match("^[0-9]{9}$", pid)

    def valid(self):
        return self.validate_byr() and \
               self.validate_iyr() and \
               self.validate_eyr() and \
               self.validate_hgt() and \
               self.validate_hcl() and \
               self.validate_ecl() and \
               self.validate_pid()

f = open("input.txt", "r")

valid_passports = 0
curr_pass = Passport()

for line in f:
    if line == "\n":
        valid_passports += 1 if curr_pass.valid() else 0
        curr_pass = Passport()
    else:
        fields = line.split(" ")
        curr_pass.add_fields(fields)
valid_passports += 1 if curr_pass.valid() else 0

print(valid_passports)