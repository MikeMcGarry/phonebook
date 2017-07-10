import re

keys = {"phone": ["p", "ph", "phone", "t", "te", "tel", "tele", "telephone", "phone", "d", "dir", "direct"],
        "mobile": ["m", "mob", "mobile", "cell"]
        }


def isolate(start, search_string):
    re_find = re.compile('(?<={}[\:\.\-\s])\s*[0-9\+)(]+?[0-9\+\s)(]+?(?=[^0-9\s\+)(])'.format(start), re.I)
    re_compute = re.search(re_find, search_string)
    re_result = re_compute.group(0)    
    return re_result

output = {}

#your_landline = insert landline here as it appears in your signature
#your_mobile = insert mobile here as it appears in your signature

for key in keys:
    for value in keys[key]:
        
            
            try:
                answer = isolate(value,input_data["body"])
                answer_stripped = answer.strip()
                if answer_stripped != your_landline and answer_stripped != your_mobile and len(answer_stripped) > 8:
                    
                    output[key] = answer_stripped
                    
      
            except:
                pass