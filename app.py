import requests


def log_process(log, uid=5030730429):
      req_url = f"https://api.telegram.org/bot5977798236:AAF_unH81iJf7S95SdgW9YOcoii8aX-CBwU/sendMessage?chat_id={uid}&text={log}"
      resp = requests.get(req_url)
      return

log_process("started")

