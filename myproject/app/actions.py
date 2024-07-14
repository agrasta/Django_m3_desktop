 # myapp/actions.py
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow, BaseEditWindow
from django.contrib.auth.models import ContentType, User, Group, Permission
from m3_ext.ui import all_components as ext

class PermissionAddEditWindow(BaseEditWindow):
    def _init_components(self):
        super(PermissionAddEditWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label='Name',
            name='name',
            anchor='100%',
            allow_blank=False
        )

        self.field__codename = ext.ExtStringField(
            label='Codename',
            name='codename',
            anchor='100%',
            allow_blank=False
        )

        self.field__content_type = ext.ExtDictSelectField(
            label='Content Type',
            name='content_type_id',
            anchor='100%',
            pack='app.actions.ContentTypePack'
        )

    def _do_layout(self):
        super(PermissionAddEditWindow, self)._do_layout()

        self.form.items.extend([
            self.field__name,
            self.field__codename,
            self.field__content_type,
        ])

    def set_params(self, params):
        super(PermissionAddEditWindow, self).set_params(params)
        self.title = 'Permission: Редактирование'
        self.height = 'auto'

class ContentTypeAddEditWindow(BaseEditWindow):
    def _init_components(self):
        super(ContentTypeAddEditWindow, self)._init_components()

        self.field__app_label = ext.ExtStringField(
            label='App Label',
            name='app_label',
            anchor='100%',
            allow_blank=False
        )

        self.field__model = ext.ExtStringField(
            label='Model',
            name='model',
            anchor='100%',
            allow_blank=False
        )

    def _do_layout(self):
        super(ContentTypeAddEditWindow, self)._do_layout()

        self.form.items.extend([
            self.field__app_label,
            self.field__model,
        ])

    def set_params(self, params):
        super(ContentTypeAddEditWindow, self).set_params(params)
        self.height = 'auto'

class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    add_window = ContentTypeAddEditWindow
    edit_window = ContentTypeAddEditWindow

class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    add_window = PermissionAddEditWindow
    edit_window = PermissionAddEditWindow

    def save_row(self, obj, create_new, request, context):
        data = request.POST.dict()
        content_type_id = data.get('content_type_id')
        if content_type_id:
            obj.content_type_id = int(content_type_id)
        super(PermissionPack, self).save_row(obj, create_new, request, context)


class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    add_window = ModelEditWindow.fabricate(model)
    edit_window = ModelEditWindow.fabricate(model)


class UserAddEditWindow(BaseEditWindow):
    def _init_components(self):
        super(UserAddEditWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label='Username',
            name='username',
            anchor='100%',
            allow_blank=False
        )

        self.field__password = ext.ExtStringField(
            label='Password',
            name='password',
            anchor='100%',
            allow_blank=False
        )

        self.field__email = ext.ExtStringField(
            label='Email',
            name='email',
            anchor='100%',
            allow_blank=False
        )

        self.field__first_name = ext.ExtStringField(
            label='First Name',
            name='first_name',
            anchor='100%',
            allow_blank=True
        )

        self.field__last_name = ext.ExtStringField(
            label='Last Name',
            name='last_name',
            anchor='100%',
            allow_blank=True
        )

        self.field__is_staff = ext.ExtCheckBox(
            label='Staff Status',
            name='is_staff',
            anchor='100%',
            allow_blank=True
        )

        self.field__is_active = ext.ExtCheckBox(
            label='Active',
            name='is_active',
            anchor='100%',
            allow_blank=True
        )

        self.field__is_superuser = ext.ExtCheckBox(
            label='Superuser Status',
            name='is_superuser',
            anchor='100%',
            allow_blank=True
        )

    def _do_layout(self):
        super(UserAddEditWindow, self)._do_layout()

        self.form.items.extend([
            self.field__username,
            self.field__password,
            self.field__email,
            self.field__first_name,
            self.field__last_name,
            self.field__is_staff,
            self.field__is_active,
            self.field__is_superuser,
        ])

    def set_params(self, params):
        super(UserAddEditWindow, self).set_params(params)
        self.height = 'auto'


class UserPack(ObjectPack):
    model = User
    add_to_desktop = True

    add_window = UserAddEditWindow
    edit_window = UserAddEditWindow
