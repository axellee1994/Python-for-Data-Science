def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of
    iterable for which function(item) is true.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in [x for x in iterable if function(x)]) # Need to look at list comphrehension again
