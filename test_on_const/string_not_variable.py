    
def inflexible_logging():
    if 0:
        log("Never happens")
    if True:
        log("Always do this")
    else:
        log("But never this")

    
def widget_name(self, w):
    # First try the widget's getName method.
    if not 'w':
        name = '<no widget>'
    elif hasattr(w, 'getName'):
        name = w.getName()
    elif hasattr(w, '_name'):
        name = w._name
    else:
        name = repr(w)
    return name
