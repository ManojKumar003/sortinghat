import re
from .data_pre_processing import DataProcessing
class SortingHat(DataProcessing):
    """This Class deals with allocation of Boarding Houses to the students as per the given rules"""
    def boarding_house_allocation(self,input_data):
        """
            This method deals with allocation of Boarding Houses to the Students
            input_data: (string_type): Raw Given input data
        """
        # calling data preprocesing method
        student_data = self.data_pre_processing(input_data)
        house_allocation_list = self.mapping_boarding_house(student_data)
        # Checking for overflow secanrio
        capacity=min(len(house_allocation_list[0]), len(house_allocation_list[1]),len(house_allocation_list[2]),
                     len(house_allocation_list[3]))
        final_allocation = self.cheking_overflow(capacity, house_allocation_list)
        return final_allocation

    @staticmethod
    def mapping_boarding_house(student_data):
        """
            This method does mapping of the students to their choosen Boarding Houses
            student_data: (string_type): Processed clean data
        """
        AV = []  # Initialization boarding house with Class A and Food option of V
        BV = []  # Initialization boarding house with Class B and Food option of V
        ANV = [] # Initialization boarding house with Class A and Food option of NV
        BNV = [] # Initialization boarding house with Class B and Food option of NV
        for data in student_data:
            data_list = data.split()
            if re.match(data_list[2], 'A', re.I) and re.match(data_list[3], 'V', re.I):
                AV.append(int(data_list[1]))
            elif re.match(data_list[2], 'B', re.I) and re.match(data_list[3], 'V', re.I):
                BV.append(int(data_list[1]))
            elif re.match(data_list[2], 'A', re.I) and re.match(data_list[3], 'NV', re.I):
                ANV.append(int(data_list[1]))
            else:
                BNV.append(int(data_list[1]))
        return AV,BV,ANV,BNV

    @staticmethod
    def cheking_overflow(capacity, house_full_list):
        """
            This method checks the overflow condition
            house_full_list: (list_type): Boarding House full list
        """
        NA = []  # Initialization overflow array
        while True:
            for house in house_full_list:
                if len(house) != capacity:
                    NA.append(int((house.pop())))
            if (len(house_full_list[0]) == len(house_full_list[1])==len(house_full_list[2])==len(house_full_list[3])
                    ==capacity):
                break
        finall_house_allocation = dict()
        finall_house_allocation['AV'] = house_full_list[0]
        finall_house_allocation['BV'] = house_full_list[1]
        finall_house_allocation['ANV'] = house_full_list[2]
        finall_house_allocation['BNV'] = house_full_list[3]
        finall_house_allocation['NA'] = NA
        return finall_house_allocation
