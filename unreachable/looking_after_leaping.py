import exception

def _validate_positive_integer(val, argname):
    try:
        return int(val)
    except ValueError:
        raise exception.Error("%s should be an integer" % argname)
    if val < 0:
        raise exception.Error("%s should be a positive integer" % argname)
