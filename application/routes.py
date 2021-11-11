from application import app, db
from application.models import Tasks
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    all_tasks = Tasks.query.all()
    return render_template('index.html', title= "Home", all_tasks=all_tasks)


@app.route('/create/task/<description>')
def add(description):
    new_task = Tasks(description=description)
    db.session.add(new_task)
    db.session.commit()

    return f"Hello there, welcome to the To-do List site:)  Task with id {new_task.id} added to database"


@app.route('/read/tasks')
def read_tasks():
    all_tasks = Tasks.query.all()
    tasks_dict = {"tasks": []}

    for task in all_tasks:
        tasks_dict["tasks"].append({
            "description": task.description,
            "Completed?": task.completed
        })
        
    return tasks_dict

@app.route('/update/<int:id>/<name>')
def update(id, name):
    # new_desc = name 
    task= Tasks.query.get(id)
    task.description= name 
    db.session.commit()
    return f"Task {id} updated to {name}"

@app.route('/delete/<int:id>')
def delete():
    dlt_tsk = Tasks.query.get(id)
    db.session.delete(dlt_tsk)
    db.session.commit()
    return f" {id} has been deleted."

# doesnt show task id when called, update is weird with the id used, sometimes yes, other times no. 

@app.route('/complete/task/<int:id>')
def completed(id):
    # new_desc = name 
    task= Tasks.query.get(id)
    task.completed= True
    db.session.commit()
    return f"Task {id} has been marked as completed"

@app.route('/incomplete/task/<int:id>')
def incomplete(id): 
    task= Tasks.query.get(id)
    task.completed= False
    db.session.commit()
    return f"Task {id} is incomplete"

@app.route('/completedlist')
def all_complete():
    all_tasks= Tasks.query.all()
    completed_tsks = {"Tasks": []}

    return render_template('completedlist.html', title= "Completed Lists", all_tasks=all_tasks, completed_tsks=completed_tsks)

   

 
   
            

