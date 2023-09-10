import csv

def convert_json(json_data, csv_file_path):
    data = json_data["data"]["daily_water_quality_monitoring"]
    
    field_names = [
        "id_pond", "doc", "ph_morning", "ph_evening", "do_morning", "do_evening",
        "tempature_morning", "tempature_evening", "anco_feed_score", "anco_shrimp_number",
        "weather", "water_height", "water_brightness", "water_color", "salinity",
        "death_number", "siphon_hours", "water_circulation", "active_paddle"
    ]
    
    with open(csv_file_path, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        
        writer.writeheader()
        
        for item in data:
            writer.writerow(item)
    
    print(f"CSV file '{csv_file_path}' has been created.")
