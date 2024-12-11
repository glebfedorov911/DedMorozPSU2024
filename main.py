from DedMorozChallenge2024.Calc_distance import geo_distance
import csv


class CSVFileWorker:
    @staticmethod
    def read_file(filename: str) -> list:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)

            return [list(map(float, [r for r in row])) for row in list(reader)[1:]]

    @staticmethod
    def write_file(filename: str, data: list) -> None:
        with open(filename, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file) 
            writer.writerows(data) 

class AlgoDedMorozHouseClasterGifts:
    DED_MOROZ_LATITUDE = 60.7603243
    DED_MOROZ_LONGITUDE = 46.3053893

    def __init__(self, gifts_information: list[list]):
        self.__gifts_information: list = gifts_information
        self.__clusters: list = []
        self.__current_cluster: list = []
        self.__current_weight: int = 0
        self.__current_gift_information: list = self.__get_first_gift()
        self.__num_of_cluster = 1
        self.result: list = []

    def __get_first_gift(self) -> list:
        return self.__gifts_information.pop(0)

    def cluster_gifts(self, max_weight=100) -> None:
        self.__sorted_by_ded_moroz_house()
        self.__algorithm_optimal_delivery()
        self.__convert_cluster_to_valid()

    def __sorted_by_ded_moroz_house(self) -> None:
        self.__gifts_information.sort(key=lambda x: geo_distance(lon1=self.DED_MOROZ_LONGITUDE, lat1=self.DED_MOROZ_LATITUDE, lon2=x[1], lat2=x[2]))

    def __algorithm_optimal_delivery(self) -> None:
        while self.__gifts_information:
            self.__add_new_gift() if self.__is_correct_weight() else self.__add_to_general_cluster()

    def __add_new_gift(self) -> None:
        self.__current_cluster.append(int(self.__current_gift_information[0]))
        self.__append_weight()
        self.__current_gift_information = self.__get_first_gift()

    def __append_weight(self) -> None:
        self.__current_weight += self.__current_gift_information[-1]

    def __is_correct_weight(self) -> bool:
        return self.__current_gift_information[-1] + self.__current_weight < 100
    
    def __add_to_general_cluster(self) -> None:
        self.__clusters.append(self.__current_cluster)
        self.__clear_data()

    def __clear_data(self) -> None:
        self.__current_weight = 0
        self.__current_cluster = []

    def __convert_cluster_to_valid(self) -> None:
        for gift in self.__clusters:
            self.result.append([self.__num_of_cluster, *gift])
            self.__num_of_cluster += 1

if __name__ == "__main__":
    gifts_info = CSVFileWorker.read_file("DedMorozChallenge2024/gifts.csv")
    cg = AlgoDedMorozHouseClasterGifts(gifts_info)
    cg.cluster_gifts()
    CSVFileWorker.write_file("DedMorozChallenge2024Output.csv", cg.result)