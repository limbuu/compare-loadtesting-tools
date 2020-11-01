from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(1, 3)
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        print("*********Start is called************")
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        print("**********End is called***************")
        pass

    host = "http://172.17.0.3:5000"

    @task
    def my_task(self):
        self.client.get("/")