import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils.formatters import format_inr
from app.utils.unit_converters import convert_land_to_acre, convert_quintal_to_kg, convert_quintal_to_ton

client = TestClient(app)

def test_unit_converters_and_formatters():
    assert format_inr(150000) == "₹1,50,000"
    assert format_inr(2500) == "₹2,500"
    assert format_inr(0) == "₹0"
    assert convert_land_to_acre(40, "Guntha") == 1.0
    assert convert_quintal_to_kg(1) == 100.0

def test_locations_api():
    res = client.get("/api/v1/locations/districts")
    assert res.status_code == 200
    assert res.json()["total_districts"] == 36

def test_farmer_field_logbook_apis():
    # 0. Farmer login
    res_auth = client.post("/api/v1/crops/auth/login", json={"mobile_number": "9876543210"})
    assert res_auth.status_code == 200
    farmer_id = res_auth.json()["farmer_id"]
    assert farmer_id == "FARMER-9876543210"

    # 1. Farmer registers crop planting
    payload = {
        "farmer_id": farmer_id,
        "crop_type": "Kanda/Onion",
        "land_area": {"value": 2.5, "unit": "Acre"},
        "sowing_date": "2026-07-01"
    }
    res = client.post("/api/v1/crops/register", json=payload)
    assert res.status_code == 201
    crop_id = res.json()["data"]["id"]

    # 2. Farmer logs watering event
    res_wat = client.post("/api/v1/crops/watering-logs", json={
        "crop_id": crop_id,
        "date": "2026-07-15",
        "notes": "Drip irrigation for 4 hours"
    })
    assert res_wat.status_code == 200
    assert len(res_wat.json()["data"]["watering_logs"]) > 0

    # 3. Farmer logs pesticide spray & money spent
    res_pest = client.post("/api/v1/crops/pesticide-logs", json={
        "crop_id": crop_id,
        "date": "2026-07-20",
        "pesticide_name": "Fipronil 5% SC (Regent)",
        "money_spent": 1800,
        "notes": "Sprayed for thrips control"
    })
    assert res_pest.status_code == 200
    assert res_pest.json()["data"]["total_input_cost"] == 1800.0

    # 4. Farmer logs labor work & wages paid
    res_lab = client.post("/api/v1/crops/labor-logs", json={
        "crop_id": crop_id,
        "date": "2026-07-25",
        "worker_count": 4,
        "wages_paid": 1600,
        "notes": "Weeding & top dressing labor"
    })
    assert res_lab.status_code == 200
    assert res_lab.json()["data"]["total_input_cost"] == 1800.0 + 1600.0

    # 5. Farmer logs other farm money needed/spent
    res_oth = client.post("/api/v1/crops/other-expenses", json={
        "crop_id": crop_id,
        "category": "Fertilizer",
        "amount": 3500,
        "notes": "Purchased 4 bags 10:26:26 Mahadhan complex fertilizer",
        "date": "2026-07-28"
    })
    assert res_oth.status_code == 200
    assert res_oth.json()["data"]["total_input_cost"] == 1800 + 1600 + 3500 # 6900

def test_mandi_prices_api():
    res = client.get("/api/v1/mandi-prices")
    assert res.status_code == 200

def test_weather_api():
    res = client.get("/api/v1/weather?taluka_id=tal-niphad")
    assert res.status_code == 200

def test_ai_pest_diagnosis():
    payload = {
        "crop_name": "Kanda/Onion",
        "symptoms_description": "Yellowing leaf tips"
    }
    res = client.post("/api/v1/ai/pest-diagnosis", json=payload)
    assert res.status_code == 200

def test_support_helplines():
    res = client.get("/api/v1/support/helplines")
    assert res.status_code == 200

def test_realtime_agri_news():
    res = client.get("/api/v1/news")
    assert res.status_code == 200
    assert res.json()["data"]["total_news_count"] > 0
    
    res_exp = client.get("/api/v1/news?category=EXPORT_IMPORT")
    assert res_exp.status_code == 200
    assert res_exp.json()["data"]["total_news_count"] > 0

def test_govt_schemes_api():
    res = client.get("/api/v1/schemes")
    assert res.status_code == 200
    assert res.json()["data"]["total_schemes_count"] > 0
    
    res_sub = client.get("/api/v1/schemes?category=STATE_SUBSIDY")
    assert res_sub.status_code == 200
    assert res_sub.json()["data"]["total_schemes_count"] > 0

def test_apmc_markets_api():
    res = client.get("/api/v1/mandi-prices/markets")
    assert res.status_code == 200
    assert res.json()["total_markets"] == 446
    
    res_nashik = client.get("/api/v1/mandi-prices/markets?district=Nashik")
    assert res_nashik.status_code == 200
    assert res_nashik.json()["total_markets"] == 30

def test_mandi_detail_api():
    res = client.get("/api/v1/mandi-prices/detail?mandi_name=Lasalgaon%20APMC")
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["mandi_name"] == "Lasalgaon APMC"
    assert data["total_commodities_traded"] > 0
    assert len(data["crops_prices"]) > 0

def test_root_html_endpoint():
    res = client.get("/")
    assert res.status_code == 200
    assert "text/html" in res.headers.get("content-type", "")
    assert "Krishi Mitra" in res.text or "कृषी मित्र" in res.text




