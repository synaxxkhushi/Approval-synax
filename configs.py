from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20515794"))
    API_HASH = getenv("API_HASH", "da128bd223a333f5bde8dc1359db4609")
    BOT_TOKEN = getenv("BOT_TOKEN", "6788557765:AAEec6hx56HDjNoZT6oaKrqWmCx3zvaOEdM")
    FSUB = getenv("FSUB", "synaxnetwork")
    CHID = int(getenv("CHID", "-1002132398644"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("mongodb+srv://synaxxkhushi:synaxherebaby@cluster0.vqzfrg0.mongodb.net/?retryWrites=true&w=majority", "")
    
cfg = Config()
