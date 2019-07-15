import json
import os
import re

import jsonlines

from settings import BASE_DIR

# NOTICE: CHANGE the jsonl_file_path source path (I didn't include the 100MB file provided in the repo for confidentiality reasons so remember to provide the path to your own version of the data !)
jsonl_file_path = os.path.join(os.path.dirname(BASE_DIR), "garment_items.jl") # CHANGE IF REPRODUCING WITH OWN DATA FILE
garment_fixtures_fp = os.path.join(os.path.join(os.path.join(
    os.path.dirname(BASE_DIR), "api\\core"), 'fixtures'), 'DB_LOAD-garment_items.json')
image_fixtures_fp = os.path.join(os.path.join(os.path.join(
    os.path.dirname(BASE_DIR), "api\\core"), 'fixtures'), 'DB_LOAD-image_items.json')

GARMENTS_LIST = list()
IMAGES_LIST = list()

CHOSEN_APPROACH = 'PERFORM_DATA_LOAD'
TEST_ON_CONTRIVED_DATA = False

if CHOSEN_APPROACH is 'PERFORM_DATA_LOAD' :
    if TEST_ON_CONTRIVED_DATA:
        garment_fixtures_fp = os.path.join(os.path.join(os.path.join(
            os.path.dirname(BASE_DIR), "api\\core"), 'fixtures'), 'test_garment_items.json')
        image_fixtures_fp = os.path.join(os.path.join(os.path.join(
            os.path.dirname(BASE_DIR), "api\\core"), 'fixtures'), 'test_image_items.json')
    with jsonlines.open(jsonl_file_path) as jl:
        for i, garment in enumerate(jl):
            # Change the values of ('flatten') single-element-array elements to avoid serialisation issues.
            image_urls_val = garment.get('image_urls', [''])[0]
            garment['image_urls'] = image_urls_val
            product_categories = garment.get('product_categories', [''])[0]
            garment['product_categories'] = product_categories
            product_categories_mapped = garment.get('product_categories_mapped', [None])[0]
            garment['product_categories_mapped'] = product_categories_mapped
            product_imgs_src = garment.get('product_imgs_src', [''])[0]
            garment['product_imgs_src'] = product_imgs_src

            # Account for the "price" attribute not compliant with Python's Decimal class in the original S3 file: 
            # i.e. change 'price' string to have prices e.g. "1140.00" instead of "1,140.00"
            garment['price'] = garment['price'].replace(r',', '') 

            # Make the data structure root compliant with django's loaddata procedure.
            new_garment_object= dict()
            new_garment_object['model'] = "core.garment"
            new_garment_object['pk'] = garment['product_id']
            new_garment_object['fields'] = dict()
            for key,value in garment.items():
                if key != 'product_id' and key != 'images' :
                    new_garment_object['fields'][key] = value
            # NOTICE: some data in the provided S3 file has NULL value of the "images" property, so I need to account for that below with try/except and "image_for_garment" conditional logic.
            try:
                image_for_garment = garment['images'][0]
            except IndexError: 
                image_for_garment = None
            if  image_for_garment is not None:
                new_garment_object['fields']['images_id'] = garment['images'][0]['url']
            else:
                new_garment_object['fields']['images_id'] = None
            GARMENTS_LIST.append(new_garment_object) # Add garment object to the master garments list. 
            # Make the images data structure compliant with how we set up "Image" model class (only if image exists for a given garment):
            if image_for_garment is not None:
                new_image_object = dict()
                new_image_object['model'] = "core.image"
                new_image_object['pk'] = garment['images'][0]['url']
                new_image_object['fields'] = dict()
                for key,value in garment['images'][0].items():
                    if key != 'url':
                        new_image_object['fields'][key] = value
                IMAGES_LIST.append(new_image_object) # Add image object to the master images list.

            # This is for testing on a limited amount of data (mostly just one garment object)
            if TEST_ON_CONTRIVED_DATA and i >= 0:
                break

        with open(garment_fixtures_fp, 'w') as f:
            json.dump(GARMENTS_LIST, f, indent=2)
        with open(image_fixtures_fp, 'w') as f:
            json.dump(IMAGES_LIST, f, indent=2)
# Below I checked length of properties so that my model has an appropriate "max_length" value set for each field reflecting the size of the actual data.  
elif CHOSEN_APPROACH is 'test_data_attributes':
    max_len = 0
    with jsonlines.open(jsonl_file_path) as jl:
        for i, garment in enumerate(jl):
            max_len = garment['product_categories_mapped'][0] if max_len < garment['product_categories_mapped'][0] else max_len
        print (max_len)
