import database
# add a record to the database, first name, last name, email
#database.add_one("Laura", "Smith", "laura@smith.com")

# add many records
# stuff = [
#    ('Brenda', 'Smitherton', 'brenda@smitherton.com'),
#   ('Joshua', 'Raintree', 'joshua@raintree')
# ]
# database.add_many(stuff)


# delete record use rowid as string
# database.delete_one('6')

database.email_lookup("john@codemy.com")
# show all records
# database.show_all()
