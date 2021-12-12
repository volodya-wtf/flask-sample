class SessionManager:
    def __init__(self, session):
        self.session = session

    def increment(self, key):
        fetched = self.session.get(key)
        fetched += 1
        self.session[key] = fetched
        self.session.modified = True

    def append(self, key, value):
        fetched = self.session.get(key)
        fetched.append(value)
        self.session[key] = fetched
        self.session.modified = True

    def assign(self, key, value):
        self.session[key] = value
        self.session.modified = True

    def create(self, key, value):
        if self.session.get(key) == None:
            self.session[key] = value
            self.session.modified = True

    def fetch(self, key: str) -> list:
        return self.session.get(key)

    def fetch_last(self, key: str):
        fetched = list(self.session.get(key))
        if fetched:
            return fetched[-1]
        else:
            return None
