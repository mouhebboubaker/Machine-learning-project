import requests
from bs4 import BeautifulSoup
import json
import csv
import time

mawdoo3_urls = {
    "mawdoo3.com": {
        "count": 157,
        "classes": {
            "اﻷخﻼق الحميدةُ (Good Quotes)": [
                "اﻹحسان إلىِ الغَيرُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D9%81%D8%B9%D9%84_%D8%A7%D9%84%D8%AE%D9%8A%D8%B1",
                "اﻻحترامُ والتوقيرﱡ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A8%D8%B1_%D8%A7%D9%84%D9%88%D8%A7%D9%84%D8%AF%D9%8A%D9%86",
                "البِرُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A8%D8%B1_%D8%A7%D9%84%D9%88%D8%A7%D9%84%D8%AF%D9%8A%D9%86_%D9%82%D8%B5%D9%8A%D8%B1",
                "البِرُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A8%D8%B1_%D8%A7%D9%84%D9%88%D8%A7%D9%84%D8%AF%D9%8A%D9%86",
                "اﻹيثارُ + https://mawdoo3.com/%D9%83%D9%84%D9%85%D8%A7%D8%AA_%D8%B9%D9%86_%D8%A7%D9%84%D8%A5%D9%8A%D8%AB%D8%A7%D8%B1",
                "اﻹنصاتُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D9%85%D8%AA",
                "اﻷمانةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%A3%D9%85%D8%A7%D9%86%D8%A9",
                "اﻷمانةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%A3%D9%85%D8%A7%D9%86%D8%A9",
                "اﻷُلفةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%85%D8%AD%D8%A8%D8%A9_%D8%A8%D9%8A%D9%86_%D8%A7%D9%84%D9%86%D8%A7%D8%B3",
                "التعاونُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D8%B9%D8%A7%D9%88%D9%86",
                "التعاونُ + https://mawdoo3.com/%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D8%B9%D8%A7%D9%88%D9%86",
                "التضحيةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%81%D9%8A_%D8%A7%D9%84%D8%AA%D8%B6%D8%AD%D9%8A%D8%A9_%D9%85%D9%86_%D8%A3%D8%AC%D9%84_%D8%A7%D9%84%D8%A2%D8%AE%D8%B1%D9%8A%D9%86",
                "التضحيةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D9%81%D9%8A_%D8%AD%D8%A8_%D8%A7%D9%84%D9%88%D8%B7%D9%86",
                "التثبت + https://mawdoo3.com/%D9%85%D9%86_%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%A7%D9%84%D8%AD%D9%83%D9%85%D8%A7%D8%A1_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8",
                "التأنِّي (اﻷناة) + https://mawdoo3.com/%D8%A3%D8%AC%D9%85%D9%84_%D8%A7%D9%84%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%A7%D9%84%D8%AD%D9%83%D9%85",
                "البشاشةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D9%88%D9%83%D9%84%D8%A7%D9%85_%D8%AC%D9%85%D9%8A%D9%84",
                "التوددُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D9%85%D8%B9%D8%A8%D8%B1%D8%A9",
                "التواضعُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D9%88%D8%A7%D8%B6%D8%B9",
                "التواضعُ + https://mawdoo3.com/%D8%A3%D8%AC%D9%85%D9%84_%D9%85%D8%A7_%D9%82%D9%8A%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D9%88%D8%A7%D8%B6%D8%B9",
                "التواصي بالخيرُ + https://mawdoo3.com/%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%A3%D8%AE%D9%84%D8%A7%D9%82",
                "التواصي بالخيرُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D8%A8%D8%B1",
                "التفاؤلُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D9%81%D8%A7%D8%A4%D9%84",
                "التفاؤلُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D9%81%D8%A7%D8%A4%D9%84",
                "حُسنِ الظنُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%AD%D8%B3%D9%86_%D8%A7%D9%84%D8%B8%D9%86",
                "حُسنِ الظنُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D9%81%D9%8A_%D8%B3%D9%88%D8%A1_%D8%A7%D9%84%D8%B8%D9%86",
                "الجودُ، الكرمُ، السخاءُ، البذلُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%83%D8%B1%D9%85",
                "الجودُ، الكرمُ، السخاءُ، البذلُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%83%D8%B1%D9%85",
                "الجديَّةُ والحزمُ + https://mawdoo3.com/%D8%A3%D8%AC%D9%85%D9%84_%D8%A7%D9%84%D8%AD%D9%83%D9%85_%D9%88_%D8%A7%D9%84%D8%B9%D8%A8%D8%B1_%D9%81%D9%8A_%D8%A7%D9%84%D8%AD%D9%8A%D8%A7%D8%A9",
                "الحياءُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AD%D9%8A%D8%A7%D8%A1",
                "الحِلمُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%AA%D8%AD%D9%82%D9%8A%D9%82_%D8%A7%D9%84%D8%A3%D8%AD%D9%84%D8%A7%D9%85",
                "الحكمةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9",
                "الحكمةُ + https://mawdoo3.com/%D8%A7%D8%AC%D9%85%D9%84_%D8%A7%D9%84%D8%AD%D9%83%D9%85_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9",
                "حِفظِ اللسانُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%AD%D9%81%D8%B8_%D8%A7%D9%84%D9%84%D8%B3%D8%A7%D9%86",
                "حِفظِ اللسانُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%AD%D9%81%D8%B8_%D8%A7%D9%84%D9%84%D8%B3%D8%A7%D9%86",
                "حُسن العِشرةِ والجوارُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%AC%D8%A7%D8%B1",
                "السكينةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9_%D8%AC%D9%85%D9%8A%D9%84%D8%A9",
                "السكينةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%87%D8%AF%D9%88%D8%A1",
                "السترُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D9%85%D8%A3%D8%AB%D9%88%D8%B1%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D8%A8%D8%B1",
                "الزهد فيما في أيدي الناسُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%85%D8%A3%D8%AB%D9%88%D8%B1%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%B2%D9%87%D8%AF",
                "الرحمةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B1%D8%AD%D9%85%D8%A9",
                "الرحمةُ + https://mawdoo3.com/%D9%83%D9%84%D8%A7%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B1%D8%AD%D9%85%D8%A9",
                "الشكرُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B4%D9%83%D8%B1",
                "الشكرُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%81%D9%8A_%D8%A7%D9%84%D8%AD%D9%85%D8%AF_%D9%88%D8%A7%D9%84%D8%B4%D9%83%D8%B1_%D9%84%D9%84%D9%87",
                "الشفقةُ + https://mawdoo3.com/%D8%A3%D8%AC%D9%85%D9%84_%D8%A7%D9%84%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%A7%D9%84%D8%AD%D9%83%D9%85",
                "الشفقةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AD%D9%8A%D8%A7%D8%A9",
                "الشجاعةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B4%D8%AC%D8%A7%D8%B9%D8%A9",
                "الشجاعةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B4%D8%AC%D8%A7%D8%B9%D8%A9",
                "السماحةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D8%B3%D8%A7%D9%85%D8%AD_%D9%88%D8%A7%D9%84%D8%B9%D9%81%D9%88",
                "السماحةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D8%B3%D8%A7%D9%85%D8%AD",
                "الصمتُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%A7%D9%84%D8%AD%D9%83%D9%85%D8%A7%D8%A1_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D9%85%D8%AA",
                "الصمتُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D9%85%D8%AA",
                "الصِّلةُ والتواصلُ + https://mawdoo3.com/%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D8%AF%D8%A7%D9%82%D8%A9",
                "الصِّلةُ والتواصلُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D8%AF%D8%A7%D9%82%D8%A9",
                "الصدقُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%AC%D9%85%D9%8A%D9%84%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D8%AF%D9%82",
                "الصدقُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D8%AF%D9%82",
                "الصبرُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D8%A8%D8%B1",
                "الصبرُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D8%A8%D8%B1",
                "الشهامةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%85%D8%A3%D8%AB%D9%88%D8%B1%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%B1%D8%AC%D9%88%D9%84%D8%A9",
                "الشهامةُ + https://mawdoo3.com/%D8%A3%D8%AC%D9%85%D9%84_%D9%85%D8%A7_%D9%82%D9%8A%D9%84_%D9%81%D9%8A_%D8%A7%D9%84%D8%B1%D8%AC%D9%88%D9%84%D8%A9",
                "العفوُ والصفحُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D8%B3%D8%A7%D9%85%D8%AD_%D9%88%D8%A7%D9%84%D8%B9%D9%81%D9%88",
                "العزمُ والعزيمةُ وعلوِ الهمةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D9%82%D9%88%D8%A9_%D8%A7%D9%84%D8%A5%D8%B1%D8%A7%D8%AF%D8%A9",
                "العزةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%B9%D8%B2%D8%A9_%D8%A7%D9%84%D9%86%D9%81%D8%B3",
                "العزةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%B9%D8%B2%D8%A9_%D8%A7%D9%84%D9%86%D9%81%D8%B3",
                "العدلُ والإنصافُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%85%D8%A3%D8%AB%D9%88%D8%B1%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%B9%D8%AF%D9%84",
                "العدلُ والإنصافُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B9%D8%AF%D9%84",
                "القناعةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%82%D9%86%D8%A7%D8%B9%D8%A9",
                "القناعةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%82%D9%86%D8%A7%D8%B9%D8%A9",
                "الفصاحةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9",
                "الغيرةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D9%8A%D8%B1%D8%A9",
                "الغيرةُ + https://mawdoo3.com/%D8%B9%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D9%8A%D8%B1%D8%A9",
                "المحبةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%85%D8%AD%D8%A8%D8%A9_%D8%A8%D9%8A%D9%86_%D8%A7%D9%84%D9%86%D8%A7%D8%B3",
                "كظمِ الغيظُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D8%B6%D8%A8",
                "القوةُ + https://mawdoo3.com/%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D9%82%D9%88%D8%A9",
                "القوةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D9%82%D9%88%D8%A9_%D8%A7%D9%84%D8%B4%D8%AE%D8%B5%D9%8A%D8%A9",
                "النشاطُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%B9%D9%85%D9%84_%D9%88%D8%A7%D9%84%D8%AC%D8%AF",
                "النشاطُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%AA%D8%AD%D9%81%D9%8A%D8%B2%D9%8A%D8%A9",
                "المواساةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9",
                "الوفاءُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D9%88%D9%81%D8%A7%D8%A1",
                "الوفاءُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%88%D9%81%D8%A7%D8%A1",
                "النظافةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%86%D8%B8%D8%A7%D9%81%D8%A9",
                "النظافةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D9%86%D8%B8%D8%A7%D9%81%D8%A9",
                "النصيحةُ + https://mawdoo3.com/%D8%A3%D8%AC%D9%85%D9%84_%D9%86%D8%B5%D9%8A%D8%AD%D8%A9",
                "النصرةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D9%86%D8%B5%D8%B1",
                "النصرةُ + https://mawdoo3.com/%D9%83%D9%84%D8%A7%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%86%D8%B5%D8%B1"
            ],
            "اﻷخﻼق المذمومةُ(Bad Quotes)": [
                "الإطراءُ والمدحُ + https://mawdoo3.com/%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A7_%D9%82%D9%8A%D9%84_%D9%81%D9%8A_%D8%A7%D9%84%D9%85%D8%AF%D8%AD",
                "الإطراءُ والمدحُ + https://mawdoo3.com/%D8%B9%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA_%D9%85%D8%AF%D8%AD_%D9%88%D8%AB%D9%86%D8%A7%D8%A1",
                "الإساءةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D9%84%D9%85%D9%86_%D8%A3%D8%B3%D8%A7%D8%A1_%D8%A5%D9%84%D9%8A%D9%83",
                "البخلُ والشحُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%A8%D8%AE%D9%84",
                "الانتقامُ + https://mawdoo3.com/%D9%83%D9%84%D9%85%D8%A7%D8%AA_%D8%B9%D9%86_%D8%A7%D9%84%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%85",
                "الإفراطُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9",
                "الافتراءُ والبهتانُ + https://mawdoo3.com/%D8%B9%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA_%D8%B9%D9%86_%D8%A7%D9%84%D9%83%D8%B0%D8%A8_%D9%88%D8%A7%D9%84%D8%AE%D8%AF%D8%A7%D8%B9",
                "التسرعُ والتهورُ والعجلةُ + https://mawdoo3.com/%D8%A3%D8%AC%D9%85%D9%84_%D8%A7%D9%84%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%A7%D9%84%D8%AD%D9%83%D9%85",
                "التخاذلُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AE%D8%B0%D9%84%D8%A7%D9%86",
                "التخاذلُ + https://mawdoo3.com/%D8%B9%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA_%D8%B9%D9%86_%D8%AE%D8%B0%D9%84%D8%A7%D9%86_%D8%A3%D9%82%D8%B1%D8%A8_%D8%A7%D9%84%D9%86%D8%A7%D8%B3",
                "البغضُ والكراهيةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D9%83%D8%B1%D8%A7%D9%87%D9%8A%D8%A9",
                "البطرُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9_%D8%AC%D9%85%D9%8A%D9%84%D8%A9",
                "البطرُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%84%D8%A6%D9%8A%D9%85",
                "التفريطُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%81%D9%8A_%D8%A7%D9%84%D8%AA%D8%B9%D8%A7%D9%85%D9%84_%D9%85%D8%B9_%D8%A7%D9%84%D9%86%D8%A7%D8%B3",
                "التفريطُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D9%88%D8%A8%D8%B9%D8%B6_%D8%A7%D9%84%D9%83%D9%84%D8%A7%D9%85",
                "التعصبُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D8%B6%D8%A8",
                "التعاليُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D9%83%D8%A8%D8%B1",
                "التعاليُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D9%83%D8%A8%D8%B1",
                "الجزعُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9",
                "الجزعُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B5%D8%A8%D8%B1",
                "الجبنُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AC%D8%A8%D9%86%D8%A7%D8%A1",
                "الثرثرةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%83%D9%84%D8%A7%D9%85",
                "الخداعُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D8%AF%D8%B1_%D9%88%D8%A7%D9%84%D8%AE%D8%AF%D8%A7%D8%B9",
                "الخداعُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AE%D8%AF%D8%A7%D8%B9",
                "الخبثُ + https://mawdoo3.com/%D8%B9%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA_%D8%B9%D9%86_%D8%A7%D9%84%D8%AE%D8%A8%D8%AB",
                "الحقدُ + https://mawdoo3.com/%D9%83%D9%84%D9%85%D8%A7%D8%AA_%D8%B9%D9%86_%D8%A7%D9%84%D8%AD%D9%82%D8%AF_%D9%88%D8%A7%D9%84%D8%BA%D9%8A%D8%B1%D8%A9",
                "الحقدُ + https://mawdoo3.com/%D9%83%D9%84%D9%85%D8%A7%D8%AA_%D8%B9%D9%86_%D8%A7%D9%84%D8%AD%D9%82%D8%AF_%D9%88%D8%A7%D9%84%D8%AD%D8%B3%D8%AF",
                "الحسدُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AD%D8%B3%D8%AF",
                "الحسدُ + https://mawdoo3.com/%D9%83%D9%84%D9%85%D8%A7%D8%AA_%D8%B9%D9%86_%D8%A7%D9%84%D8%AD%D8%B3%D8%AF",
                "الجفاءُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D9%88%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D9%88%D9%81%D8%A7%D8%A1",
                "الذلُ + https://mawdoo3.com/%D9%83%D9%84%D9%85%D8%A7%D8%AA_%D8%B9%D9%86_%D8%A7%D9%84%D8%B0%D9%84",
                "الذلُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B0%D9%84",
                "الخيانةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AE%D9%8A%D8%A7%D9%86%D8%A9_%D9%88%D8%A7%D9%84%D8%BA%D8%AF%D8%B1",
                "الخيانةُ + https://mawdoo3.com/%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AE%D9%8A%D8%A7%D9%86%D8%A9_%D9%88%D8%A7%D9%84%D8%BA%D8%AF%D8%B1",
                "خلف الوعدُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%88%D8%B9%D8%AF",
                "خلف الوعدُ + https://mawdoo3.com/%D9%83%D9%84%D8%A7%D9%85_%D8%B9%D9%86_%D8%A5%D8%AE%D9%84%D8%A7%D9%81_%D8%A7%D9%84%D9%88%D8%B9%D8%AF",
                "الخِذلانُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AE%D8%B0%D9%84%D8%A7%D9%86",
                "الخِذلانُ + https://mawdoo3.com/%D8%B9%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA_%D8%B9%D9%86_%D8%AE%D8%B0%D9%84%D8%A7%D9%86_%D8%A3%D9%82%D8%B1%D8%A8_%D8%A7%D9%84%D9%86%D8%A7%D8%B3",
                "سوء الجوارُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%AC%D8%A7%D8%B1",
                "السفهُ والحُمقُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B3%D9%81%D9%87%D8%A7%D8%A1",
                "الظلمُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B8%D9%84%D9%85",
                "الظلمُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B8%D9%84%D9%85_%D9%88%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D8%A8%D8%AF%D8%A7%D8%AF",
                "الطمعُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%B7%D9%85%D8%B9",
                "الطمعُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B7%D9%85%D8%B9",
                "سوء الظنُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D9%81%D9%8A_%D8%B3%D9%88%D8%A1_%D8%A7%D9%84%D8%B8%D9%86",
                "سوء الظنُ + https://mawdoo3.com/%D8%B9%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA_%D8%B9%D9%86_%D8%B3%D9%88%D8%A1_%D8%A7%D9%84%D8%B8%D9%86_%D8%A8%D8%A7%D9%84%D9%86%D8%A7%D8%B3",
                "الغشُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D8%B4",
                "الغشُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D8%B4",
                "الغدرُ ونقض العهدُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D8%AF%D8%B1",
                "الغدرُ ونقض العهدُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AE%D9%8A%D8%A7%D9%86%D8%A9_%D9%88%D8%A7%D9%84%D8%BA%D8%AF%D8%B1",
                "العبوسُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D9%81%D8%A7%D8%A4%D9%84",
                "العبوسُ + https://mawdoo3.com/%D8%A7%D8%B4%D9%87%D8%B1_%D9%85%D9%82%D9%88%D9%84%D8%A7%D8%AA_%D8%A7%D9%84%D8%B9%D8%B8%D9%85%D8%A7%D8%A1",
                "الفجورُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D9%81%D8%B1%D8%AC",
                "الغيبةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D9%8A%D8%A8%D8%A9",
                "الغضبُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D8%B6%D8%A8",
                "اللامبالاةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%84%D8%A7%D9%85%D8%A8%D8%A7%D9%84%D8%A7%D8%A9",
                "اللامبالاةُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D9%84%D8%A7%D9%85%D8%A8%D8%A7%D9%84%D8%A7%D8%A9",
                "الكذبُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%83%D8%B0%D8%A8",
                "الكذبُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D9%83%D8%B0%D8%A8",
                "الكبرُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D9%83%D8%A8%D8%B1",
                "الكبرُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D8%AA%D9%83%D8%A8%D8%B1",
                "نكران الجميلُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D9%86%D9%83%D8%B1%D8%A7%D9%86_%D8%A7%D9%84%D8%AC%D9%85%D9%8A%D9%84",
                "نكران الجميلُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D9%81%D9%8A_%D9%86%D9%83%D8%B1%D8%A7%D9%86_%D8%A7%D9%84%D8%AC%D9%85%D9%8A%D9%84",
                "النفاقُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%85%D8%A3%D8%AB%D9%88%D8%B1%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D9%86%D9%81%D8%A7%D9%82",
                "النفاقُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D9%81%D9%8A_%D8%A7%D9%84%D9%85%D9%86%D8%A7%D9%81%D9%82%D9%8A%D9%86",
                "المنُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9_%D9%85%D8%A3%D8%AB%D9%88%D8%B1%D8%A9",
                "المنُ + https://mawdoo3.com/%D8%A7%D8%AC%D9%85%D9%84_%D8%A7%D9%84%D8%AD%D9%83%D9%85_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9",
                "اليأسُ والقنوطُ والإحباطُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D9%88%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D8%A7%D9%84%D9%8A%D8%A3%D8%B3",
                "اليأسُ والقنوطُ والإحباطُ + https://mawdoo3.com/%D8%B9%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA_%D8%B9%D9%86_%D8%A7%D9%84%D9%8A%D8%A3%D8%B3",
                "الوهنُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D8%B6%D8%B9%D9%81",
                "الوهنُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85_%D8%B9%D9%86_%D9%86%D9%81%D8%A7%D8%B0_%D8%A7%D9%84%D8%B5%D8%A8%D8%B1_%D9%88%D9%82%D9%84%D8%A9_%D8%A7%D9%84%D8%AD%D9%8A%D9%84%D8%A9",
                "الهجرُ + https://mawdoo3.com/%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%B9%D9%86_%D8%A7%D9%84%D9%87%D8%AC%D8%B1%D8%A9",
                "النميمةُ + https://mawdoo3.com/%D8%AD%D9%83%D9%85%D8%A9_%D8%B9%D9%86_%D8%A7%D9%84%D8%BA%D9%8A%D8%A8%D8%A9"
            ]
        }
    }   
}
def scrape_page(url, output_file):
    try:
        # Send GET request to the URL
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extracting the Arabic proverbs from specific divs
            proverbs_section = soup.find('div', {'id': 'mw-content-text'})
            
            # Get all list items (li) inside this section
            if proverbs_section:
                proverbs_list = proverbs_section.find_all('li')
                for proverb in proverbs_list:
                    # Write each proverb to the file
                    output_file.write(proverb.get_text() + '\n')
            else:
                print(f"Couldn't find the proverbs section in the page: {url}")
        else:
            print(f"Error: Unable to retrieve the page. Status code {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {str(e)}")

# Open a file to save the proverbs
with open('arabic_proverbs.txt', 'w', encoding='utf-8') as output_file:
    # Loop over each category in the mawdoo3_urls dictionary
    for category, details in mawdoo3_urls.items():
        for class_name, urls in details["classes"].items():
            for url in urls:
                # Extract the actual URL from the string
                if '+' in url:  # To separate the proverb from the URL
                    proverb_text, proverb_url = url.split(' + ')
                    print(f"Scraping URL: {proverb_url.strip()}")
                    scrape_page(proverb_url.strip(), output_file)
                    output_file.write("\n" + "="*40 + "\n")  # Add a separator between different pages

print("Scraping completed. Data saved to 'arabic_proverbs.txt'.")
