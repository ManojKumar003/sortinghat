import re
class DataProcessing():
    def data_pre_processing(self,input_data):
        """
            This method does all the pre-processing/cleanup of the data.
            input_data: (string_type): Given input data
        """
        student_id_boarding_map = dict()
        input_data = input_data.strip()    # Removes the extra spaces from both start and end postion
        data_list = input_data.split('\n') # Spliting the data with new line operator
        data_list = data_list[1:-1:1]      # Storing data excluding 'init12' and 'fin'
        final_list = []
        for ele in data_list:
            final_list.append(ele.strip())
        self.checking_data(final_list)
        # Below logic will remove the student data with duplicate roll number and roll number more than 4 digits
        # As per other rules in the assignment
        for std_id in final_list:
            if std_id.split(' ')[1] not in student_id_boarding_map:
                student_id_boarding_map[std_id.split(' ')[1]] = std_id
        return student_id_boarding_map.values()
    @staticmethod
    def checking_data(data_list):
        """
             This method does the checking of data format of given input data.
             data_list: (list_type): Given input data
        """
        for data in data_list:
            char = data.split(' ')
            if not re.match('reg', char[0], re.I):  # Checks if 'reg' is given or not
                raise ValueError("Data format is not correct or reg is missing value:", data)
            if not re.match("\d{1,4}$", char[1]):  # Checks number of digits of roll number
                raise ValueError("Data format is not correct for roll number or is missing value:", data)
            if not re.match("A|B", char[2], re.I):  # Checks class of A or B
                raise ValueError("Data format is not correct for class A|B or is missing value:", data)
            if not re.match("NV|V", char[3], re.I):  # Checks food option as V or NV
                raise ValueError("Data format is not correct for food V|NV or is missing value:", data)
        return # As the data format is correct so returing back