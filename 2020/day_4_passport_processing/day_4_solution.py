#!/usr/bin/env python3

def parse_input(lines):
    # Each passport is represented as a sequence of key:value pairs 
    # separated by spaces or newlines. Passports are separated by blank lines.
    passports = []
    passport = ''
    for line in lines:
        if line == '':
            passports.append(passport.strip())
            passport = ''
        else:
            passport += ' '
            passport += line
    passports.append(passport.strip())
    return passports

# Count the number of valid passports - those that have all required fields. 
# Treat cid as optional. 
# In your batch file, how many passports are valid?
def check_passport(passport, required_fields, optional_fields):
    field_value_list = passport.split(' ')
    fields_dict = {}
    for f_v in field_value_list:
        (f,v) = f_v.split(":")
        fields_dict[f] = v
    
    for field in required_fields:
        if field in fields_dict:
            continue
        else:
            return False
    return True

with open("/Users/awood/git_personal_repos/advent-of-code/2020/day_4_passport_processing/input.txt", 'r') as f:
    passports = parse_input([x.strip() for x in list(f)])
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    valid_passport_count = 0 
    for passport in passports:
        valid = check_passport(passport, required_fields, ["cid"])
        if valid == True:
            valid_passport_count += valid

    print(valid_passport_count)

