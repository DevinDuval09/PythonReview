import os
import os.path
import pathlib


class Os_Directory():

    def __init__(self):
        self.cd = os.getcwd()
        self.files = [f for f in os.listdir(self.cd)]

    def get_wd(self, header='Files in '):
        '''get list of files in the current working directory'''
        return header + "{}:\n".format(self.cd)
        + "\n".join(['{}: {}'.format(*tup) for tup in enumerate(self.files)])

    def os_copy_text(self):
        file_name = str(self.files[int(input(
                        self.get_wd(header="Select a file from ") + '\n:'))])
        new_path = input('Enter target directory:')
        print(new_path)
        with open(file_name, 'r') as file_source,\
                open(new_path + '\\' + file_name, 'w') as file_copy:
            file_copy.write(''.join(file_source.readlines()))
            file_copy.close()

    def pwd(self):
        print(self.get_wd())



