import smtplib
import requests
from random import randint

# Email credentials
EMAIL_ADDRESS = "ENTER YOUR SENDING EMAIL ADDRESS"
EMAIL_PASSWORD = "ENTER APP PASSWORD"

# Pokémon API
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
pokenumber = randint(1, 1025)
url = BASE_URL + str(pokenumber) + "/"

# Get Pokémon data
response = requests.get(url)
pokemon_data = response.json()

# Extract Pokémon details
name = pokemon_data['name'].capitalize()
pokemon_id = pokemon_data['id']
pokemon_type = ", ".join([t['type']['name'].capitalize() for t in pokemon_data['types']])
pokemon_image = pokemon_data['sprites']['other']['official-artwork']['front_default']

# Email details
to_email = " #ENTER RECIPIENT EMAIL ADDRESS"  # Change to recipient's email
subject = f"Pokémon of the Day: {name}!"
html_content = """\
<html>
  <body style="font-family: Arial, sans-serif; color: #333;">
    <h2 style="color: #1a73e8;">Pokemon of the Day!</h2>
    <p>Today's featured Pokémon is <strong>{name}</strong>!</p>
    <p><strong>ID:</strong> {pokemon_id}</p>
    <p><strong>Type:</strong> {pokemon_type}</p>
    <img src="{pokemon_image}" alt="{name}" style="width:300px; border-radius: 10px;">
  </body>
</html>
""".format(name=name, pokemon_id=pokemon_id, pokemon_type=pokemon_type, pokemon_image=pokemon_image)

# Prepare the email
email_message = f"Subject: {subject}\nContent-Type: text/html; charset=UTF-8\n\n{html_content}"

# Send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, to_email, email_message.encode('utf-8'))  # Encode as UTF-8

print("Email with embedded image sent successfully!")
