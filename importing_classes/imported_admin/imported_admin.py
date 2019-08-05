from admin import Admin, Privileges


admin = Admin("john", "sam",)
admin.describe_user()
admin.privileges.show_privileges()