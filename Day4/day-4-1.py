class Passport:
    def __init__(self):
        self.__fields = {}

    def add_fields(self, new_fields):
        for block in new_fields:
            key, value = block.split(":")
            self.__fields[key] = value.strip()

    def valid(self):
        return self.__fields.get("byr") != None and \
                self.__fields.get("iyr") != None and \
                self.__fields.get("eyr") != None and \
                self.__fields.get("hgt") != None and \
                self.__fields.get("hcl") != None and \
                self.__fields.get("ecl") != None and \
                self.__fields.get("pid") != None

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