from nameko.extensions import DependencyProvider
from twilio.rest import Client


class Twilio(DependencyProvider):
    def __init__(self, **options):
        self.options = options
        self.client = None
        self.sid = None
        self.token = None

    def setup(self):
        config = self.container.config["TWILIO"]
        self.sid = config["SID"]
        self.token = config["TOKEN"]

    def start(self):
        self.client = Client(self.sid, self.token, **self.options)

    def stop(self):
        self.client = None

    def kill(self):
        self.client = None

    def get_dependency(self, worker_ctx):
        return self.client
