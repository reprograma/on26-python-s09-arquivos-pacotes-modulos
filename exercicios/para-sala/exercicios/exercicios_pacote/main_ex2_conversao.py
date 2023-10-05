from pacote_conversao import metro_para_pes, quilometros_para_milhas, celcius_para_fahrenheit

print("\n**Metro para Pés**\n")

resultado_metros_pes = metro_para_pes.metro_pes(4)

print(f"\nMetro para pés: {resultado_metros_pes:.2f}pi")

print("\n**Km para Milhas**\n")

resultado_km_milhas = quilometros_para_milhas.km_milha(24)
print(f"\nKm para milhas: {resultado_km_milhas:.2f}mi")

print("\n**Celcius para Fahrenheit**\n")

resultado_celcius_fahrenheit = celcius_para_fahrenheit.celcius_fahrenheit(100)
print(f"\nCelcius para fahrenheit: {resultado_celcius_fahrenheit}°F")