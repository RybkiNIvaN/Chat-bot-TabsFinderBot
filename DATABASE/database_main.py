from database_models import *
import os
import config
with db:
    db.create_tables([Tab, Collection, User])


def add_user(name, user_id) -> None:
    with db:
        if name != None:
            try:
                query = User.select().where((User.name == name) &
                                            (User.user_id == user_id))
                print(query[0])
            except Exception as no_in_users:
                add = User(name=name,
                           user_id=user_id
                           )
                add.save()
                print('in query 2 ')
        else:
            try:
                query = User.select().where((User.user_id == user_id))
                print(query[0])
            except Exception as no_in_users:
                add = User(name='None',
                           user_id=user_id
                           )
                add.save()
                print('in query 2 ')


def create_tabs_table() -> None:
    with db:
        os.chdir(config.path_tabs)

        path_tabs = os.getcwd()


        for letter_number in os.listdir(path_tabs):
            os.chdir(path_tabs)
            if letter_number.isdigit():
                os.chdir(os.path.join(path_tabs, letter_number))
                path_letter_number = os.getcwd()
                for groups in os.listdir(path_letter_number):
                    os.chdir(os.path.join(path_tabs, letter_number))
                    os.chdir(os.path.join(os.getcwd(), groups))
                    path_groups = os.getcwd()
                    for songs in os.listdir(path_groups):
                        Tab(groups=groups,
                            song=songs,
                            path=path_groups
                            ).save()


def get_from_tabs_table(t_groups, t_song) -> str:
    with db:
        print("in QUERY ")
        print('g1', t_groups, t_song)
        try:
            query = Tab.select().where((Tab.groups == t_groups) &
                                       (Tab.song == t_song)
                                       )
            print('g2', query[0])
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

        return query[0]


def add_to_collection_table_from_send(user_id: str,
                                      file_song: str,
                                      file_id: str,
                                      sent) -> str:
    with db:

        try:
            print('in func')
            query_s = Collection.select().where((Collection.song == file_song) &
                                                (Collection.user_id == user_id)
                                                )
            print(f'По запросу {query_s[0]}')
            print('Уже в коллекции')
            return 'in collection'
        except Exception as no_in_collection:
            add = Collection(tab_id=file_id, user_id=user_id, song=file_song, sent=sent)
            add.save()
            return 'not in collection'


def add_to_collection_table_from_tabs(user_id: str,
                                      group: str,
                                      file_song: str,
                                      sent) -> str:
    with db:
        print('a1', user_id, group, file_song)
        id_from_tabs = get_from_tabs_table(group, file_song)
        print('a2', id_from_tabs)

        try:
            query = Collection.select().where((Collection.tab_id == id_from_tabs) &
                                              (Collection.user_id == user_id))
            print(f'По запросу {query[0]}')
            print('Уже в коллекции')
            return 'in collection'
        except Exception as no_in_collection:
            add = Collection(tab_id=id_from_tabs,
                             user_id=user_id,
                             song=file_song,
                             sent=sent
                             )
            add.save()
            return 'not in collection'


def elements_of_collection(user_id, category) -> list | int:
    with db:
        query = Collection.select().where((Collection.user_id == user_id))
        all_files = []
        for val in query:
            all_files.append(val.song)
        print('el_1', all_files)
        if category == 'ShowAll':
            return all_files

        if category == 'AmountOfFiles':
            return len(all_files)


def open_file_from_collection(user_id, file_name) -> str:
    with db:

        query_s = Collection.select().where(
            (Collection.user_id == user_id) &
            (Collection.song == file_name)
        )
        res = ''
        for val in query_s:
            print('1', val.sent)
            res = val.sent
        if res == 1:
            return config.path_sent
        query1 = Collection.select().where((Collection.user_id == user_id) &
                                           (Collection.song == file_name)
                                           )
        res = ''
        for val in query1:
            res = val.tab_id
        query2 = Tab.select(Tab.path).where(Tab.id == res)
        for val in query2:
            res = val.path
        print(res)
        return res


# add_user('RybkiN_I', '5110620740')
# res = elements_of_collection('RybkiN_I', 'ShowAll')
#print(open_file_from_collection('5110620740', 'dobraya_pesnya.gp5'))
#create_tabs_table()

print("OK")
