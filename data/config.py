from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = '6267733278:AAFaRgFn5mwdyspPrhMgTaJJMGUZrBmi_cA'  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str('IP')
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
DB_PORT = env.int("DB_PORT")



CHANNELS = ["@Amirjon_Karimov_Blog"]