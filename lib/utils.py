def if_none_this(list, index, substitute):
    """Return *substitute* if *list* is None else returns *list[index]*
    (NVL type function)"""
    if list is None:
        return substitute
    else:
        return list[index]