import json
from collections import defaultdict
from urllib.parse import urlparse


import sys
import codecs

# Set the default encoding to UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())



class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

def analyze_websites(json_file_path, frequency_threshold=2):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        collected_data = json.load(f)

    website_freq = defaultdict(lambda: {'count': 0, 'classes': defaultdict(list)})

    for class_name, behaviors in collected_data.items():
        for behavior, websites in behaviors.items():
            for website in websites:
                domain = urlparse(website).netloc                
                website_freq[domain]['count'] += 1                
                website_freq[domain]['classes'][class_name].append(f"{behavior} + {website}")
    filtered_websites = {domain: data for domain, data in website_freq.items() if data['count'] >= frequency_threshold}
    sorted_websites = sorted(filtered_websites.items(), key=lambda x: x[1]['count'], reverse=True)
    print(f"Common websites (appearing {frequency_threshold} or more times) and their associated classes/meanings:")
    print("="*50)
    for domain, data in sorted_websites:
        print(f"\nWebsite: {domain}")
        print(f"Frequency: {data['count']}")
        print("Associated classes and behaviors:")
        for class_name, urls in data['classes'].items():
            print(f"  {class_name}:")
            for url in urls:
                print(f"    - {url}")
        print("-"*30)

    analyzed_data = {}
    for domain, data in sorted_websites:
        analyzed_data[domain] = {
            'count': data['count'],
            'classes': {class_name: list(urls) for class_name, urls in data['classes'].items()}
        }

    output_file = f'analyzed_websites_with_url_{frequency_threshold}.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analyzed_data, f, cls=SetEncoder, ensure_ascii=False, indent=4)
    
    print(f"\nAnalyzed data has been saved to '{output_file}'")

if __name__ == "__main__":
    analyze_websites('collected_websites.json', 2)
