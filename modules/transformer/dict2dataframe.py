
class Dict2dataframe:
    """
    Esta clase transforma los datos de un diccionario en una sola trama de datos
    """
    def __init__(self, data_ui: dict) -> None:

        self.data_ui = data_ui

    def transform(self) -> str:

        data_frame = ""

        for row, inf in self.data_ui.items():

            data_frame += inf

        return data_frame

if __name__ == "__main__":

    data = {
        "name": "alberto",
        "lastname": "narro"
    }

    data_frame = Dict2dataframe(data_ui=data)
    print(data_frame.transform())
