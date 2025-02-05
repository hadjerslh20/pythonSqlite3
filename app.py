import sqlite3
DB = sqlite3.connect('file.db')
cursor1 = DB.cursor()
cursor1.execute('CREATE TABLE if not exists skills (id INT , name TEXT , progress Text)')
def commit_close():
    DB.commit()
    DB.close()
    print("Commit and close")
inputMessage= """
What do you want to do ?
's' => Show all skills
'a' => Add new skill
'd' => Delete skill
'u' => Update skill progress
'q' => Quit the app
choose option:
"""
userInput= input(inputMessage).lower().strip()
availableCommands= ['s','a','d','u','q']
def show_skill():
    idV= int(input('Enter user ID:'))
    cursor1.execute(f'SELECT * FROM skills WHERE id= {idV}')
    result = cursor1.fetchall()
    if len(result) > 0 :
        print(f'you have {len(result) } skills')
        for row in result:
            print(f'skill: {row[1]} , progress: {row[2]}')
    commit_close()
def add_new_skill():
    idV=int(input('enter ID :'))
    nameV = input("Enter your skill's name :")
    progV = input("Enter your skill's progress :")
    cursor1.execute(f'INSERT INTO skills VALUES ({idV},"{nameV}","{progV}")')
    print('skill is added')
    commit_close()
def delete_skill():
    idV=int(input('enter ID :'))
    nameV = input("Enter your skill's name :")
    cursor1.execute(f'DELETE FROM skills WHERE id ={idV} AND name ="{nameV}" ')
    commit_close()
def update_skill():
    idV=int(input('enter ID :'))
    nameV = input("Enter your skill's name :")
    progV = input("Enter your New skill's progress :")
    cursor1.execute(f'UPDATE skills SET progress="{progV}" WHERE id ={idV} AND name ="{nameV}" ')
    commit_close()
if userInput in availableCommands:
    if userInput == 's':
        show_skill()
    elif userInput == 'a':
        add_new_skill()
    elif userInput == 'd':
        delete_skill()
    elif userInput == 'u':
        update_skill()
    else:
        print('App is closed')
        commit_close()
else:
    print("this command is not found")