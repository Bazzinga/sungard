import unittest
import requests
import json

class AddCarsTest(unittest.TestCase):
    def setUp(self):
        self.baseurl = 'http://localhost:8000'
        self.headers= {'Content-Type': 'application/json',
                'Accept': 'application/json'}
        self.ids=[]
        self.addurl='/rest/sungard/cars'

    def testAddcars(self):
        cars = [{
            "make":"Hyundai",
            "carmodel":"Elantra",
            "vin":"19hgdjvmnv99"
            },
            {
                "make":"Honda",
                "carmodel":"Civic",
                "vin":"128xnb7e66xbdkj"
                } ]
        for car in cars:
            ret = requests.post(self.baseurl + self.addurl, data = json.dumps(car), headers= self.headers)
            self.assertTrue(ret.status_code==201)
            ret_id = ret.json()['id']
            self.ids.append(ret_id)

    def tearDown(self):
        for car_id in self.ids:
            ret = requests.delete(self.baseurl + self.addurl+'/'+str(car_id),
                                    headers=self.headers) 

class UpdateCarsTest(unittest.TestCase):
    def setUp(self):
        self.baseurl = 'http://localhost:8000'
        self.addurl='/rest/sungard/cars'
        self.headers= {'Content-Type': 'application/json',
                'Accept': 'application/json'}
        self.ids = []
        cars = [{
            "make":"Hyundai",
            "carmodel":"Elantra",
            "vin":"19hgdjvmnv99"
            },
            {
            "make":"Honda",
            "carmodel":"Civic",
            "vin":"128xnb7e66xbdkj"
            }] 
        for car in cars:
            ret = requests.post(self.baseurl + self.addurl, data = json.dumps(car), headers= self.headers)
            try:
                ret_id = ret.json()['id']
                self.ids.append(ret_id)
            except:
                pass

    def testUpdate(self):
        cars = {self.ids[0]:{
            "make":"Hyundai",
            "carmodel":"Elantra",
            "vin":"19hgdjvmnv990000"
            },
            self.ids[1]: {
            "make":"Honda",
            "carmodel":"Civic",
            "vin":"128xnb7e66xbdkj0000"
            }
        }
        for car_id in cars:
            ret = requests.put(self.baseurl + self.addurl+'/'+str(car_id), 
                    data = json.dumps(cars[car_id]), headers= self.headers)
            self.assertTrue(ret.status_code == 200)

    def tearDown(self):
        for car_id in self.ids:
            ret = requests.delete(self.baseurl + self.addurl+'/'+str(car_id),
                                    headers=self.headers) 

class GetCarsTest(unittest.TestCase):
    def setUp(self):
        self.baseurl = 'http://localhost:8000'
        self.addurl='/rest/sungard/cars'
        self.headers= {'Content-Type': 'application/json',
                'Accept': 'application/json'}
        self.ids = []
        cars = [{
            "make":"Hyundai",
            "carmodel":"Elantra",
            "vin":"19hgdjvmnv99"
            },
            {
            "make":"Honda",
            "carmodel":"Civic",
            "vin":"128xnb7e66xbdkj"
            }] 
        for car in cars:
            ret = requests.post(self.baseurl + self.addurl, data = json.dumps(car), headers= self.headers)
            try:
                ret_id = ret.json()['id']
                self.ids.append(ret_id)
            except:
                pass

    def testGet(self):
        for car_id in self.ids:
            ret = requests.get(self.baseurl + self.addurl+'/'+str(car_id), 
                    headers= self.headers)
            self.assertTrue(ret.status_code == 200)

    def tearDown(self):
        for car_id in self.ids:
            ret = requests.delete(self.baseurl + self.addurl+'/'+str(car_id),
                                    headers=self.headers) 
class DelCarsTest(unittest.TestCase):
    def setUp(self):
        self.baseurl = 'http://localhost:8000'
        self.addurl='/rest/sungard/cars'
        self.headers= {'Content-Type': 'application/json',
                'Accept': 'application/json'}
        self.ids = []
        cars = [{
            "make":"Hyundai",
            "carmodel":"Elantra",
            "vin":"19hgdjvmnv99"
            },
            {
            "make":"Honda",
            "carmodel":"Civic",
            "vin":"128xnb7e66xbdkj"
            }] 
        for car in cars:
            ret = requests.post(self.baseurl + self.addurl, data = json.dumps(car), headers= self.headers)
            try:
                ret_id = ret.json()['id']
                self.ids.append(ret_id)
            except:
                pass

    def testDel(self):
        for car_id in self.ids:
            ret = requests.delete(self.baseurl + self.addurl+'/'+str(car_id), 
                    headers= self.headers)
            self.assertTrue(ret.status_code == 204)

    def tearDown(self):
        for car_id in self.ids:
            ret = requests.delete(self.baseurl + self.addurl+'/'+str(car_id),
                                    headers=self.headers) 

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AddCarsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(UpdateCarsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(GetCarsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(DelCarsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

