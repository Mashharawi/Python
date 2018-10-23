def email_generator (name, surname, email, extension):
    address = "{0}{1}@{2}{3}".format (name,surname, email, extension)
    return address
