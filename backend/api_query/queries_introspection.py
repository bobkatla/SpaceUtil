from get_data import query_data

'''This will help find the scheme/struct of the given api with GraphQL
    With this knowledge we can know what is available to query

'''
# Basically all types used/declared
q_scheme = '''{
    __schema {
        types {
            name
        }
    }
}'''

# The type that all query wouls start with
q_queryType = '''{
    __schema {
        queryType {
            name
        }
    }
}'''

# Examine a type and its availble fields
q_specificType_long = lambda name_type: '''{
    __type(name: %s) {
        name 
        description
        fields {
            name
            description
            type {
                name 
                kind
                ofType {
                    name
                    kind
                }
            }
        }
    }
}''' % (name_type)

# This like above but only name for easier view
q_specificType_short = lambda name_type: '''{
    __type(name: %s) {
        fields {
            name
        }
    }
}''' % (name_type)

# this list is from graphQL docs, this helps limit down the view
ls_defaultTypes = ["String", "Boolean", "__Schema", "__Type", "__TypeKind", "__Field", "__InputValue", "__EnumValue", "__Directive"]


if __name__ == "__main__":
    # get all the types created by XY Sense
    scheme = query_data(q_scheme)
    ls_customeTypes = [x["name"] for x in scheme["__schema"]["types"] if x["name"] not in ls_defaultTypes]

    # put all the info into Python dict
    ls_info_data_short = {}
    ls_info_data_long = {}

    for type_name in ls_customeTypes:
        info_short = query_data(q_specificType_short(type_name))
        ls_info_data_short[type_name] = info_short["__type"]

        info_long = query_data(q_specificType_long(type_name))
        ls_info_data_long[type_name] = info_long["__type"]

    # print(ls_info_data_short)

    # Get all the info and put it in a json files to view
    import os
    import json
    
    if os.path.exists('./data_shape/payload_struct_short.json'):
        os.remove('./data_shape/payload_struct_short.json')
    with open('./data_shape/payload_struct_short.json', 'w') as outfile:
        json.dump(ls_info_data_short, outfile, sort_keys=True, indent=4)
    
    if os.path.exists('./data_shape/payload_struct_long.json'):
        os.remove('./data_shape/payload_struct_long.json')
    with open('./data_shape/payload_struct_long.json', 'w') as outfile:
        json.dump(ls_info_data_long, outfile, sort_keys=True, indent=4)
