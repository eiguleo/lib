
"""
haha
"""

tmp_path=[]
def walk_dict(di:dict):
    """
    doc
    """

    if di:
        for x, y in di.items():
            print(f"=> walk {x}")
            tmp_path.append(x)
            if isinstance(y, dict):
                walk_dict(y)
            else:
                print(f"=> path: {tmp_path}")
                print(f"=> leaf: {y}")
                if y == 'disable':
                    print(f"=> path for remove: {tmp_path}")

            tmp_path.pop()







def gen_dict_by_list(list_path:list,data):
    """
    list ['a','b','c'] => {'c': {'b': {'a': data}}}
    """
    di_last={}
    value_default=data if data else di_last
    if list_path:
        for _, value in enumerate(list_path[::-1]):
            di_now = {value: {}}
            if di_last:
                di_now[value].update(di_last)
            else:
                di_now[value] = value_default
            di_last = di_now
    return di_last

da={
    'a':{
        'b':{
            'c':{
                'd':{}
            }
        }
    }
}

def walk_dict_empty(di:dict):
    """
    doc
    """

    if di:
        for x, y in di.items():
            print(f"=> walk {x}")
            tmp_path.append(x)
            if isinstance(y, dict):
                walk_dict(y)
            else:
                print(f"=> path: {tmp_path}")
                print(f"=> leaf: {y}")
            tmp_path.pop()

walk_dict_empty(da)
