import requests

base_url = "https://682d014e4fae1889475497b9.mockapi.io/v1/api/senior-qc-test/booking/places"
r = requests.get(base_url)
if r.status_code == 200:
    data = r.json()
    print(f"Found {len(data)} bookings.")
    for booking in data:
        del_url = f"{base_url}/{booking['id']}"
        del_resp = requests.delete(del_url)
        print(f"Deleted {booking['id']} - Status: {del_resp.status_code}")
    print("Done.")
else:
    print("Failed to fetch bookings:", r.status_code)
