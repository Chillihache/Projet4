import os.path
import json


class Data:

    def __init__(self, data_directory):

        self.data_directory = data_directory

    def get_data(self):

            if os.path.exists(self.data_directory):
                with open(self.data_directory, "r") as file:
                    data = json.load(file)
                    return data
            return None


    def add_in_data(self, data):

        if os.path.exists(self.data_directory):

            with open(self.data_directory, "r") as file:
                existing_data = json.load(file)

            existing_data.append(data)

            with open(self.data_directory, "w") as file:
                json.dump(existing_data, file, indent=4)

        else:

            with open(self.data_directory, "w") as file:
                json.dump([data], file, indent=4)

