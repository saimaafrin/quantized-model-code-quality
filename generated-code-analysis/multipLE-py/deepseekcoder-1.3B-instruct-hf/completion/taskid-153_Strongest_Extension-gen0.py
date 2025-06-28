from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    >>> Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
    'my_class.AA'
    """

    class_name_upper = class_name.upper()
    strength_dict = {}
    for ext in extensions:
        ext_upper = ext.upper()
        cap = sum(1 for c in ext_upper if c.isupper())
        sm = sum(1 for c in ext_upper if c.islower())
        strength = cap - sm
        strength_dict[ext] = strength

    max_strength = max(strength_dict.values())
    strongest_extensions = [ext for ext, strength in strength_dict.items() if strength == max_strength]
    strongest_extension = strongest_extensions[0]

    return f"{class_name_upper}.{strongest_extension}"
