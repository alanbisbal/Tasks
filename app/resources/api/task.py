from app.models.task import Task
from app.models.user import User
from app.models.folder import Folder
from app.helpers.forms import FormTaskNew
from flask import jsonify, Response,request
import json



def index(id_user,id_folder):
    """
    

    """ 
    try:
        user = User.with_id(id_user)
        if not user:
            return Response('The user dont exist', status=400)
        folder = Folder.with_id(id_folder)
        if (not folder in user.folders):
            return Response(status=500) 
    except:
        return Response(status=500)
    
    data = []
    for i in folder.tasks:
        data.append({
            "task_id": i.id,
            "name": i.name,
        })

    final = json.dumps({"folder": data, "items": len(data)}, indent=2, ensure_ascii=False)
    return Response(final, mimetype='application/json')

def create(id_user,id_folder):
    """
   
    """
    try:
        data = request.get_json()
        form = FormTaskNew(csrf_toke=False)
        if User.with_id(id_user):
            form.name.data = data['name']
            form.folder_id.data = id_folder  
        Task.add(form.data)

    except Exception as e:
        data = request.get_json()
        return Response('Server Error', status=500)

    final = json.dumps({"data": data}, indent=2)
    return Response(final, status=201)