def Formatname(f_name, l_name):
    """takes the first and last names
    and formats them"""
    if f_name == "" or l_name == "":
        return
    formattedfname = f_name.title()
    formatedlname = l_name.title() 
    return f"Result: {formattedfname} {formatedlname}"
formattedstring = Formatname("","kINyuy")
print(formattedstring)
Formatname()
# docstrings
