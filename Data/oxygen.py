import unittest

def set_oxygen_level_refactored(suit_stats, mission_params):
    OXYGEN_USAGE_RATE = 0.8
    
    def _validate_input_types():
        return isinstance(suit_stats, dict) and isinstance(mission_params, dict)
    
    def _validate_oxygen():
        return 'oxygen' in suit_stats and isinstance(suit_stats['oxygen'], (int, float)) and suit_stats['oxygen'] >= 0
    
    def _validate_mission_params():
        return (
            'duration' in mission_params and 
            'crew' in mission_params and 
            isinstance(mission_params['duration'], (int, float)) and 
            mission_params['duration'] > 0 and 
            isinstance(mission_params['crew'], int) and 
            mission_params['crew'] > 0
        )
    
    if not _validate_input_types():
        return "Invalid input: must be dictionaries"
    
    if not _validate_oxygen():
        return "Missing oxygen stat" if 'oxygen' not in suit_stats else "Invalid oxygen value"
    
    if not _validate_mission_params():
        missing = 'duration' not in mission_params or 'crew' not in mission_params
        return "Missing mission parameters" if missing else "Invalid mission parameters"
    
    oxygen_required = mission_params['duration'] * mission_params['crew'] * OXYGEN_USAGE_RATE
    return "Oxygen level sufficient" if suit_stats['oxygen'] >= oxygen_required else "Insufficient oxygen for mission"

class TestOxygenLevelRefactored(unittest.TestCase):
    def test_sufficient_oxygen(self):
        self.assertEqual(
            set_oxygen_level_refactored({'oxygen': 100}, {'duration': 10, 'crew': 10}),
            "Oxygen level sufficient"
        )
    
    def test_insufficient_oxygen(self):
        self.assertEqual(
            set_oxygen_level_refactored({'oxygen': 50}, {'duration': 10, 'crew': 10}),
            "Insufficient oxygen for mission"
        )
    
    def test_invalid_input_type(self):
        self.assertEqual(
            set_oxygen_level_refactored([], {}), 
            "Invalid input: must be dictionaries"
        )
    
    def test_missing_oxygen(self):
        self.assertEqual(
            set_oxygen_level_refactored({}, {'duration': 10, 'crew': 2}),
            "Missing oxygen stat"
        )
    
    def test_invalid_oxygen_value(self):
        self.assertEqual(
            set_oxygen_level_refactored({'oxygen': -5}, {'duration': 10, 'crew': 2}),
            "Invalid oxygen value"
        )
    
    def test_missing_mission_param(self):
        self.assertEqual(
            set_oxygen_level_refactored({'oxygen': 50}, {'duration': 10}),
            "Missing mission parameters"
        )
    
    def test_invalid_duration(self):
        self.assertEqual(
            set_oxygen_level_refactored({'oxygen': 50}, {'duration': -10, 'crew': 2}),
            "Invalid mission parameters"
        )
    
    def test_invalid_crew(self):
        self.assertEqual(
            set_oxygen_level_refactored({'oxygen': 50}, {'duration': 10, 'crew': 0}),
            "Invalid mission parameters"
        )

if __name__ == '__main__':
    unittest.main()
