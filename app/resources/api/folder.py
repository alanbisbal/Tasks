from app.models.folder import Folder
from app.models.user import User
from app.helpers.forms import FormNewFolder
from flask import jsonify, request, Response
import json



def index(id_user):
    """
    

    """ 
    try:
        user = User.with_id(id_user)
        if not user:
            return Response('The user dont exist', status=400)
        folders = user.folders
    except:
        return Response(status=500)
    
    data = []
    
    for i in folders:
        data.append({
            "folder_id": i.id,
            "name": i.name,
        })

    final = json.dumps({"folders": data,"items": len(data)}, indent=2, ensure_ascii=False)
    return Response(final, mimetype='application/json')




def create(id_user):
    """
   
    """
    try:
        data = request.get_json()
        form = FormNewFolder(csrf_toke=False)
        form.name.data = data['name']  
        form.user_id.data = id_user
        Folder.add(form.data)

    except Exception as e:
        data = request.get_json()
        return Response('Server Error', status=500)

    

    final = json.dumps({"data": data}, indent=2)
    return Response(final, status=201)

def show (id_user, id_folder):
    """
    

    """ 
    try:
        user = User.with_id(id_user)
        if not user:
            return Response('The user dont exist', status=400)
        folder = Folder.with_id(id_folder)
    except:
        return Response(status=500)
    
    data = []
    data.append({
        "folder_id": folder.id,
        "name": folder.name,
        })

    final = json.dumps({"folders": data,"items": len(data)}, indent=2, ensure_ascii=False)
    return Response(final, mimetype='application/json')
