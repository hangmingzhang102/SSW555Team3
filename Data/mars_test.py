import unittest

def check_planetary_survival(gear_stats, planet_hazards):
    if not (isinstance(gear_stats, dict) and isinstance(planet_hazards, dict)):
        return "Invalid input: must be dictionaries"
    
    for v in gear_stats.values():
        if not isinstance(v, (int, float)) or v < 0:
            return "Invalid gear values"

    for h, t in planet_hazards.items():
        if h not in gear_stats:
            return f"Missing {h} gear"
        if gear_stats[h] < t:
            return f"Insufficient {h} protection"
    
    return "Survival successful"

class TestSurvival(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(
            check_planetary_survival(
                {"temp": 100}, 
                {"temp": 80}
            ), 
            "Survival successful"
        )
    
    def test_missing_gear(self):
        self.assertEqual(
            check_planetary_survival(
                {"temp": 100}, 
                {"radiation": 50}
            ), 
            "Missing radiation gear"
        )
    
    def test_invalid_gear_value(self):
        self.assertEqual(
            check_planetary_survival(
                {"temp": -10}, 
                {"temp": 0}
            ), 
            "Invalid gear values"
        )

if __name__ == '__main__':
    unittest.main()
