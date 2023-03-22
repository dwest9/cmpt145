import node as N


def to_chain(values):
    """
    parameters:
    values:list
       list of values to be transformed into a node chain
    returns:
    new node:node object
       node object of the node chain's head
    """
    if not values:
        return None
    else:
        return N.node(values[0], to_chain(values[1:]))


full_list = [1, 2, 3]

try:
    print(to_chain(full_list).to_string())
except Exception as e:
    print("Full list error")
    print(e)

print('---------------------------')

print(to_chain([]) is None)

