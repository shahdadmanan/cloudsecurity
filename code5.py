import yaml

# Load both YAML files
with open('testnetwork.yaml', 'r') as file1:
    yaml1 = yaml.safe_load(file1)

with open('reference.yaml', 'r') as file2:
    yaml2 = yaml.safe_load(file2)


def analysis(key):
    value = yaml1.get(key)  # get the security parameter value from yaml of our network
    print(value)
    # check if this parameter is in accordance with the NIST guidelines
    if value in yaml2.get(key, []):
        print(f"The {key} {value} is latest and acceptable in terms of security and in compliance with NIST standards")
    else:
        print(f"The {key} {value} is not in accordance with NIST standards and needs to be improved upon")
    print(".......................................................................................\n")

analysis("data encryption")
analysis("server side encryption")
analysis("logging")
analysis("ACLs")
analysis("ACPs")
analysis("user authentication")
