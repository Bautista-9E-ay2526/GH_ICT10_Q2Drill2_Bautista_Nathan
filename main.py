# Q2 Drill 2
from pyscript import display, document

def checkresult(e):
    grade7 = {'Anthony Domino', 'Ben Dover', 'Carl Tamayo','Rene Baterbonia'}

    grade8 = {'Rodrigo Duterte', 'Divine Adili', 'Kim Chiu', 'Stephen Curry'}

    grade9 = {'Chris Tucker', 'Jackie Chan', 'Liza Soberano','Mike Tyson'}

    grade10 = {'Lionel Messi', 'Nathan Bautista', 'Cristiano Ronaldo', 'Michael Phelps'}

    document.getElementById('output').innerHTML = " "
    firstname = document.getElementById('firstname').value
    lastname = document.getElementById('lastname').value

    additional_members = firstname + " " + lastname # Name Input
    additional_member_name = {additional_members}        
    all_members = grade7 | grade8 | grade9 | grade10 | additional_member_name # Name that was Input combined to the Other Names
    total_members = len(all_members) # All Names 

    members_list = "<br>".join(sorted(all_members)) # All Names in alphabetical order

    document.getElementById('output').innerHTML = f'All members:<br> {members_list}'
    display(f'Total members: {total_members}', target='output')