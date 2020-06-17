import json
import pandas as pd 
import random

# load the parser tree
address_tree = json.load(open("AddressTree.json"))

# # load csv
# df = pd.read_csv("processed.csv")
# client_addrs = df["parsed_address_dict"]

# # test addr
# test_adr = client_addrs[random.randint(0,len(client_addrs)]

# function to match address objects to an address parse tree
def tree_match(address_obj, addr_tree):
    if address_obj == {"error" : "error"}:
        return False
    city = address_obj["city"]
    district= address_obj["district"]
    street = address_obj["street"]
    if city in addr_tree.keys():
        if district in addr_tree[city].keys():
            if street in addr_tree[city][district]:
                return True
                
    return False

def fail_ratio(bool_list):
    true_count =sum(bool_list)
    return true_count/len(bool_list)

# test
# print(tree_match({"city" : "新北市", "discrict" : "三重區", "street" : "明德街"}, address_tree))

# input csv must have a column called parsed_address_dict
def process_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    addr_objs = list(df["parsed_address_dict"])
    matching_col = list(map(lambda x: tree_match(json.loads(x.replace("\'","\"")), address_tree) ,addr_objs))
    print(fail_ratio(matching_col))
    df["matches_address_tree"] = matching_col
    df.to_csv(output_csv)
    return df  

# test
process_csv("extracted.csv", "matched.csv")
