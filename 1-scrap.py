import requests
from bs4 import BeautifulSoup
import json
import time
import urllib.parse



import sys
import codecs

# Set the default encoding to UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

queries = {
    "اﻷخﻼق الحميدةُ (Good Quotes)": [
        "اﻹعراض عنَ الجاهِلينُ", "اﻻعتِدالُ والوسَطيﱠةُ", "اﻹصﻼحُ", "اﻹحسان إلىِ الغَيرُ",
        "اﻻحترامُ والتوقيرﱡ", "البِرُ", "اﻹيثارُ", "اﻹنصاتُ", "اﻷمانةُ", "اﻷُلفةُ", "التعاونُ",
        "التضحيةُ", "التثبت", "التأنِّي (اﻷناة)", "البشاشةُ", "التوددُ", "التواضعُ", 
        "التواصي بالخيرُ", "التفاؤلُ", "التغافلِ", "حُسنِ الظنُ", "حسن السمتُ", 
        "الحذرُ واليقظةُ والحَيطةُ", "الجودُ، الكرمُ، السخاءُ، البذلُ", "الجديَّةُ والحزمُ", 
        "الحياءُ", "الحِلمُ", "الحكمةُ", "حِفظِ اللسانُ", "حُسن العِشرةِ والجوارُ", 
        "السكينةُ", "السترُ", "الزهد فيما في أيدي الناسُ", "الرفقُ", "الرحمةُ", "الشكرُ", 
        "الشفقةُ", "الشجاعةُ", "السماحةُ", "الصمتُ", "الصِّلةُ والتواصلُ", "الصدقُ", "الصبرُ", 
        "الشهامةُ", "العفوُ والصفحُ", "العفةُ", "العزمُ والعزيمةُ وعلوِ الهمةُ", "العزةُ", 
        "العدلُ والإنصافُ", "القناعةُ", "الفطنةُ والذكاءُ", "الفصاحةُ", "الفراسةُ", 
        "الغيرةُ", "المداراةُ", "المحبةُ", "كظمِ الغيظُ", "كتمان السرُ", "القوةُ", 
        "النشاطُ", "النزاهةُ", "المواساةُ", "المزاحُ", "المروءةُ", "الوفاءُ", "الورعُ", 
        "النظافةُ", "النصيحةُ", "النصرةُ", "الوقارُ والرزانة"
    ],
    "اﻷخﻼق المذمومةُ(Bad Quotes)": [
        "الإطراءُ والمدحُ", "الإسرافُ والتبذيرُ", "الإساءةُ", "الاختلافُ والتنازعُ", 
        "الأثرةُ والأنانيةُ", "البخلُ والشحُ", "الانتقامُ", "إفشاء السرُ", "الإفراطُ", 
        "الافتراءُ والبهتانُ", "التسرعُ والتهورُ والعجلةُ", "التخاذلُ", "التجسسُ", "البغضُ والكراهيةُ", 
        "البطرُ", "التقليدُ والتبعيةُ", "التفريطُ", "التعصبُ", "التعسيرُ", "التعاليُ", 
        "الجزعُ", "الجدالُ والمراءُ", "الجبنُ", "الثرثرةُ", "التنابزُ بالألقابُ", "الخداعُ", 
        "الخبثُ", "الحقدُ", "الحسدُ", "الجفاءُ", "الذلُ", "الدِياثةُ", "الخيانةُ", 
        "خلف الوعدُ", "الخِذلانُ", "سوء الجوارُ", "السفهُ والحُمقُ", "السخريةُ والاستهزاءُ", 
        "السبُ والشتمُ", "رفع الصوتُ", "الظلمُ", "الطمعُ", "الشماتةُ", "الشراهةُ", 
        "سوء الظنُ", "الغشُ", "الغدرُ ونقض العهدُ", "العدوانُ", "العُجبُ", "العبوسُ", 
        "الفُحشُ والبذاءةُ", "الفجورُ", "الغيبةُ", "الغلظةُ والقسوةُ والفظاظةُ", "الغضبُ", 
        "اللؤمُ والخسةُ والدناءةُ", "اللامبالاةُ", "الكسلُ والفتورُ", "الكذبُ", "الكبرُ", 
        "نكران الجميلُ", "النفاقُ", "المنُ", "المكرُ والكيدُ", "المداهنةُ", 
        "اليأسُ والقنوطُ والإحباطُ", "الوهنُ", "الهمزُ واللمزُ", "الهجرُ", "النميمةُ"
    ]
}

def search_web(query):
    encoded_query = urllib.parse.quote(query)
    search_url = f"https://www.google.com/search?q={encoded_query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        print(f"Sending request to: {search_url}")
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        
        print(f"Response status code: {response.status_code}")
        print(f"Response content length: {len(response.text)}")
        
        soup = BeautifulSoup(response.text, "html.parser")
        print(f"Number of 'a' tags found: {len(soup.find_all('a'))}")
        print(f"Number of 'div.yuRUbf' found: {len(soup.select('div.yuRUbf'))}")
        
        search_results = []
        for index, result in enumerate(soup.select("div.yuRUbf"), 1):
            print(f"\nAnalyzing result {index}:")
            print(result.prettify())  # Print the entire content of the div
            
            a_tag = result.find('a')
            if a_tag and 'href' in a_tag.attrs:
                link = a_tag['href']
                search_results.append(link)
                print(f"Found link: {link}")
            else:
                print("No valid link found in this result")

        return search_results[:3]

    except requests.exceptions.RequestException as e:
        print(f"Error searching for {query}: {e}")
        return []
    
def collect_websites():
    collected_websites = {}

    for class_name, behaviors in queries.items():
        collected_websites[class_name] = {}

        for behavior in behaviors:
            print(f"Searching for: حكم وأقوال عربية في {behavior}")
            query = f"حكم وأقوال عربية في {behavior}"
            top_websites = search_web(query)
            collected_websites[class_name][behavior] = top_websites

            print(f"Found {len(top_websites)} websites for {behavior}")
            time.sleep(2)

    with open('collected_websites.json', 'w', encoding='utf-8') as f:
        json.dump(collected_websites, f, ensure_ascii=False, indent=4)

    print("Websites collected and saved to 'collected_websites.json'.")

if __name__ == "__main__":
    collect_websites()