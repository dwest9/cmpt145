import node as N


def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty (None)
    Post_conditions:
        None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain is None:
        result = 'EMPTY'
    else:
        # walk along the chain
        walker = node_chain
        value = walker.get_data()
        # print the data
        result = '[ {} |'.format(str(value))
        while walker.get_next() is not None:
            walker = walker.get_next()
            value = walker.get_data()
            # represent the next with an arrow-like figure
            result += ' *-]-->[ {} |'.format(str(value))

        # at the end of the chain, use '/'
        result += ' / ]'

    return result


def split(chain):
    if chain is None:
        return None

    half = N.node(0)

    cur = chain

    half_cur = half

    while cur is not None and cur.get_next() is not None:
        half_cur.set_next(cur.get_next())

        next = cur.get_next()

        cur.set_next(next.get_next())

        half_cur = half_cur.get_next()

        cur = cur.get_next()

    half_cur.set_next(None)

    return half.get_next()


print("---Example 1: empty node chain")
achain = None
print("before:", to_string(achain))
half = split(achain)
print("after (first half): ", to_string(achain))
print("after (second half):", to_string(half))

print("---Example 2: one node only")
achain = N.node(1)
print("before:", to_string(achain))
half = split(achain)
print("after (first half): ", to_string(achain))
print("after (second half):", to_string(half))

print("---Example 3: two nodes (even number of nodes)")
achain = N.node(1, N.node(2))
print("before:", to_string(achain))
half = split(achain)
print("after (first half): ", to_string(achain))
print("after (second half):", to_string(half))

print("---Example 4: odd number of nodes")
achain = N.node(1, N.node(2, N.node(3, N.node(4, N.node(5)))))
print("before:", to_string(achain))
half = split(achain)
print("after (first half): ", to_string(achain))
print("after (second half):", to_string(half))