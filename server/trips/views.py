from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def calculate_trip(request):
    data = request.data

    miles = float(data.get("miles", 0))
    driving_hours = miles / 60
    rest_hours = 1
    total_hours = driving_hours + rest_hours

    return Response({
        "current": data.get("current"),
        "pickup": data.get("pickup"),
        "dropoff": data.get("dropoff"),
        "miles": round(miles, 2),
        "driving_hours": round(driving_hours, 2),
        "rest_hours": rest_hours,
        "total_hours": round(total_hours, 2),
        "cycle_used": float(data.get("cycle_used", 0)),
    })
