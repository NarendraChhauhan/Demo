import requests


def query_llama(eligibility_criteria, user_details):
    
    system_prompt = """
You are an exact-match scholarship eligibility validator. Your task is to compare the user's profile against the criteria field-by-field. 
Return ONLY `true` if ALL these fields match exactly:  
- Course  
- Class  
- Category  
- Gender  
- State  
- Country  
- Family Income (must be ≤ specified threshold)  
- Previous Performance (must meet minimum)  
- Age (must be within range)  

Rules:  
1. Ignore any extra information in the user profile.  
2. If any field which is in scholarship but not present in user profile but matches all other then say true.  
3. Respond with EXACTLY one word: `true` or `false`. 
4. If some info is not present in user profile ignore it and answer on the basis of given information only 
"""

    prompt = f"""
    Eligibility Criteria: {eligibility_criteria}
    User Profile: {user_details}
    Is the user eligible? Answer strictly `true` or `false`.
"""

    payload = {
    "model": "deepseek-r1:1.5b",
    "system": system_prompt,
    "prompt": prompt,
    "stream": False,
    
}
    
    response = requests.post('http://localhost:11434/api/generate', json=payload)
    response_data = response.json()  # Parse JSON response

    if response.status_code == 200:
        model_output = response_data.get("response", "").strip()
        print("Raw model output:", model_output)
        
        # Clean the output (ensure it's lowercase and matches "true"/"false")
        if model_output.lower() in ("true", "false"):
            return model_output.lower() == "true"
        else:
            print("Model failed to follow instructions. Output:", model_output)
            return False
    else:
        print("API Error:", response_data)
        return False



