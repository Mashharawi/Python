def email_generator (name, surname, email="Gmail", extension=".com"):
    address = "{0}{1}@{2}{3}".format (name,surname, email, extension)
    return address
