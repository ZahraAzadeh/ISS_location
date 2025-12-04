import requests

ISS_API_URL = "https://api.wheretheiss.at/v1/satellites/25544"
ASTRONAUTS_API_URL = "http://api.open-notify.org/astros.json"


def get_iss_location():
    """Fetch and display the current ISS location."""
    try:
        response = requests.get(ISS_API_URL, timeout=10)
        data = response.json()

        latitude = data["latitude"]
        longitude = data["longitude"]

        print("\n=== Current ISS Location ===")
        print(f"Latitude:  {latitude}")
        print(f"Longitude: {longitude}")

        # OpenStreetMap link
        map_link = (
            f"https://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}"
            f"#map=5/{latitude}/{longitude}"
        )
        print(f"\nMap Link: {map_link}")

    except Exception as e:
        print("Error fetching ISS location:", e)


def get_astronauts():
    """Fetch and display the astronauts currently in space."""
    try:
        response = requests.get(ASTRONAUTS_API_URL, timeout=10)
        data = response.json()

        number = data["number"]
        people = data["people"]

        print("\n=== Astronauts Currently in Space ===")
        print(f"Number of astronauts in space: {number}\n")

        for person in people:
            print(f"- {person['name']} (Spacecraft: {person['craft']})")

    except Exception as e:
        print("Error fetching astronauts info:", e)


def main_menu():
    while True:
        print("\n===== ISS & Astronaut Tracker =====")
        print("1. Show current location of the ISS")
        print("2. Show astronauts currently in space")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            get_iss_location()
            input("\nPress Enter to continue...")

        elif choice == "2":
            get_astronauts()
            input("\nPress Enter to continue...")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main_menu()
