import requests


def es_dia_festivo(fecha, pais='EC'):
    año = fecha.year
    url = f"https://date.nager.at/api/v3/PublicHolidays/{año}/{pais}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dias_festivos = response.json()
        
        for festivo in dias_festivos:
            if festivo['date'] == fecha.strftime('%Y-%m-%d'):
                return True, festivo['name']
        
        return False, None
    except requests.RequestException:
        return False, None