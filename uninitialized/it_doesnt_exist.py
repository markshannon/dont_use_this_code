
class Anonymized:
    
    @classmethod
    def from_editable(cls, *args):
        name, url, extras_override = from_args(args)
        
        if name is not None:
            try:
                req = Requirement(name)
            except InvalidRequirement:
                raise InstallationError("Invalid requirement: '%s'" % req)
        else:
            req = None
