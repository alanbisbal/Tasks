from app.models.task import Task
from app.models.user import User
from app.models.folder import Folder
from flask import jsonify, Response
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

