import os

TOKEN = '8791874608:AAHhR0Z36CAOEN_aLvQ-PXM20btxmxL25a0'
ADMIN_IDS = [806709593, 595795530, 1576242455]
PHONE = "+79674317119"
BANK = "Сбербанк"
TEST_GROUP_ID = -1001628595679
GROUP_ID = TEST_GROUP_ID 
ANNOUNCE_TOPIC_ID = 5912
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:Test1TestMafia@db.udhsmhlhzdkzsrwrhalp.supabase.co:5432/postgres"
)
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "https://mafiabot-test-oh6l.onrender.com")