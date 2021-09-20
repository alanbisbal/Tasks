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

    final = json.dumps({"folder": data, "items": len(data)}, indent=2, ensure_ascii=False)
    return Response(final, mimetype='application/json')

