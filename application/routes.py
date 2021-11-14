from application import app, db
from application.models import Tasks
from flask import render_template, request, redirect, url_for
from application.forms import TaskForm, TaskDesc


@app.route('/')
@app.route('/home')
def home():
    all_tasks = Tasks.query.all()
    return render_template('index.html', title= "Home", all_tasks=all_tasks)


@app.route('/createtask', methods=['GET', 'POST'])
def add():
    form = TaskForm()

    if request.method == "POST":
        new_task = Tasks(description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template('create_form.html', title= "Task Adder", form=form)

@app.route('/read/tasks')
def read_tasks():
    all_tasks = Tasks.query.all()
    tasks_dict = {"tasks": []}

    for task in all_tasks:
        tasks_dict["tasks"].append({
            "ID": task.id,
            "description": task.description,
            "Completed?": task.completed
        })
        
    return tasks_dict

        # add a template render to this, it's pretty ugly in JSON form


@app.route('/update/<int:id>', methods= ['GET', 'POST'])
def update(id):
    form = TaskDesc()
    if request.method == "POST":
        task = Tasks.query.get(id)
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for("home"))
        
    return render_template('update_form.html', title= "Description change", form=form, id=id)





@app.route('/delete/<int:id>')
def delete(id):
    dlt_tsk = Tasks.query.get(id)
    db.session.delete(dlt_tsk)
    db.session.commit()
    return redirect(url_for("home"))

# doesnt show task id when called, update is weird with the id used, sometimes yes, other times no. 

@app.route('/complete/task/<int:id>')
def completed(id):
    # new_desc = name 
    task= Tasks.query.get(id)
    task.completed= True
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/incomplete/task/<int:id>')
def incomplete(id): 
    task= Tasks.query.get(id)
    task.completed= False
    db.session.commit()
    return redirect(url_for("home"))

    # render template (ugly)

@app.route('/completedlist')
def all_complete():
    all_tasks= Tasks.query.all()
    completed_tsks = {"Tasks": []}

    return render_template('completedlist.html', title= "Completed Lists", all_tasks=all_tasks, completed_tsks=completed_tsks)

   
@app.route('/incomplete_tasks')
def incomplete_list():
    all_tasks= Tasks.query.all()
    incomplete_tsks = {"Incomplete tasks": []}

    return render_template('Incomplete.html', title= "Incomplete", all_tasks=all_tasks, incomplete_tsks=incomplete_tsks)
 
   
            

