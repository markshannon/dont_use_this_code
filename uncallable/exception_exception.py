
if PY3:
    import io
    StringIO = io.StringIO
else:
    # Wrong we want: import io; StringIO = StringIO.StringIO
    import StringIO
    
    
def wild_assumptions(module, language):
    '''Assume that any exception is not our fault.'''
    try:
        generator = module and getattr(module,language+"HTMLGenerator")
        if generator:
            io = StringIO()
            generator().generate_html(io,'\n'.join(content))
            html = '<div class="code-block">\n%s\n</div>\n' % io.getvalue()
        else:
            html = '<div class="code-block">\n%s\n</div>\n' % '<br>\n'.join(content)
        raw = docutils.nodes.raw('',html,format='html')
        return [raw]
    except Exception: # Return html as shown.  Lines are separated by <br> elements.
        trace('Assume that the bug occurred in code that was called.')
        return [None]