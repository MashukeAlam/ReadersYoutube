from urllib import request
import json

def get_vdo_id(videourl: str) -> str:
    return videourl[videourl.find('?v=') + 3:].split('&')[0]

def give_caption_url(videourl: str) -> str:
    res = request.urlopen(videourl)
    if res.status == 200:
        res_str = res.read().decode('utf-8')
        seg = '"captionTracks":[{"baseUrl":"'
        url = res_str[res_str.find(seg) + len(seg):].split('"')[0]
        for_json = 'en&fmt=json3&xorb=2&xobt=3&xovt=3'
        return url.replace('\\u0026', '&')[:-2] + for_json

def json_parse(caption_url: str) -> dict:
    res = request.urlopen(caption_url)
    print(caption_url)
    if res.status == 200:
        js_str = res.read().decode('utf-8')
        js_data = json.loads(js_str)
        return js_data

def make_captions(json_data: dict) -> str:
    captions = ""
    for i, item in enumerate(json_data['events']):
        # print(item)
        if i == 0:
            continue
        for j in item['segs']:

            captions += (j['utf8'])
        
    return captions.replace('\n', ' ')

def write_to_file(string: str) -> None:
    f = open(get_vdo_id(URL), 'w')
    f.write(string)



if __name__ == "__main__":
    URL = input("give the url please: ")
    print(write_to_file(make_captions(json_parse(give_caption_url(URL)))))