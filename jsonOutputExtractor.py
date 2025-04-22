import json

def extract_demographics(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)

    result = []
    faces = data.get("media", {}).get("faces", [])
    
    for face in faces:
        demographics = {"age": None, "race": None, "gender": None}
        confidences = {"age_confidence": None, "race_confidence": None, "gender_confidence": None}

        for tag in face.get("tags", []):
            if tag["name"] in demographics:
                demographics[tag["name"]] = tag["value"]
                confidences[f"{tag['name']}_confidence"] = tag["confidence"]

        result.append({**demographics, **confidences})

    return result

# Example usage:
if __name__ == "__main__":
    paths_to_json = [
        "./output6.json",
        "./output7.json",
        "./output8.json",
        "./output9.json",
        "./output10.json",
        "./output11.json",
        "./output12.json",
        "./output13.json",
        "./output14.json",
        "./output15.json",
        "./output16.json",
        "./output17.json",
        "./output18.json",
        "./output19.json",
        "./output20.json",
        "./output21.json",
        "./output22.json",
        "./output23.json",
        "./output24.json",
        "./output25.json",
        "./output26.json",
        "./output27.json",
        "./output28.json",
        "./output29.json",
        "./output30.json"
    ]
    path = ""
    num = 6
    for path in paths_to_json:
        # Extract demographics from the JSON file
        demographics = extract_demographics(path)
        for idx, entry in enumerate(demographics):
            print(f"Face {num}:")
            print(f"  Age: {entry['age']} (Confidence: {entry['age_confidence']})")
            print(f"  Gender: {entry['gender']} (Confidence: {entry['gender_confidence']})")
            print(f"  Race: {entry['race']} (Confidence: {entry['race_confidence']})")
            num += 1
        print("\n")