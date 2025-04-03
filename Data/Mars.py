import unittest

def check_planetary_survival(gear_stats, planet_hazards):
    if not isinstance(gear_stats, dict) or not isinstance(planet_hazards, dict):
        return "Invalid input: gear_stats and planet_hazards must be dictionaries"
    
    if not all(isinstance(value, (int, float)) for value in gear_stats.values()):
        return "Invalid input: all gear stats values must be numbers"
    
    if any(value < 0 for value in gear_stats.values()):
        return "Invalid input: all gear stats values must be non-negative"
    
    for hazard, threshold in planet_hazards.items():
        if hazard not in gear_stats:
            return f"Missing gear to handle {hazard}"
        if gear_stats[hazard] < threshold:
            return f"Survival failed: insufficient {hazard} protection"
    
    return "Survival successful"

class TestPlanetaryExploration(unittest.TestCase):
    def test_invalid_input_non_dict(self):
        self.assertEqual(check_planetary_survival("invalid", {"thermal_protection": 100}), "Invalid input: gear_stats and planet_hazards must be dictionaries")
    
    def test_missing_gear_key(self):
        self.assertEqual(check_planetary_survival({"thermal_protection": 100}, {"thermal_protection": 100, "radiation_shield": 50}), "Missing gear to handle radiation_shield")
    
    def test_negative_gear_value(self):
        self.assertEqual(check_planetary_survival({"thermal_protection": -10, "oxygen_supply": 50, "radiation_shield": 20, "pressure_tolerance": 30}, {"thermal_protection": 100}), "Invalid input: all gear stats values must be non-negative")
    
    def test_insufficient_thermal_protection(self):
        self.assertEqual(check_planetary_survival({"thermal_protection": 50, "oxygen_supply": 100, "radiation_shield": 50, "pressure_tolerance": 100}, {"thermal_protection": 100}), "Survival failed: insufficient thermal_protection protection")
    
    def test_successful_survival(self):
        self.assertEqual(check_planetary_survival({"thermal_protection": 150, "oxygen_supply": 200, "radiation_shield": 100, "pressure_tolerance": 300}, {"thermal_protection": 100, "oxygen_supply": 150, "radiation_shield": 50, "pressure_tolerance": 200}),"Survival successful")

if __name__ == '__main__':
    unittest.main()
