import random
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class FlightSearchInput(BaseModel):
    origin: str = Field(..., description="Departure city or airport code (e.g. 'Paris' or 'CDG')")
    destination: str = Field(..., description="Destination city or airport code (e.g. 'Tokyo' or 'NRT')")
    date: str = Field(..., description="Travel date in YYYY-MM-DD format")


class FlightSearchTool(BaseTool):
    name: str = "Flight Search Tool"
    description: str = (
        "Searches for available flights between two cities on a given date. "
        "Returns a list of flight options with airline, times, duration, stops, and price."
    )
    args_schema: Type[BaseModel] = FlightSearchInput

    def _run(self, origin: str, destination: str, date: str) -> str:
        airlines = ["Air France", "Emirates", "Lufthansa", "Turkish Airlines", "Qatar Airways", "British Airways"]
        results = []

        for i in range(random.randint(3, 5)):
            airline = random.choice(airlines)
            dep_hour = random.randint(5, 22)
            dep_min = random.choice([0, 15, 30, 45])
            duration_h = random.randint(2, 14)
            duration_m = random.choice([0, 20, 40])
            arr_hour = (dep_hour + duration_h) % 24
            arr_min = (dep_min + duration_m) % 60
            stops = random.choice([0, 0, 1, 1, 2])
            stop_label = "Non-stop" if stops == 0 else f"{stops} stop(s)"
            price = random.randint(200, 1800)
            flight_number = f"{airline[:2].upper()}{random.randint(100, 999)}"

            results.append(
                f"  - Flight {flight_number} | {airline}\n"
                f"    Departure: {dep_hour:02d}:{dep_min:02d}  →  Arrival: {arr_hour:02d}:{arr_min:02d}\n"
                f"    Duration: {duration_h}h {duration_m:02d}m | {stop_label}\n"
                f"    Price: ${price} per person\n"
            )

        header = f"Available flights from {origin} to {destination} on {date}:\n\n"
        return header + "\n".join(results)
