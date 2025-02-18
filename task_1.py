class SocialNetwork:
    """Базовый класс социальной сети"""

    def __init__(self, profiles_base: dict = None, admins_base: list = None, black_list: list = None):
        '''
        Конструктор класса

        :param profiles_base: словарь, содержащий в себе данные профилей пользователей в формате "ник:пароль"
        :param admins_base: список, содержащий в себе информацию ники администраторов социальной сети
        :param black_list: список заблокированных пользователей
        '''

        #Использован тип protected атрибута для того, чтобы разработчик не имел соблазна работать напярмую с базой пользователей
        self._profiles_base = profiles_base if profiles_base else dict()
        #Использован тип protected атрибута для того, чтобы гарантировать корректное значение числа пользователей
        self._users_count = len(self._profiles_base.keys())
        self.admins_base = admins_base if admins_base else list()
        self.black_list = black_list if black_list else list()


    def registry(self, nickname: str, password: str) -> bool:
        '''
        Регистрация нового пользователя в социальной сети
        :param nickname: имя пользователя
        :param password: пароль
        :return: True если пользователь успешно зарегистрирован, иначе False
        '''

        if nickname in self._profiles_base.keys():
            #Пользователь с заданным никнеймом уже есть в базе
            return False

        #Проверка сложности пароля...

        self._profiles_base[nickname] = password
        self._users_count += 1
        return True


    def block_user(self, user_nick: str, admin_nick: str) -> bool:
        '''
        Блокировка пользователя.
        :param user_nick: ник пользователя, которого требуется заблокировать
        :param admin_nick: ник администратора, который выполняет блокировку
        :return: True в случае успешного выполнения операции, иначе False
        '''

        #Проверка, что пользователь, выполняющий блокировку действительно администратор...
        if admin_nick in self.admins_base:
            self.black_list.append(user_nick)
            return True

        return False


    def unblock_user(self, user_nick: str, admin_nick: str) -> bool:
        '''
        Блокировка пользователя.
        :param user_nick: ник пользователя, которого требуется разблокировать
        :param admin_nick: ник администратора, который выполняет разблокировкублокировку
        :return: True в случае успешного выполнения операции, иначе False
        '''

        #Проверка, что пользователь, выполняющий разблокировку действительно администратор...
        if admin_nick in self.admins_base and user_nick in self.black_list:
            self.black_list.remove(user_nick)
            return True

        return False


    def login(self, nickname: str, password: str) -> bool:
        '''
        Осуществление пользователем входа в социальную сеть
        :param nickname: логин
        :param password: пароль
        :return: True в случае успешного выполнения операции, иначе False
        '''

        if nickname not in self.black_list and (nickname, password) in self._profiles_base.items():
            return True

        return False


    @property
    def users_count(self):
        return self._users_count


    def __str__(self):
        return "Класс, реализующий функционал социальной сети"


    def __repr__(self):
        return f"{self.__class__.__name__}(profiles_base={self._profiles_base}, admins_base={self.admins_base}, black_list={self.black_list})"



class RuTube(SocialNetwork):
    """Класс, описывающей социальную сеть (видеохостинг)"""

    def __init__(self, profiles_base: dict = None, admins_base: list = None, black_list: list = None, video_base: dict = None):
        '''
        Конструктор класса

        :param profiles_base: словарь, содержащий в себе данные профилей пользователей в формате "ник:пароль"
        :param admins_base: список, содержащий в себе информацию ники администраторов социальной сети
        :param black_list: список заблокированных пользователей
        :param video_base: словарь, содержащий информацию о загруженных видео в формате "ник_фавтора: {url:название}"
        '''

        super().__init__(profiles_base, admins_base, black_list)
        #Использован атрибут типа protected, чтобы оградить разработчика от прямого взаимодействия с базой видео
        self._video_base = video_base if video_base else dict()


    def upload(self, video_name: str, source_to_file: str, author_nick:str) -> bool:
        """
        Загруpзка видео на хостинг
        :param video_name: название ролика
        :param source_to_file: путь до фалйа
        :param author_nick: имя пользователя, загрузившего видео
        :return: True в случае успешного выполнения операции, иначе False
        """
        #Генерация ссылки и добавление ролика в базу видео


    def delete_video(self, video_name: str) -> bool:
        """
        Удаление видеоролика с хостинга
        :param video_name: название ролика
        :return: True в случае успешного выполнения операции, иначе False
        """
        #Проверка принадлежности пользователя к запрашиваемому на удаление материалу
        #Удаление видеоролика в случае прохождения всех проверок


    def block_user(self, user_nick: str, admin_nick: str) -> bool:
        '''
        Блокировка пользователя. (Метод перегружен, так как помимо блокировки самого пользователя необходимо удалить все загруженные им видео)
        :param user_nick: ник пользователя, которого требуется заблокировать
        :param admin_nick: ник администратора, который выполняет блокировку
        :return: True в случае успешного выполнения операции, иначе False
        '''


    def __repr__(self):
        return f"{self.__class__.__name__}(profiles_base={self._profiles_base}, admins_base={self.admins_base}, black_list={self.black_list}, video_base={self._video_base})"



if __name__ == "__main__":
    pass
