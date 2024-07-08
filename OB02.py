user_list = []
black_list = []

class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self._access = 'user'

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access(self):
        return self._access

    def set_name(self, name):
        self.__name = name

    def user_data(self):
        about_user = f'ID: {self.__id}\nName: {self.__name}\nAccess level: {self._access}'
        return about_user

class Admin(User):
    def __init__(self, id, name, user_list, black_list):
        super().__init__(id, name)
        self._access = 'admin'
        user_list.append(self)

    def add_user(self, user):
        if user in black_list:
            print(f'User {user.get_name()} is in black list. Try to restore.')
        elif user not in user_list:
            user_list.append(user)
            print(f'Welcome to {user.get_name()}')
        else: print(f'User {user.get_name()} is in users list already')

    def remove_user(self, user):
        if user in user_list:
            black_list.append(user)
            user_list.remove(user)
            print(f'User {user.get_name()} is in black list now!')
        else: print(f'User {user.get_name()} absent in users list')

    def restore_user(self, user):
        if user in black_list:
            user_list.append(user)
            black_list.remove(user)
            print(f'User {user.get_name()} is restored!')
        else: print(f'User {user.get_name()} absent in black list')

    def user_list(self):
        print('Actual users list:')
        for user in user_list: print(user.user_data())

    def black_list(self):
        print('Users in black list:')
        for user in black_list: print(user.user_data())

admin = Admin(1, 'Antonio', user_list, black_list)
user1 = User(2, 'Anfiska')
user2 = User(3, 'Mr. Bond')

print(admin.user_data())
admin.add_user(user1)
admin.add_user(user2)
admin.remove_user(user2)
admin.black_list()
admin.restore_user(user2)
admin.user_list()
user2.set_name('Mr. Good')
admin.user_list()
