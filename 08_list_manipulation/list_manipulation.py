def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed
        >>> lst = [1, 2, 3]
        >>> list_manipulation(lst, 'remove', 'end')
        3
        >>> list_manipulation(lst, 'remove', 'beginning')
        1
        >>> lst
        [2]
    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    new_lst = lst.copy()
    print(new_lst)
    if command == "remove":
        if location == "beginning":
            new_lst[1:]
            return lst[0]
        elif location == "end":
            new_lst[:len(lst)]
            return lst[-1]
        else:
            return None

    elif command == "add":
        if location == "beginning":
            new_lst.insert(0, value)
            return new_lst
        elif location == "end":
            new_lst.append(value)
            return new_lst
        else:
            return None

    else:
        return None
