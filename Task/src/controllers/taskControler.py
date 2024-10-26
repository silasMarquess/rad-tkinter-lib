from ..views.MainForm import *
from ..models.task import Task

class Functions():
    def story(self,TaskObject):
        Task.create(descryption=TaskObject['descryption'],completed=TaskObject['completed'])

    def index(self):
        lista = Task.select();
        return lista

    def delete(self,id):
        task_delete = Task.get_by_id(id);
        task_delete.delete_instance();        
        pass

    def show(self, id):
        task_show = Task.get_by_id(id);
        return task_show;

    def update(self,id,TaskObject):
        task_update = Task.get_by_id(id);
        task_update.completed = TaskObject['completed']
        task_update.descryption = TaskObject['descryption']
        task_update.save();
        pass

    def update_status(self,id,status):
        task_update = Task.get_by_id(id);
        task_update.completed = status
        task_update.save();
        pass

