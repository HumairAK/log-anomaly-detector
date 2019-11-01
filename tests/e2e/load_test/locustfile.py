import uuid
from random import randint

from locust import HttpLocust, TaskSet, task


def generate_form():
    uid = str(uuid.uuid4())
    num = randint(0, 1)
    banana_data = {
        uid + "[id]": "1",
        uid + "[image]": "bananas.jpg",
        uid + "[pname]": "bananas",
        uid + "[pprice]": "5",
        uid + "[pquant]": "1",
        uid + "[ptype]": "fruit",
        uid + "[newQuant]": "1",
    }
    uid = str(uuid.uuid4())
    onion_data = {
        uid + "[id]": "2",
        uid + "[image]": "onions.jpg",
        uid + "[pname]": "onions",
        uid + "[pprice]": "3",
        uid + "[pquant]": "1",
        uid + "[ptype]": "vegetables",
        uid + "[newQuant]": "1"
    }
    data = [onion_data, banana_data]
    return data[num]


class UserBehavior(TaskSet):
    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task(1)
    def place_order(self):
        self.client.post("/mock/orderService", generate_form())


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 250
    max_wait = 250
