from django.shortcuts import render, render_to_response

from module_inspect.entity.FileStructureEntity import RudiInspectorFileManager
from module_inspect.service import build_entity_structure


def homepage(request):
    context = {
    }
    return render(request, 'web/homepage.html')


def inspector_home(request):
    path = "/Users/rudi/Project/rudi/rudi_map"
    if 'path' in request.GET:
        path = request.GET['path']

    def get_entity_manager(path):
        entitys = build_entity_structure(path)
        manager = RudiInspectorFileManager(entitys)
        return manager

    inspector_file_manager = get_entity_manager(path)
    ctx = {'entitys': inspector_file_manager.entitys}

    return render_to_response('web/rudi_inspector.html',ctx)
