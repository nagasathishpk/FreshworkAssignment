import json
import os




class KeyValue:

    def __init__(self,path="data.json"):
        if(path=="data.json"):
            self.file_path=path
            self.Open()
        else:
            self.file_path=path
            file_location=os.path.dirname(path)
            if not os.path.exists(file_location):
                os.makedirs(file_location)
            if not os.path.isfile(self.file_path):
                self.Open()
    
    def Open(self):
        with open(self.file_path, 'w') as f:
            json.dump({},f)
    

    def Create(self,input_data):
        with open(self.file_path,'r+') as f:
            data= json.load(f)
            data.update(input_data)
        with open(self.file_path,'w') as f:
            json.dump(data,f)
        return data


    def read(self,input_data):
        with open(self.file_path,'r') as f:
            data = json.load(f)
            if(input_data in data):
                return data[input_data]
            else:
                raise KeyError(f"ERROR:  {input_data} is INVALID KEY")

    def delete(self,input_data):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            if(input_data in data):
                del data[input_data]
                with open(self.file_path,'w') as f:
                    json.dump(data,f)
                return data
            else:
                raise KeyError(f"ERROR:  {input_data} is INVALID KEY")