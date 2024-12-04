# from django.core.exceptions import PermissionDenied

# class UserIsAdminMixin():
#     # Выполняет проверку. будет возвращаться True в случае, если совпадает user_id с админом.
#     def has_permission(self):
#         return self.get_object().user == self.request.user.is_staff
#     def dispatch(self, request, *args, **kwargs):
#         if not self.has_permission():
#             raise PermissionDenied 
#         return super().dispatch(request, *args, **kwargs)