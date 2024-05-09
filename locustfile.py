from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/token", json={"user":"axxon", "password":"AxxonSoft24#"})
        

    @task
    def guarda_tag(self):
        self.client.post("/guardaTag", 
                         json={"imei": "8297389911", "antena": "A782", "epc": "EPC02", "tid": "85165"}, 
                         headers={"authorization": "Bearer " + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJheHhvbiIsImV4cCI6MTcxNTE0MTIwN30.4XqGVhKCZrJ8wW9AWTFsJILogDz8RbHzx04Rx8EkYb8"},)
