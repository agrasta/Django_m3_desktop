from objectpack import desktop
from django.conf.urls import url
from .controller import controller
from .actions import ContentTypePack, PermissionPack, UserPack, GroupPack

def dict_view(request):
        return dict_controller.process_request(request)

def register_urlpatterns():
    return [url(*controller.urlpattern)]

def register_actions():
    controller.packs.extend([
        ContentTypePack(),
        PermissionPack(),
        UserPack(),
        GroupPack()
    ])

def register_desktop_menu():
    desktop.uificate_the_controller(
        controller,
        menu_root=desktop.MainMenu.SubMenu('Demo')
    )
