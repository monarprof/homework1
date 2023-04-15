import requests
def daily_affirmation():
    daily_affirmation = requests.get('https://www.affirmations.dev')
    daily_quote = daily_affirmation.json()
    print(daily_quote)
    result = f"""From Nara your Daily affirmation: {daily_quote['affirmation']}"""
    return result


def mike_bot(affirmation):
    url = 'https://hooks.slack.com/services/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'
    header = {"Content-type": "application/json"}
    data = '{"text":"%s"}' % affirmation

    daily_affirmation = requests.post (url, headers=header, data=data)
    print(daily_affirmation)
    return daily_affirmation
  
mike_bot(affirmation=daily_affirmation())