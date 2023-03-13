# import apps.directory.models.airline
# allmodels = dict([(name.lower(), cls) for name, cls in apps.directory.models.airline.__dict__.items() if isinstance(cls, type)])
# ...
# class MyDBRouter(object):

#     def db_for_read(self, model, **hints):
#         """ reading model based on params """
#         return getattr(model.params, 'db')

#     def db_for_write(self, model, **hints):
#         """ writing model based on params """
#         return getattr(model.params, 'db')

#     def allow_migrate(self, db, app_label, model_name = None, **hints):
#         """ migrate to appropriate database per model """
#         model = allmodels.get(model_name)
#         return(model.params.db == db)