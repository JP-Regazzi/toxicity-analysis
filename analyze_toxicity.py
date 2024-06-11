import json
from googleapiclient import discovery

# Replace this with your API key
API_KEY = 'put-your-key-here'

client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)

def analyze_toxicity(text):
    analyze_request = {
        'comment': {'text': text},
        'requestedAttributes': {'TOXICITY': {}}
    }

    response = client.comments().analyze(body=analyze_request).execute()
    return response

def read_and_analyze_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    results = []
    for line in lines:
        response = analyze_toxicity(line.strip())
        toxicity_score = response['attributeScores']['TOXICITY']['summaryScore']['value']
        results.append({'line': line.strip(), 'toxicity_score': toxicity_score})

    return results

def read_and_analyze_whole_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read().strip()

    response = analyze_toxicity(text)
    toxicity_score = response['attributeScores']['TOXICITY']['summaryScore']['value']
    
    return {'text': text, 'toxicity_score': toxicity_score}

def main():
    file_path = 'test.txt'

    # Analyze each line
    #print("Analyzing each line:")
    #line_analysis_results = read_and_analyze_lines(file_path)
    #for result in line_analysis_results:
    #    print(f"Line: {result['line']}\nToxicity Score: {result['toxicity_score']}\n")

    # Analyze the whole text
    print("Analyzing the whole text:")
    whole_text_analysis_result = read_and_analyze_whole_text(file_path)
    print(f"Whole Text: {whole_text_analysis_result['text']}\nToxicity Score: {whole_text_analysis_result['toxicity_score']}\n")

if __name__ == "__main__":
    main()
