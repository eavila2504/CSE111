from unittest import result

from monthly_savings import calculate_monthly_savings, display_results
from pytest import approx
import pytest


def test_calculate_monthly_savings():
    result=calculate_monthly_savings(100, 0.075, 0.13, 3, 0)
    assert result["subtotal"] == approx(300.00, abs=0.01)
    assert result["interest_normal"] == approx(3.77, abs=0.02)
    assert result["interest_frozen"] == approx(0.00, abs=0.01)
    assert result["total_interest"] == approx(3.77, abs=0.01)
    assert result["total_final"] == approx(303.77, abs=0.01)

    result=calculate_monthly_savings(100, 0.075, 0.13, 3, 50)

    assert result["subtotal"] == approx(300.00, abs=0.01)
    assert result["interest_normal"] == approx(1.88, abs=0.01)
    assert result["interest_frozen"] == approx(3.28, abs=0.01)
    assert result["total_interest"] == approx(5.16, abs=0.01)
    assert result["total_final"] == approx(305.16, abs=0.01)

def test_display_results():
    result=display_results(100, 0)
  
    assert "3 months: $303.26" in result
    assert "6 months: $611.48" in result
    assert "9 months: $924.73" in result
    assert "12 months: $1243.10" in result        
   

pytest.main(["-v", "--tb=line", "-rN", __file__])

  

