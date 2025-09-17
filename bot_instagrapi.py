import os
import time
from instagrapi import Client
from dotenv import load_dotenv

# carrega variáveis do .env
load_dotenv()
USER = os.getenv("INSTA_USER")
PASS = os.getenv("INSTA_PASS")

POST_URL = "https://www.instagram.com/p/DOtbpJPEYDX/"
MESSAGE = "Oi, você passou no teste, parabens, agora você esta QUASE pronto!!!"

cl = Client()
cl.login(USER, PASS)

# pega media_id a partir do link do post
mediapk = cl.media_pk_from_url(POST_URL)
media_id = cl.media_id(mediapk)

# marca comentários já existentes para não responder de novo
seen = set()
for c in cl.media_comments(media_id):
    seen.add(c.pk)

print("🤖 Monitorando comentários... (Ctrl+C para parar)")
while True:
    try:
        comments = cl.media_comments(media_id)
        for c in comments:
            if c.pk not in seen:
                seen.add(c.pk)
                text = c.text.strip().lower()
                username = c.user.username
                print(f"Novo comentário de @{username}: {c.text}")
                if text == "eu quero":
                    user_pk = c.user.pk
                    cl.direct_send(MESSAGE, user_ids=[user_pk])
                    print("DM enviada para", username)
        time.sleep(10)  # espera 10s antes de checar de novo
    except Exception as e:
        print("Erro:", e)
        time.sleep(30)
