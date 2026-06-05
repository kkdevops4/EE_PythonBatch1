import requests
import polyline


def get_osrm_route(start_lat, start_lon, end_lat, end_lon):

    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{start_lon},{start_lat};{end_lon},{end_lat}"
        f"?overview=full&geometries=polyline"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if "routes" not in data or not data["routes"]:
            return None

        geometry = data["routes"][0]["geometry"]
        coords = polyline.decode(geometry)

        return [[lon, lat] for lat, lon in coords]

    except Exception as e:
        return None