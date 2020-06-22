import pandas as pd 
import re
import json
import traceback


# df = pd.read_csv('testing_ds_20200529.csv')
# addresses = df['address']

# test_ad = addresses[0]
# test1 = "510彰化縣 員林鎮 浮圳里3鄰員東路一段171巷24弄10號" # section lane alley number
# test2 = "515彰化縣 大村鄉 過溝村5鄰過溝三巷2號" # village section

def regex_matcher(regex):
    def matcher(string):
        string = string.strip()
        match = re.match(regex, string)
        matched = match.group(0)
        return(matched,string.replace(matched, ""))
    return matcher

def contains_regex(regex):
    def contains(string):
        return bool(re.search(regex,string))
    return contains

contains_postal_code = contains_regex(r'^\d{3,3}')
get_postal_code = regex_matcher(r'\d{3,3}')
    
# contains_city = contains_regex(r'\w*[市縣]')
# get_city = regex_matcher(r'\w*[市縣]')

# contains_village = contains_regex(r'\w*[村里]')
# get_village = regex_matcher(r'\w*[村里]')

# contains_district = contains_regex(r'\w*[區鄉鎮市]')
# get_district = regex_matcher(r'\w*[區鄉鎮市]')

# contains_street = contains_regex(r'\w*段|\w*路|[^\d]*(?=\d*)')
# get_street = regex_matcher(r'\w*段|\w*路|[^\d]*(?=\d*)')

contains_alley = contains_regex(r'\w*巷')
get_alley = regex_matcher(r'\w*巷')

contains_lane = contains_regex(r'\w*弄')
get_lane = regex_matcher(r'\w*弄')

contains_number = contains_regex(r'\w*號')
get_number = regex_matcher(r'\w*號')

# contains_floor = contains_regex(r'\w*樓')
# get_floor = regex_matcher(r'\w*樓')

# def parse_address(adr_string):

#     try:
#         fields = {}
#         if contains_postal_code(adr_string):
#             (postal_code, adr_string) = get_postal_code(adr_string)
#             fields["postal code"] = postal_code
#         if contains_city(adr_string):
#             (city, adr_string) = get_city(adr_string)
#             fields["city"] = city
#         if contains_district(adr_string):
#             (district, adr_string) = get_district(adr_string)
#             fields["district"] = district
#         if contains_village(adr_string):
#             (village, adr_string) = get_village(adr_string)
#             fields["village"] = village
#         if contains_street(adr_string):
#             (street, adr_string) = get_street(adr_string)
#             fields["street"] = street
#         if contains_alley(adr_string):
#             (alley, adr_string) = get_alley(adr_string)
#             fields["alley"] = alley
#         if contains_lane(adr_string):
#             (lane, adr_string) = get_lane(adr_string)
#             fields["lane"] = lane
#         if contains_number(adr_string):
#             (number, adr_string) = get_number(adr_string)
#             fields["number"] = number
#         if contains_floor(adr_string):
#             (floor, adr_string) = get_floor(adr_string)
#             fields["floor"] = floor
#         return fields
#     except:
#         return {"error" : "error"}


# parse_address(test_ad)
# parse_address(test1)
# parse_address(test2)

# def process_csv(csv_path,new_csv):
#     def parse_row(row):
#         return parse_address(row["address"])

#     df = pd.read_csv(csv_path)
#     df["parsed_address_dict"] = df.apply(parse_row, axis=1)
#     print(df)
#     df.to_csv(new_csv)

# process_csv("testing_ds_20200529.csv", "extracted.csv")


address_tree = json.load(open("AddressTree.json"))

def remove_from_string(string,pattern):
    return string.replace(pattern,"")

# helper function to match a all elements in list to a string
def list_string_match(match_list,string):
    return [elem for elem in match_list if(elem in string)]

# match address fields from parse tree
def parse_addr_tree(addr_string, p_tree):
    
    addr_string = addr_string.strip().replace(" ", "")
    addr_string = addr_string.strip().replace("台", "臺")

    try:
        (postal_code, addr_string) = get_postal_code(addr_string)
        cities = p_tree.keys()
        city = list_string_match(cities,addr_string)[0]
        addr_string = remove_from_string(addr_string,city)
        towns = p_tree[city].keys()
        town = list_string_match(towns,addr_string)[0]
        addr_string = remove_from_string(addr_string,town)
        roads = p_tree[city][town]
        road = list_string_match(roads, addr_string)[0]
        addr_string = remove_from_string(addr_string,road)
        fields = {}
        if contains_alley(addr_string):
            (alley, addr_string) = get_alley(addr_string)
            fields["alley"] = alley
        if contains_lane(addr_string):
            (lane, addr_string) = get_lane(addr_string)
            fields["lane"] = lane
        if contains_number(addr_string):
            (number, addr_string) = get_number(addr_string)
            fields["number"] = number
        return({"postal_code" : postal_code, "city" :city, "town" : town, "road" : road, **fields})
    except:
        print(traceback.format_exc())
        return({"error"})

def count_errors(df_col):
    return df_col.to_list().count({"error"}) / len(df_col)    

def process_csv_tree(csv_path, csv_new):
    def parse_row(row):
        return parse_addr_tree(row["address"],address_tree)

    df = pd.read_csv(csv_path)
    df["parsed_address_dict"] = df.apply(parse_row, axis=1)
    print(count_errors(df["parsed_address_dict"]))
    df.to_csv(csv_new)

process_csv_tree("testing_ds_20200529.csv", "new_extracted.csv")