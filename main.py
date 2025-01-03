import httpx
import user_agent

url = ("https://qyw-831000.hichina.com/api/sms/sendCode")

payload = {"scene":"YZMDL","mobile":"17313559906"}

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://qyw-831000.hichina.com",
    "pragma": "no-cache",
    "sec-ch-ua": user_agent.generate_user_agent(),
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "version":"1.0.0"
}

for i in range(3):
    response = httpx.post(url, json=payload, headers=headers, verify=False)
    print(response.text)
    if response.status_code == 200:
        continue
    else:
        print(f"Failed to send code, retrying... ({i + 1}/3)")