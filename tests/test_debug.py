import pytest
from debugBuddy import debug

class Tests:
    #Test functions
    
    # jake test units
    def test_debug_hint_default_parameters(self):
        result = debug.debug_hint()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_debug_hint_specific_parameters(self):
        result = debug.debug_hint("syntax", "beginner")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_debug_hint_all_combinations(self):
        issue_types = ["general", "syntax", "logic", "runtime", "performance"]
        experience_levels = ["beginner", "intermediate", "advanced"]
        
        for issue_type in issue_types:
            for level in experience_levels:
                result = debug.debug_hint(issue_type, level)
                assert isinstance(result, str)
                assert len(result) > 0
    
    pass